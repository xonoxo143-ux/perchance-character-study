(() => {
  "use strict";

  const DEFAULT_CONFIG = {
    owner: "xonoxo143-ux",
    repo: "perchance-character-study",
    ref: "perchance-runtime",
    runtimePath: "runtime",
    characterId: "yvette",
    autoApply: false
  };

  const CONFIG = {...DEFAULT_CONFIG, ...(window.LB_GITHUB_RUNTIME_CONFIG || {})};
  const CACHE_KEY = "lbGithubRuntimeCacheV1";
  const STATUS_KEY = "lbGithubRuntimeStatusV1";

  const baseUrl = () => `https://raw.githubusercontent.com/${CONFIG.owner}/${CONFIG.repo}/${CONFIG.ref}/${CONFIG.runtimePath}`;
  const rawUrl = path => `${baseUrl()}/${String(path).replace(/^runtime\//, "")}`;

  function threadData() {
    oc.thread.customData ||= {};
    return oc.thread.customData;
  }

  function cache() {
    const data = threadData();
    data[CACHE_KEY] ||= {manifest: null, packs: {}, shared: {}};
    return data[CACHE_KEY];
  }

  function setStatus(status, detail = "") {
    threadData()[STATUS_KEY] = {
      status,
      detail,
      time: Date.now(),
      ref: CONFIG.ref,
      characterId: CONFIG.characterId
    };
  }

  async function fetchJson(path) {
    const url = rawUrl(path);
    const response = await fetch(url, {cache: "no-store"});
    if (!response.ok) throw new Error(`GitHub runtime fetch failed: ${response.status} ${url}`);
    return response.json();
  }

  function validateManifest(manifest) {
    if (!manifest || manifest.schema !== "lb-perchance-runtime-manifest-v1") throw new Error("Unsupported runtime manifest schema.");
    if (!manifest.characters || typeof manifest.characters !== "object") throw new Error("Runtime manifest has no character map.");
    return manifest;
  }

  function validatePack(pack, expectedId) {
    if (!pack || pack.schema !== "lb-character-pack-v1") throw new Error("Unsupported character pack schema.");
    if (expectedId && pack.id !== expectedId) throw new Error(`Character pack ID mismatch: expected ${expectedId}, got ${pack.id}.`);
    if (!pack.character || typeof pack.character.roleInstruction !== "string") throw new Error("Character pack has no roleInstruction.");
    return pack;
  }

  async function loadManifest({network = true} = {}) {
    const c = cache();
    if (network) {
      try {
        const manifest = validateManifest(await fetchJson("manifest.json"));
        c.manifest = manifest;
        setStatus("manifest-online", `runtimeVersion ${manifest.runtimeVersion}`);
        return manifest;
      } catch (error) {
        console.warn("LB GitHub runtime manifest fetch failed; trying cache.", error);
      }
    }
    if (c.manifest) {
      setStatus("manifest-cache", "Using last-known-good manifest.");
      return validateManifest(c.manifest);
    }
    throw new Error("No runtime manifest is available online or in cache.");
  }

  async function loadCharacter(characterId = CONFIG.characterId, {network = true} = {}) {
    const manifest = await loadManifest({network});
    const entry = manifest.characters?.[characterId];
    if (!entry || entry.enabled === false) throw new Error(`Character '${characterId}' is not enabled in the runtime manifest.`);

    const c = cache();
    if (network) {
      try {
        const pack = validatePack(await fetchJson(entry.path), characterId);
        c.packs[characterId] = pack;
        setStatus("pack-online", `${characterId}@${pack.version}`);
        return pack;
      } catch (error) {
        console.warn(`LB GitHub runtime pack fetch failed for ${characterId}; trying cache.`, error);
      }
    }

    const cached = c.packs?.[characterId];
    if (cached) {
      const pack = validatePack(cached, characterId);
      setStatus("pack-cache", `${characterId}@${pack.version}`);
      return pack;
    }
    throw new Error(`No cached runtime pack exists for '${characterId}'.`);
  }

  async function loadShared(key, {network = true} = {}) {
    const manifest = await loadManifest({network});
    const path = manifest.shared?.[key];
    if (!path) throw new Error(`Shared runtime module '${key}' is not registered.`);
    const c = cache();

    if (network) {
      try {
        const value = await fetchJson(path);
        c.shared[key] = value;
        setStatus("shared-online", key);
        return value;
      } catch (error) {
        console.warn(`LB GitHub runtime shared fetch failed for ${key}; trying cache.`, error);
      }
    }

    if (c.shared?.[key]) {
      setStatus("shared-cache", key);
      return c.shared[key];
    }
    throw new Error(`No cached shared runtime module exists for '${key}'.`);
  }

  function applyCharacter(pack, options = {}) {
    validatePack(pack, options.expectedId || pack.id);
    const character = pack.character;
    const applyName = options.name !== false;
    const applyRole = options.roleInstruction !== false;
    const applyReminder = options.reminderMessage !== false;

    if (applyName && typeof pack.name === "string") oc.thread.character.name = pack.name;
    if (applyRole) oc.thread.character.roleInstruction = character.roleInstruction;
    if (applyReminder) oc.thread.character.reminderMessage = character.reminderMessage || "";

    const data = threadData();
    data.lbGithubRuntimeAppliedV1 = {
      id: pack.id,
      version: pack.version,
      ref: CONFIG.ref,
      time: Date.now()
    };
    data.lbGithubRuntimeBaseRoleV1 = character.roleInstruction;
    setStatus("applied", `${pack.id}@${pack.version}`);
    return pack;
  }

  async function refresh(characterId = CONFIG.characterId, options = {}) {
    const pack = await loadCharacter(characterId, {network: options.network !== false});
    if (options.apply !== false) applyCharacter(pack, {expectedId: characterId});
    return pack;
  }

  async function start(options = {}) {
    const characterId = options.characterId || CONFIG.characterId;
    try {
      const pack = await refresh(characterId, {network: options.network !== false, apply: options.apply !== false});
      return {ok: true, pack, status: threadData()[STATUS_KEY]};
    } catch (error) {
      setStatus("error", error?.message || String(error));
      console.error("LB GitHub runtime failed to start.", error);
      return {ok: false, error, status: threadData()[STATUS_KEY]};
    }
  }

  window.lbGithubRuntime = {
    config: {...CONFIG},
    baseUrl: baseUrl(),
    loadManifest,
    loadCharacter,
    loadShared,
    applyCharacter,
    refresh,
    start,
    getStatus: () => threadData()[STATUS_KEY] || null,
    getCache: () => cache()
  };

  if (CONFIG.autoApply) start();
})();

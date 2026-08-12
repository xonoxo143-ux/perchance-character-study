(async () => {
  "use strict";

  const LOADER_URL = "https://raw.githubusercontent.com/xonoxo143-ux/perchance-character-study/perchance-runtime/runtime/perchance/github-runtime-loader.js";

  window.LB_GITHUB_RUNTIME_CONFIG = {
    owner: "xonoxo143-ux",
    repo: "perchance-character-study",
    ref: "perchance-runtime",
    runtimePath: "runtime",
    characterId: "yvette",
    autoApply: false
  };

  try {
    if (!window.lbGithubRuntime) {
      const response = await fetch(LOADER_URL, {cache: "no-store"});
      if (!response.ok) throw new Error(`Runtime loader fetch failed: ${response.status}`);
      const source = await response.text();
      const script = document.createElement("script");
      script.textContent = `${source}\n//# sourceURL=lb-github-runtime-loader.js`;
      document.head.appendChild(script);
      script.remove();
    }

    if (!window.lbGithubRuntime) throw new Error("Runtime loader did not initialize.");
    const result = await window.lbGithubRuntime.start({characterId: "yvette", apply: true});
    if (!result.ok) throw result.error || new Error("Runtime start failed.");
    console.info(`LB GitHub runtime loaded Yvette ${result.pack.version}.`);
  } catch (error) {
    console.error("LB Yvette GitHub bootstrap failed.", error);
  }
})();

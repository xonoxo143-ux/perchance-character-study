# Perchance Runtime

This directory is the runtime-facing layer for Perchance custom-code characters.

It is intentionally separate from `library/`, `source-material/`, and the rest of the research corpus. Files here should be small, stable, machine-readable, and safe for a public client to fetch directly.

## Goals

- Let a Perchance character load its character pack from GitHub.
- Keep reusable behavior/config outside exported Perchance JSON files.
- Make character changes versionable, diffable, and reversible.
- Avoid embedding secrets or private tokens in client-side custom code.
- Cache last-known-good data in the Perchance thread so a transient network failure does not destroy a working character.

## Layout

```text
runtime/
  manifest.json
  characters/
    _template.json
    yvette.json
  shared/
    enchantments.json
  schema/
    character-pack.schema.json
  perchance/
    github-runtime-loader.js
```

## Runtime contract

`manifest.json` is the entry point. It maps stable character IDs to runtime pack files.

A character pack contains the text/settings that custom code may apply to `oc.thread.character` plus optional shared-module references. It is not a full Perchance database export.

The loader should:

1. fetch the manifest;
2. resolve the requested character pack;
3. validate the pack's schema/version;
4. cache the last-known-good copy in `oc.thread.customData`;
5. apply only fields the caller explicitly permits;
6. fall back to cache when GitHub cannot be reached.

## Development branch

During development, raw files are read from the `perchance-runtime` branch. After the system is proven, the runtime ref can be pinned to a release tag or merged to `main`.

## Security

Everything under this directory is public. Never store GitHub PATs, API keys, passwords, private prompts, or other secrets here. Perchance custom code is client-side code and must be treated as inspectable.

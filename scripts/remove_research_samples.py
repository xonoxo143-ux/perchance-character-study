#!/usr/bin/env python3
"""Remove invalid Character Shape Research samples from ledgers.

This is intended for cleanup of entries that were appended from insufficient source
evidence. It removes accepted entries from SAMPLED_CHARACTERS.md by sample ID,
optionally deletes batch files, updates next-batch markers, and adds a durable
source-evidence rule to the protocol.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACCEPTED_LEDGER = ROOT / "research" / "SAMPLED_CHARACTERS.md"
REJECTED_LEDGER = ROOT / "research" / "REJECTED_CHARACTERS.md"
PROTOCOL_FILE = ROOT / "research" / "CHARACTER_SHAPE_RESEARCH.md"
DEFAULT_REQUEST_DIR = ROOT / "research" / "cleanup"

HEADING_RE = re.compile(r"^##\s+(\d{3})\s+—\s+(.+?)\s*$", re.MULTILINE)
NEXT_BATCH_RE = re.compile(r"The next batch starts at `\d{3}–\d{3}`\.")
NEXT_STEP_RE = re.compile(r"Continue with candidate triage for samples \d{3}–\d{3}\.")
SOURCE_RULE_HEADING = "## Source Evidence Rule"
SOURCE_RULE_TEXT = """## Source Evidence Rule

Do not create full sample entries from example-list names, screenshots, search-result snippets, or URL slugs alone.

Those weak sources may identify candidates, but they do not support a full Character Core extraction.

A full accepted or rejected sample entry must be grounded in at least one of:

- actual `manifest.json` content
- exported character JSON
- decompressed card/share data
- actual repo file content containing the character fields

If the source is only a UI/name observation, record it as a candidate note, not as a sampled character.
"""


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_request(path: Path) -> tuple[set[int], list[Path]]:
    text = read_text(path)
    ids: set[int] = set()
    delete_files: list[Path] = []
    in_delete_files = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("sample_ids:"):
            value = line.split(":", 1)[1]
            ids.update(int(x) for x in re.findall(r"\b\d{3}\b", value))
            in_delete_files = False
            continue
        if line.lower().startswith("delete_files:"):
            in_delete_files = True
            continue
        if in_delete_files and line.startswith("-"):
            file_path = line[1:].strip()
            if file_path:
                delete_files.append(ROOT / file_path)
            continue
    return ids, delete_files


def split_ledger_entries(text: str) -> tuple[str, list[str]]:
    # Split on separators immediately before sample headings.
    parts = re.split(r"\n---\n\n(?=##\s+\d{3}\s+—\s+)", text.rstrip())
    if not parts:
        return text, []
    header = parts[0]
    entries = parts[1:]
    return header, entries


def entry_id(entry: str) -> int | None:
    match = HEADING_RE.search(entry)
    return int(match.group(1)) if match else None


def remove_entries_from_accepted(ids_to_remove: set[int]) -> tuple[list[int], list[int]]:
    text = read_text(ACCEPTED_LEDGER)
    header, entries = split_ledger_entries(text)
    removed: list[int] = []
    kept: list[str] = []

    for entry in entries:
        sid = entry_id(entry)
        if sid in ids_to_remove:
            removed.append(sid)
            continue
        kept.append(entry.strip())

    if removed:
        if kept:
            new_text = header.rstrip() + "\n\n---\n\n" + "\n\n---\n\n".join(kept).strip() + "\n"
        else:
            new_text = header.rstrip() + "\n"
        write_text(ACCEPTED_LEDGER, new_text)

    missing = sorted(ids_to_remove - set(removed))
    return sorted(removed), missing


def final_sample_ids() -> list[int]:
    ids: set[int] = set()
    for path in [ACCEPTED_LEDGER, REJECTED_LEDGER]:
        for match in HEADING_RE.finditer(read_text(path)):
            ids.add(int(match.group(1)))
    return sorted(ids)


def next_batch_after_current_final() -> str:
    ids = final_sample_ids()
    start = (max(ids) + 1) if ids else 1
    end = start + 2
    return f"{start:03d}–{end:03d}"


def update_next_batch_markers(path: Path, next_batch: str) -> None:
    text = read_text(path)
    if not text:
        return
    text = NEXT_BATCH_RE.sub(f"The next batch starts at `{next_batch}`.", text)
    text = NEXT_STEP_RE.sub(f"Continue with candidate triage for samples {next_batch}.", text)
    write_text(path, text)


def add_source_rule_to_protocol() -> None:
    text = read_text(PROTOCOL_FILE)
    if not text or SOURCE_RULE_HEADING in text:
        return
    anchor = "## Research Position\n"
    if anchor in text:
        text = text.replace(anchor, SOURCE_RULE_TEXT + "\n" + anchor, 1)
    else:
        text = text.rstrip() + "\n\n" + SOURCE_RULE_TEXT
    write_text(PROTOCOL_FILE, text)


def delete_requested_files(paths: list[Path]) -> list[str]:
    deleted: list[str] = []
    for path in paths:
        try:
            resolved = path.resolve()
            resolved.relative_to(ROOT.resolve())
        except Exception as exc:
            raise ValueError(f"refusing to delete path outside repo: {path}") from exc
        if path.exists():
            path.unlink()
            deleted.append(str(path.relative_to(ROOT)))
    return deleted


def find_request_files(request_file: str | None, request_dir: Path) -> list[Path]:
    if request_file:
        return [ROOT / request_file]
    if not request_dir.exists():
        return []
    return sorted(request_dir.glob("REMOVE_*.txt"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request-file", help="Specific cleanup request file")
    parser.add_argument("--request-dir", default=str(DEFAULT_REQUEST_DIR), help="Directory containing cleanup requests")
    args = parser.parse_args()

    ids_to_remove: set[int] = set()
    files_to_delete: list[Path] = []

    request_files = find_request_files(args.request_file, Path(args.request_dir))
    if not request_files:
        print("No cleanup request files found. Nothing to remove.")
        return 0

    for request in request_files:
        ids, delete_files = parse_request(request)
        ids_to_remove.update(ids)
        files_to_delete.extend(delete_files)

    if not ids_to_remove and not files_to_delete:
        print("Cleanup requests contained no sample_ids or delete_files. Nothing to remove.")
        return 0

    removed, missing = remove_entries_from_accepted(ids_to_remove)
    deleted = delete_requested_files(files_to_delete)
    add_source_rule_to_protocol()

    next_batch = next_batch_after_current_final()
    update_next_batch_markers(ACCEPTED_LEDGER, next_batch)
    update_next_batch_markers(PROTOCOL_FILE, next_batch)

    print("Cleanup complete.")
    print("Removed accepted samples:", ", ".join(f"{x:03d}" for x in removed) or "none")
    print("Requested sample IDs not found in accepted ledger:", ", ".join(f"{x:03d}" for x in missing) or "none")
    print("Deleted files:", ", ".join(deleted) or "none")
    print("Next batch:", next_batch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

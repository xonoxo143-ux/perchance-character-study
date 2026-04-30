#!/usr/bin/env python3
"""Append accepted Character Shape Research batch entries into the main ledger.

This script is intentionally conservative:
- It only reads entries between ACCEPTED_APPEND_START and ACCEPTED_APPEND_END markers.
- It refuses to append duplicate sample headings already present in the target ledger.
- It can process one batch file or all marked batch files.
- It updates simple next-batch marker text when possible.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

START_MARKER = "<!-- ACCEPTED_APPEND_START -->"
END_MARKER = "<!-- ACCEPTED_APPEND_END -->"
DEFAULT_TARGET = Path("research/SAMPLED_CHARACTERS.md")
DEFAULT_BATCH_DIR = Path("research/batches")

HEADING_RE = re.compile(r"^##\s+(\d{3})\s+—\s+(.+?)\s*$", re.MULTILINE)
NEXT_BATCH_RE = re.compile(r"The next batch starts at `\d{3}–\d{3}`\.")
NEXT_STEP_RE = re.compile(r"Continue with candidate triage for samples \d{3}–\d{3}\.")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def extract_marked_block(batch_text: str, batch_path: Path) -> str | None:
    if START_MARKER not in batch_text and END_MARKER not in batch_text:
        return None
    if START_MARKER not in batch_text or END_MARKER not in batch_text:
        raise ValueError(f"{batch_path}: found only one append marker; expected both")

    start = batch_text.index(START_MARKER) + len(START_MARKER)
    end = batch_text.index(END_MARKER)
    if end <= start:
        raise ValueError(f"{batch_path}: append end marker comes before start marker")

    block = batch_text[start:end].strip()
    if not block:
        raise ValueError(f"{batch_path}: append block is empty")
    return block


def split_entries(block: str, batch_path: Path) -> list[str]:
    matches = list(HEADING_RE.finditer(block))
    if not matches:
        raise ValueError(f"{batch_path}: append block contains no sample headings")

    entries: list[str] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(block)
        entry = block[start:end].strip()
        entries.append(entry)
    return entries


def sample_ids(entries: Iterable[str]) -> list[int]:
    ids: list[int] = []
    for entry in entries:
        match = HEADING_RE.search(entry)
        if not match:
            raise ValueError("entry missing sample heading")
        ids.append(int(match.group(1)))
    return ids


def already_present(target_text: str, sample_id: int) -> bool:
    return re.search(rf"^##\s+{sample_id:03d}\s+—\s+", target_text, re.MULTILINE) is not None


def append_entries(target_text: str, entries: list[str]) -> tuple[str, list[int], list[int]]:
    appended: list[int] = []
    skipped: list[int] = []
    chunks: list[str] = []

    for entry in entries:
        sid = sample_ids([entry])[0]
        if already_present(target_text, sid):
            skipped.append(sid)
            continue
        chunks.append(entry)
        appended.append(sid)

    if not chunks:
        return target_text, appended, skipped

    new_text = target_text.rstrip() + "\n\n---\n\n" + "\n\n---\n\n".join(chunks).strip() + "\n"
    return new_text, appended, skipped


def next_batch_text(last_seen_id: int) -> str:
    start = last_seen_id + 1
    end = start + 2
    return f"{start:03d}–{end:03d}"


def update_next_batch_markers(text: str, next_batch: str) -> str:
    text = NEXT_BATCH_RE.sub(f"The next batch starts at `{next_batch}`.", text)
    text = NEXT_STEP_RE.sub(f"Continue with candidate triage for samples {next_batch}.", text)
    return text


def find_batch_files(batch_file: str | None, batch_dir: Path) -> list[Path]:
    if batch_file:
        return [Path(batch_file)]
    if not batch_dir.exists():
        return []
    return sorted(batch_dir.glob("BATCH_*.md"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-file", help="Specific batch file to process")
    parser.add_argument("--target-file", default=str(DEFAULT_TARGET), help="Accepted ledger file")
    parser.add_argument("--batch-dir", default=str(DEFAULT_BATCH_DIR), help="Batch file directory")
    parser.add_argument("--protocol-file", default="research/CHARACTER_SHAPE_RESEARCH.md")
    args = parser.parse_args()

    target_path = Path(args.target_file)
    protocol_path = Path(args.protocol_file)
    batch_files = find_batch_files(args.batch_file, Path(args.batch_dir))

    if not target_path.exists():
        raise FileNotFoundError(f"target file missing: {target_path}")

    target_text = read_text(target_path)
    all_appended: list[int] = []
    all_skipped: list[int] = []
    saw_marked_batch = False

    for batch_path in batch_files:
        if not batch_path.exists():
            raise FileNotFoundError(f"batch file missing: {batch_path}")
        batch_text = read_text(batch_path)
        block = extract_marked_block(batch_text, batch_path)
        if block is None:
            continue
        saw_marked_batch = True
        entries = split_entries(block, batch_path)
        target_text, appended, skipped = append_entries(target_text, entries)
        all_appended.extend(appended)
        all_skipped.extend(skipped)

    if not saw_marked_batch:
        print("No marked batch files found. Nothing to append.")
        return 0

    if all_appended:
        last_id = max(all_appended + all_skipped)
        next_batch = next_batch_text(last_id)
        target_text = update_next_batch_markers(target_text, next_batch)
        write_text(target_path, target_text)

        if protocol_path.exists():
            protocol_text = read_text(protocol_path)
            protocol_text = update_next_batch_markers(protocol_text, next_batch)
            write_text(protocol_path, protocol_text)

    print(f"Appended: {', '.join(f'{x:03d}' for x in all_appended) or 'none'}")
    print(f"Skipped existing: {', '.join(f'{x:03d}' for x in all_skipped) or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

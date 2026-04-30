#!/usr/bin/env python3
"""Validate Character Shape Research ledgers and batch files.

This script is intentionally report-oriented. It prints errors/warnings but exits 0 by
default so early workflow adoption does not block sampling. Use --strict to return a
non-zero exit code on errors.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
ACCEPTED_LEDGER = ROOT / "research" / "SAMPLED_CHARACTERS.md"
REJECTED_LEDGER = ROOT / "research" / "REJECTED_CHARACTERS.md"
BATCH_DIR = ROOT / "research" / "batches"

START_MARKER = "<!-- ACCEPTED_APPEND_START -->"
END_MARKER = "<!-- ACCEPTED_APPEND_END -->"
HEADING_RE = re.compile(r"^##\s+(\d{3})\s+—\s+(.+?)\s*$", re.MULTILINE)
BATCH_NAME_RE = re.compile(r"BATCH_(\d{3})_(\d{3})\.md$")
STATUS_RE = re.compile(r"^-\s+(\d{3})\s+—\s+(.+?):\s+(.+)$", re.MULTILINE)


@dataclass(frozen=True)
class SampleRef:
    sample_id: int
    name: str
    location: str
    status: str


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def headings(text: str, location: str, status: str) -> list[SampleRef]:
    refs: list[SampleRef] = []
    for match in HEADING_RE.finditer(text):
        refs.append(SampleRef(int(match.group(1)), match.group(2).strip(), location, status))
    return refs


def marked_block(text: str, path: Path, errors: list[str]) -> str:
    has_start = START_MARKER in text
    has_end = END_MARKER in text
    if has_start != has_end:
        errors.append(f"{path}: has only one accepted append marker")
        return ""
    if not has_start:
        return ""
    start = text.index(START_MARKER) + len(START_MARKER)
    end = text.index(END_MARKER)
    if end <= start:
        errors.append(f"{path}: append marker order is invalid")
        return ""
    return text[start:end]


def batch_files() -> list[Path]:
    if not BATCH_DIR.exists():
        return []
    return sorted(BATCH_DIR.glob("BATCH_*.md"))


def parse_status_lines(text: str) -> list[tuple[int, str, str]]:
    out: list[tuple[int, str, str]] = []
    for match in STATUS_RE.finditer(text):
        out.append((int(match.group(1)), match.group(2).strip(), match.group(3).strip()))
    return out


def collect_samples(errors: list[str], warnings: list[str]) -> tuple[list[SampleRef], list[SampleRef], list[SampleRef]]:
    accepted = headings(read_text(ACCEPTED_LEDGER), str(ACCEPTED_LEDGER.relative_to(ROOT)), "accepted")
    rejected = headings(read_text(REJECTED_LEDGER), str(REJECTED_LEDGER.relative_to(ROOT)), "rejected")
    pending: list[SampleRef] = []

    for path in batch_files():
        text = read_text(path)
        rel = str(path.relative_to(ROOT))
        name_match = BATCH_NAME_RE.search(path.name)
        if not name_match:
            errors.append(f"{rel}: batch file name does not match BATCH_###_###.md")
            continue
        expected_start = int(name_match.group(1))
        expected_end = int(name_match.group(2))

        status_lines = parse_status_lines(text)
        if status_lines:
            ids = [sid for sid, _name, _status in status_lines]
            for sid in ids:
                if sid < expected_start or sid > expected_end:
                    errors.append(f"{rel}: status sample {sid:03d} is outside batch range {expected_start:03d}-{expected_end:03d}")
        else:
            warnings.append(f"{rel}: no status lines found")

        block = marked_block(text, path, errors)
        if block:
            for ref in headings(block, rel, "pending"):
                if ref.sample_id < expected_start or ref.sample_id > expected_end:
                    errors.append(f"{rel}: accepted sample {ref.sample_id:03d} is outside batch range {expected_start:03d}-{expected_end:03d}")
                pending.append(ref)

    return accepted, rejected, pending


def duplicate_report(refs: Iterable[SampleRef], errors: list[str]) -> None:
    by_id: dict[int, list[SampleRef]] = {}
    for ref in refs:
        by_id.setdefault(ref.sample_id, []).append(ref)
    for sid, items in sorted(by_id.items()):
        accepted_or_rejected = [x for x in items if x.status in {"accepted", "rejected"}]
        # Pending duplicates are allowed if the accepted entry has already been appended;
        # the append script itself skips duplicates. Accepted+rejected duplicates are not okay.
        statuses = {x.status for x in accepted_or_rejected}
        if len(accepted_or_rejected) > 1 and len(statuses) > 1:
            locs = ", ".join(f"{x.status}@{x.location}" for x in accepted_or_rejected)
            errors.append(f"sample {sid:03d} appears as multiple final statuses: {locs}")
        if len([x for x in accepted_or_rejected if x.status == "accepted"]) > 1:
            locs = ", ".join(x.location for x in accepted_or_rejected if x.status == "accepted")
            errors.append(f"sample {sid:03d} appears multiple times in accepted ledgers: {locs}")
        if len([x for x in accepted_or_rejected if x.status == "rejected"]) > 1:
            locs = ", ".join(x.location for x in accepted_or_rejected if x.status == "rejected")
            errors.append(f"sample {sid:03d} appears multiple times in rejected ledgers: {locs}")


def sequence_report(final_refs: list[SampleRef], errors: list[str], warnings: list[str]) -> None:
    if not final_refs:
        warnings.append("no accepted/rejected final samples found")
        return
    ids = sorted({ref.sample_id for ref in final_refs})
    expected = list(range(ids[0], ids[-1] + 1))
    missing = [sid for sid in expected if sid not in ids]
    if missing:
        warnings.append("missing final sample IDs: " + ", ".join(f"{sid:03d}" for sid in missing))


def batch_status_report(accepted: list[SampleRef], rejected: list[SampleRef], pending: list[SampleRef], errors: list[str], warnings: list[str]) -> None:
    accepted_ids = {ref.sample_id for ref in accepted}
    rejected_ids = {ref.sample_id for ref in rejected}
    pending_ids = {ref.sample_id for ref in pending}

    for path in batch_files():
        text = read_text(path)
        rel = str(path.relative_to(ROOT))
        for sid, _name, status_text in parse_status_lines(text):
            lowered = status_text.lower()
            if "rejected" in lowered and sid not in rejected_ids:
                errors.append(f"{rel}: status says {sid:03d} rejected, but it is not in REJECTED_CHARACTERS.md")
            if "accepted" in lowered:
                if sid not in accepted_ids and sid not in pending_ids:
                    errors.append(f"{rel}: status says {sid:03d} accepted, but it is neither in SAMPLED_CHARACTERS.md nor append markers")
                if "pending" in lowered and sid in accepted_ids:
                    warnings.append(f"{rel}: {sid:03d} says pending auto-merge but already exists in SAMPLED_CHARACTERS.md")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="exit non-zero if errors are found")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    accepted, rejected, pending = collect_samples(errors, warnings)
    duplicate_report([*accepted, *rejected, *pending], errors)
    sequence_report([*accepted, *rejected], errors, warnings)
    batch_status_report(accepted, rejected, pending, errors, warnings)

    print("Research validation report")
    print(f"Accepted final samples: {len(accepted)}")
    print(f"Rejected final samples: {len(rejected)}")
    print(f"Pending accepted batch entries: {len(pending)}")

    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"- WARNING: {item}")
    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"- ERROR: {item}")

    if not warnings and not errors:
        print("No warnings or errors found.")

    return 1 if args.strict and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path

REQUIRED_FILES = [
    "LICENSE_CORE",
    "LICENSE_CLIENTS",
    "CONTENT_LICENSE.md",
    "AUTHORS.md",
    "THIRD_PARTY_NOTICES.md",
]

CODE_EXTENSIONS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".go", ".rs", ".java", ".kt",
    ".cs", ".cpp", ".c", ".h", ".hpp", ".swift", ".php", ".rb", ".sh",
    ".ps1", ".lua", ".json", ".yml", ".yaml", ".toml",
}

MEDIA_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg",
    ".mp3", ".wav", ".flac", ".ogg", ".mp4", ".mov", ".webm",
}

DEPENDENCY_MARKERS = {"package.json", "pyproject.toml", "requirements.txt"}


def find_files(root: Path, names: set[str]) -> list[Path]:
    found: list[Path] = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name in names:
                found.append(Path(dirpath) / name)
    return found


def scan_for_extensions(root: Path, exts: set[str]) -> list[Path]:
    hits: list[Path] = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if Path(name).suffix.lower() in exts:
                hits.append(Path(dirpath) / name)
    return hits


def report_missing_files(root: Path) -> list[str]:
    missing = [name for name in REQUIRED_FILES if not (root / name).exists()]
    return missing


def scan_layer_mismatches(root: Path) -> dict[str, list[Path]]:
    issues: dict[str, list[Path]] = {"media_in_core": [], "code_in_content": []}
    core_dir = root / "core"
    content_dir = root / "content"

    if core_dir.exists():
        issues["media_in_core"] = scan_for_extensions(core_dir, MEDIA_EXTENSIONS)
    if content_dir.exists():
        issues["code_in_content"] = scan_for_extensions(content_dir, CODE_EXTENSIONS)
    return issues


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    print(f"license-audit: {root}")

    missing = report_missing_files(root)
    if missing:
        print("\nMissing required files:")
        for name in missing:
            print(f"- {name}")
    else:
        print("\nRequired files: OK")

    deps = find_files(root, DEPENDENCY_MARKERS)
    print("\nDependency manifests found:")
    if deps:
        for path in sorted(deps):
            print(f"- {path.relative_to(root)}")
        print("  -> Review THIRD_PARTY_NOTICES.md for new entries.")
    else:
        print("- (none)")

    issues = scan_layer_mismatches(root)
    if issues["media_in_core"]:
        print("\nPotential media in core/:")
        for path in issues["media_in_core"]:
            print(f"- {path.relative_to(root)}")
    if issues["code_in_content"]:
        print("\nPotential code in content/:")
        for path in issues["code_in_content"]:
            print(f"- {path.relative_to(root)}")

    if not any(issues.values()):
        print("\nLayer separation check: OK")

    return 0


if __name__ == "__main__":
    sys.exit(main())

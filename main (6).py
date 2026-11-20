"""Entry program for the make.fun news-image-20261120 bounty.

The picture itself sits next to this file (entry.png, or the name a
phone download gave it). Running the
program places a byte-for-byte copy of that picture at the output
location the judges read, /output/entry.png. Nothing is downloaded
and nothing is random: every run produces exactly the same bytes,
and the copy is checked against the original with SHA-256 before
the program reports success.

Usage:
    python3 main.py [destination]

The optional destination argument only exists so the copy step can
be tested without touching /output; the judges run it with no
arguments.
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TARGET = Path("/output/entry.png")

# The picture may sit in the repo under any of these names: the
# canonical entry.png, or the name a phone browser gave the download
# before it was uploaded (image.png, image (1).png). The content is
# the same file either way; the first name that exists wins.
SOURCE_NAMES = ("entry.png", "image (1).png", "image.png")


def find_source() -> Path:
    """Return the first entry-image name that exists next to this file."""
    for name in SOURCE_NAMES:
        candidate = HERE / name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        f"entry image missing: none of {SOURCE_NAMES} found in {HERE}"
    )


def place_entry(target: Path) -> Path:
    """Copy the entry image to *target*, creating parent folders if needed."""
    source = find_source()
    with source.open("rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"entry image is not a PNG: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    return target


def digest(path: Path) -> str:
    """SHA-256 of a file, read in chunks so big files stay cheap."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv: list[str]) -> int:
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    written = place_entry(target)
    if digest(written) != digest(find_source()):
        raise RuntimeError("copy does not match the entry image")
    print(f"wrote {written} ({written.stat().st_size} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

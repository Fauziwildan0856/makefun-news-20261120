#!/usr/bin/env python3
"""Entry program for the make.fun bounty "Sum up 20 November's world news
in one image" (news-image-20261120).

The picture itself is finished artwork stored next to this file. Running
the program publishes that picture, unchanged, to /output/entry.png --
the one path the bounty rules ask for.

Before anything is published, the source picture is checked against the
SHA-256 fingerprint recorded below. If the bytes on disk are not the
bytes that were entered, the program stops with an error instead of
publishing the wrong picture.

The picture may sit in the repository under any of the names listed in
SOURCE_NAMES. The first name that exists wins; the fingerprint check
makes the choice safe, because a wrong file cannot match it.
"""

import hashlib
import os
import sys

# SHA-256 of the entered picture: "THE WORLD TODAY -- Friday
# 20 November 2026", 56 stories on one 1024x1024 page.
EXPECTED_SHA256 = "a88b58ca7e6754875a89ced34c1a8782ec9e11262f71b89faf8730dc98f02734"

# Names the picture is allowed to carry in the repository, in the order
# they are tried. The first one was the name the rules suggest; the
# others are names a phone upload actually produced.
SOURCE_NAMES = ("entry.png", "image (1).png", "image.png")

OUTPUT_PATH = os.path.join("/output", "entry.png")


def sha256_of(path):
    """Return the SHA-256 hex digest of the file at *path*."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_source(directory):
    """Return the path of the entered picture inside *directory*.

    Every candidate name is tried in order. The first one that exists
    and matches the recorded fingerprint is returned; a candidate that
    exists but does not match is skipped with a warning, because the
    next name may still be the right file. Raises FileNotFoundError
    when no candidate matches.
    """
    for name in SOURCE_NAMES:
        candidate = os.path.join(directory, name)
        if not os.path.isfile(candidate):
            continue
        if sha256_of(candidate) == EXPECTED_SHA256:
            return candidate
        print("warning: %s exists but is not the entered picture" % name,
              file=sys.stderr)
    raise FileNotFoundError(
        "no file matching the entered picture was found in %s" % directory)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = find_source(here)

    with open(source, "rb") as handle:
        picture = handle.read()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(picture)

    # Read the published file back and check it once more. A short or
    # corrupted write must fail loudly here, not at judging time.
    if sha256_of(OUTPUT_PATH) != EXPECTED_SHA256:
        raise IOError("the published file does not match the entered picture")

    print("published %s (%d bytes) to %s"
          % (os.path.basename(source), len(picture), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())

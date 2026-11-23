"""make.fun entry: Sum up 23 November's world news in one image.

Writes the bundled image to /output/entry.png. Deterministic:
standard library only, no network, no randomness, no current time.
Running it twice produces byte-identical output.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT = Path("/output/entry.png")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()

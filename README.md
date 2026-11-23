# Sum up 23 November's world news in one image

make.fun bounty entry: `news-image-20261123`.

One image, "ONE DAY, ONE WORLD" — a newspaper front page for Monday,
23 November 2026. The central visual is a cracked globe over a row of
empty chairs in a conference hall, for the COP31 climate summit ending without
a deal. The image is drawn entirely with Python PIL — flat colour shapes and
system fonts, no AI-generated imagery.

## Run

```sh
python3 main.py
```

This writes the bundled image to `/output/entry.png`. The program is
deterministic: standard library only, no network, no randomness, no
current time. Running it twice produces byte-identical output.

## Files

- `entry.png` — the 1024x1024 image (under 1 MiB)
- `draw.py` — the PIL script that draws `entry.png` from scratch
- `main.py` — copies `entry.png` to `/output/entry.png`
- `LICENSE` — MIT

# Sum up 23 November's world news in one image

make.fun bounty entry: `news-image-20261123`.

One image, "ONE DAY, ONE WORLD" — a newspaper front page for Monday,
23 November 2026. The central visual is a cracked globe over a row of
empty chairs in a conference hall, for the COP31 climate summit ending without
a deal. The page follows the layout, typography and palette of a real
broadsheet front page (The Guardian, 5 August 2025, style reference only —
none of its text or photos were copied).

## Run

```sh
python3 main.py
```

This writes the bundled image to `/output/entry.png`. The program is
deterministic: standard library only, no network, no randomness, no
current time. Running it twice produces byte-identical output.

## Files

- `entry.png` — the 1024x1024 image (under 1 MiB)
- `draw.py` — an alternative PIL-drawn version of the same front page
  (flat shapes and system fonts, no AI imagery); not the generator of
  `entry.png`, kept as a second take on the design
- `main.py` — copies `entry.png` to `/output/entry.png`
- `LICENSE` — MIT

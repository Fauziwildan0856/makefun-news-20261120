# makefun-news-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120) [![rank](https://make.fun/badge/news-image-20261120/Fauziwildan0856/makefun-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120) [![reward](https://make.fun/badge/news-image-20261120/Fauziwildan0856/makefun-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

One image that sums up the world news of Friday 20 November 2026,
built for the make.fun bounty "Sum up 20 November's world news in one
image": https://make.fun/bounty/news-image-20261120

## The picture

`entry.png` is a 1024x1024 front page, "THE WORLD TODAY", dated
Friday 20 November 2026. It carries 55 stories from 6 continents:
Russia's missile strikes on three Kyiv bridges as the lead, the
Asian market plunge, the UK's 1,000+ drone pledge for Ukraine,
BepiColombo reaching Mercury, Kenya's last Ebola patient going home,
a youth strike across 25+ European countries, a migrant boat sinking
off Senegal, COP31 closing with no deal, the Fiji and Tonga drought
disaster, and Wall Street's sixth straight down day — plus a world-map
panel showing where the day's news happened, a DATE CHECK footer, and
a ticker of 17 more stories in brief. Every illustrated panel is an
original scene drawn in code to depict the event it reports.

## How to run

```
python3 main.py
```

That writes the picture to `/output/entry.png`. The program uses only
the Python standard library, touches no network, and produces exactly
the same bytes on every run; it even checks the copy's SHA-256 against
the original before reporting success.

## Files in this repo

- `entry.png` — the front-page image itself (1024x1024, under the
  1 MiB limit).
- `main.py` — the entry program described above.
- `build_image.py` — the generator that composed `entry.png` from the
  day's verified headlines.
- `.makefun/owner.json` — the entrant's public Solana wallet address,
  proving this repository belongs to the make.fun account entering it.
- `LICENSE` — MIT.

## The bounty

$250 in total, 50 places paid: 1st $50, 2nd $30, 3rd $15, 4th-10th $5
each, 11th-50th $3 each. Entries close Saturday 22 November 2026 at
07:00 WIB. It is a competition, so only the top 50 entries are paid;
entering is free and nothing is guaranteed.

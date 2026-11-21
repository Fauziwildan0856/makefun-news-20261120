# THE WORLD TODAY — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120) [![rank](https://make.fun/badge/news-image-20261120/Fauziwildan0856/makefun-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120) [![reward](https://make.fun/badge/news-image-20261120/Fauziwildan0856/makefun-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

This repository holds one entry for the make.fun bounty
"Sum up 20 November's world news in one image":
https://make.fun/bounty/news-image-20261120

## The picture

One 1024x1024 front page carrying 56 stories from Friday
20 November 2026, every one of them numbered:

- 11 illustrated panels up top. The lead shows the missile strike on
  three Kyiv bridges; beside it, a full panel follows Cyclone Akvan
  making landfall in Odisha, with 300,000 people evacuated.
- A big-number stat bar under the panels: 300,000+ evacuated, 84 cruise
  missiles at Kyiv, the Nikkei down 4.8%, a GBP 260m drone pledge for
  Ukraine, a $120bn COP31 finance cut, and a youth climate strike
  across 25+ countries.
- A continent bar (Asia 11, Europe 8, Americas 18, Africa 5, Middle
  East 4, Oceania 2, Global 8), a numbered world map whose pins match
  the story numbers, an "ALSO ON" list running to story 38, and a
  one-line ticker that carries the count to 56.
- A DATE CHECK footer naming the neighbouring days' stories that were
  deliberately left out, so nothing from 19 or 21 November sneaks in.

## Running it

```
python3 main.py
```

That is the whole interface. The program writes the picture to
`/output/entry.png`, uses only the Python standard library, touches no
network, and produces the same bytes on every run. Before publishing,
it checks the source picture against its recorded SHA-256 fingerprint
and refuses to publish anything else; after publishing, it reads the
output back and checks it again.

In this repository the picture travels under the name `image (1).png`,
the name the phone upload gave it. `main.py` also accepts `entry.png`
and `image.png`; the fingerprint check, not the name, decides which
file is the entered picture.

## Files

- `main.py` — the entry program described above.
- `image (1).png` — the finished front page, 1024x1024, 243,088 bytes.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the public wallet of the entering account.

## Ownership

The entry belongs to the make.fun account **@fitri-yang**. The file
`.makefun/owner.json` names that account's public wallet, which is how
make.fun can tell this repository belongs to the account entering it.

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/vedreal/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/vedreal/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

# 27 November 2026 — The World in One Day

One image summing up the world news of **Friday, 27 November 2026**, drawn
entirely with PIL so every word renders exactly. A navy date banner names
the day; four cards cover the day's most consequential stories across
regions and fields.

## The four stories

1. **New Zealand — hung parliament.** The official final count of the
   7 November general election, published Friday 27 November, left the
   ruling centre-right bloc on 65 of 130 seats — one short of a majority —
   with the new centrist Opportunity Party (7 seats) holding the balance
   of power. Sources: Reuters, AP, Elections NZ.
2. **Thanksgiving storm — US East Coast.** A powerful storm battered the
   eastern United States over Thanksgiving, cutting power to 900,000+
   customers and cancelling 400+ flights. Sources: Reuters, ANI/CNN,
   PowerOutage.us.
3. **EU budget talks stall.** EU leaders failed to agree the 2028–2034
   budget; 24 member states backed a proposed €45 billion loan for
   Ukraine, to be revisited in December. Source: European Council
   President António Costa's remarks, 27 November 2026.
4. **Trump: Putin wants a deal.** US President Donald Trump said Russian
   President Vladimir Putin "would like to make a deal" to end the war in
   Ukraine. Source: ANI, 27 November 2026.

Stories deliberately left out: North Korea's nuclear expansion and the
Cairo fuel-tanker fire were both first reported on 25–26 November, not
27 November, so they do not belong in a picture of this day.

## Run it

```sh
python3 main.py
```

`main.py` (Python standard library only) copies `entry.png` to
`/output/entry.png`. The image is 1024×1024 PNG, under 1 MiB, and the
program is deterministic — every run writes the same bytes.

`make_image.py` is the PIL script that draws `entry.png` from scratch.

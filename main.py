#!/usr/bin/env python3
"""Entry for make.fun competition the-plan-make-fun-will-carry-20261122-2138.

Writes a 30-day plan (turn $100 into the most money) to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

PLAN = (
    "Sell AI listing-SEO + photo refresh to Etsy sellers at $49/shop: "
    "find 200 shops with weak photos on Etsy, message 20/day offering one free "
    "listing, deliver in 24h with GPT-4o + background removal; "
    "spend $100 on API credits, domain + Gumroad page. "
    "10 sales in 30 days = $490."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)
    print(f"chars: {len(PLAN)}")


if __name__ == "__main__":
    main()

Sample market maker bot
===

Strategy
---

The bot layers bids and offers around the market mid, which it attempts to calculate from the order book. The spread between quoted bids and offers is determined by a user-set risk charge on volatility. Volatility is estimated by an EWMA (Exponentially Weighted Moving Average Process) with frequency and parameters that may also be set by the user.

Set up
---

This bot requires python3 and the [Deribit api wrapper](https://pypi.org/project/deribit_api/).

To set up the bot, edit the `KEY` and `SECRET` variables in the code to your credentials. You can obtain those from the [Deribit account](https://www.deribit.com/main#/account?scrollTo=api).

To start the bot, run `python3 market_maker.py`.

Disclaimer
---

Different market conditions will produce different results. This code is for sample purposes only. It comes as is, with no warranty or guarantee of performance.

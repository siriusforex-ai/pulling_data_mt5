# Pulling Forex Market Data — Python × MetaTrader 5

Pull live forex candlestick data from MetaTrader 5 into Python, convert it into a clean Pandas DataFrame, and save it to CSV for backtesting and analysis.

---

## What This Script Does

- Connects to your MT5 broker account from Python
- Pulls historical OHLCV candlestick data (Open, High, Low, Close, Volume)
- Works with any symbol — GOLD, XAUUSD, EURUSD, BTCUSD, whatever your broker offers
- Works with any timeframe — 1 minute to monthly
- Two ways to pull data: last N candles or specific date range
- Converts raw data into a clean Pandas DataFrame
- Saves everything to a CSV file for offline use

---

## Requirements

- **Windows** (MT5 is Windows only — use VPS or VM if on Mac/Linux)
- **Python 3.8+**
- **MetaTrader 5** installed and running
- A broker account (demo works fine)

---

## Setup

1. Clone this repo

```
git clone https://github.com/siriusforex-ai/pulling_data_mt5.git
cd pulling_data_mt5
```

2. Install the libraries

```
pip install MetaTrader5 pandas
```

3. Open `market_data.py` and replace these with your broker details

```python
account  = 0000000000          # your MT5 account number
password = "your_password"     # your MT5 trading password
server   = "YourBroker-Server" # e.g. XMGlobal-MT5 6, ICMarkets-Live
```

4. Change the symbol if needed

```python
symbol = "GOLD"  # or XAUUSD, EURUSD, BTCUSD, etc.
```

5. Make sure MetaTrader 5 is open and logged in

6. Run the script

```
python market_data.py
```

---

## Two Ways to Pull Data

### Method 1: Last N Candles (default)

Grabs the most recent candles going backwards. Active by default in the script.

```python
timeframe = mt5.TIMEFRAME_M5
num_candles = 100

rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_candles)
```

### Method 2: Date Range

Grabs all candles between two dates. Commented out by default — uncomment Step 3B and comment out Step 3 to use.

```python
from_date = datetime(2026, 3, 1)
to_date = datetime(2026, 4, 8)

rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_H1, from_date, to_date)
```

---

## Available Timeframes

| Code | Timeframe |
|---|---|
| `mt5.TIMEFRAME_M1` | 1 minute |
| `mt5.TIMEFRAME_M5` | 5 minutes |
| `mt5.TIMEFRAME_M15` | 15 minutes |
| `mt5.TIMEFRAME_M30` | 30 minutes |
| `mt5.TIMEFRAME_H1` | 1 hour |
| `mt5.TIMEFRAME_H4` | 4 hours |
| `mt5.TIMEFRAME_D1` | Daily |
| `mt5.TIMEFRAME_W1` | Weekly |
| `mt5.TIMEFRAME_MN1` | Monthly |

---

## Symbol Names

Different brokers use different names for the same instrument:

| Instrument | XM | IC Markets | Exness |
|---|---|---|---|
| Gold | GOLD | XAUUSD | XAUUSDm |
| Euro/USD | EURUSD | EURUSD | EURUSDm |
| Bitcoin/USD | BTCUSD | BTCUSD | BTCUSDm |

Check your MT5 **Market Watch** to find the correct symbol name.

---

## Output

The script outputs a clean OHLCV DataFrame:

```
                  time     open     high      low    close  volume
0  2026-04-07 23:50:00  4712.13  4712.13  4707.74  4708.62     930
1  2026-04-07 23:55:00  4708.42  4713.64  4704.89  4705.48     863
2  2026-04-08 01:00:00  4719.90  4747.67  4719.90  4744.34    1755
3  2026-04-08 01:05:00  4744.44  4751.93  4741.85  4744.36    1432
4  2026-04-08 01:10:00  4744.50  4744.70  4731.11  4731.87    1545
```

And saves it to a CSV file in your project folder.

---

## Common Errors

| Error | Fix |
|---|---|
| `Failed to initialize MT5` | Make sure MT5 is open and running |
| `Login failed` | Double check account number, password, and server name |
| `No IPC connection` | Close MT5, reopen it, login manually, then run script |
| `Failed to get data` | Check symbol name in your MT5 Market Watch |

---

## Links

- 💬 **Telegram:** [Join the channel](https://t.me/+Vib2LlvgE5llNjM1)
- 🐙 **GitHub:** [siriusforex-ai](https://github.com/siriusforex-ai)

---

وَمَن يَتَوَكَّلْ عَلَى اللَّهِ فَهُوَ حَسْبُهُ — [٦٥:٣]

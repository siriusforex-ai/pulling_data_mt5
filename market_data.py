import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import sys
import time

# ─────────────────────────────────────────
#  STEP 1 -- Initialize & Login
# ─────────────────────────────────────────
if not mt5.initialize():
    print(f"Failed to initialize MT5. Error: {mt5.last_error()}")
    mt5.shutdown()
    sys.exit()

print("✅ MT5 initialized successfully")

account  = 1301110952
password = "your_password"
server   = "XMGlobal-MT5 6"

if not mt5.login(account, password=password, server=server):
    print(f"Login failed. Error: {mt5.last_error()}")
    mt5.shutdown()
    sys.exit()

print("✅ Connected successfully!")

# ─────────────────────────────────────────
#  STEP 2 -- Select Symbol
# ─────────────────────────────────────────
symbol = "GOLD"

mt5.symbol_select(symbol, True)
time.sleep(1)

# ─────────────────────────────────────────
#  STEP 3 -- Pull Data (Method 1: Last N candles)
# ─────────────────────────────────────────
timeframe = mt5.TIMEFRAME_M5
num_candles = 100

rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_candles)

if rates is None or len(rates) == 0:
    print(f"Failed to get data. Error: {mt5.last_error()}")
    mt5.shutdown()
    sys.exit()

print(f"✅ Got {len(rates)} candles")

df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')
df = df.rename(columns={'tick_volume': 'volume'})
df = df[['time', 'open', 'high', 'low', 'close', 'volume']]
print(df.to_string())

# # ─────────────────────────────────────────
# #  STEP 3B -- Pull Data (Method 2: Date range)
# # ─────────────────────────────────────────
# from_date = datetime(2026, 3, 1)
# to_date = datetime(2026, 4, 8)
#
# rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_H1, from_date, to_date)
#
# if rates is None or len(rates) == 0:
#     print(f"No data for this range. Error: {mt5.last_error()}")
# else:
#     df = pd.DataFrame(rates)
#     df['time'] = pd.to_datetime(df['time'], unit='s')
#     df = df.rename(columns={'tick_volume': 'volume'})
#     df = df[['time', 'open', 'high', 'low', 'close', 'volume']]
#     print(f"✅ Got {len(df)} candles from {from_date.date()} to {to_date.date()}")
#     print(df.head().to_string())
#     print("...")
#     print(df.tail().to_string())

# ─────────────────────────────────────────
#  STEP 4 -- Save to CSV
# ─────────────────────────────────────────
filename = f"{symbol}_H1_data.csv"
df.to_csv(filename, index=False)
print(f"✅ Data saved to {filename}")

# ─────────────────────────────────────────
#  STEP 5 -- Shutdown
# ─────────────────────────────────────────
mt5.shutdown()
print("✅ MT5 connection closed")

# coding=utf-8
import datetime

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from overhead.toolboxoh import import_file, draw_1d, timestamp_convert


def candle_normalize(low, high, close):
    return (float(close)-float(low)) / (float(high)-float(low))


bitcoin_data = import_file("../Binance/Binance_BTCUSDT_d.csv").split("\n")
keys = bitcoin_data[1].split(",")
lenght = len(bitcoin_data[3:])
bitcoin_dict = {i: dict(zip(keys, bitcoin_data[i + 2].split(","))) for i in range(len(bitcoin_data) - 3)}

candles_normalized = {i: candle_normalize(bitcoin_dict[i]['low'], bitcoin_dict[i]['high'], bitcoin_dict[i]['close']) for i in bitcoin_dict}
print("Candles normalized:", len(candles_normalized))

# import best time series analysis package for easy data analysis ex. sma, ema, etc.

style.use('ggplot')

# convert unix timestamp to datetime
bitcoin_dict = {i: {k: timestamp_convert(float(v)) if k == 'time' else v for k, v in bitcoin_dict[i].items()} for i in bitcoin_dict}
print("Bitcoin dict:", len(bitcoin_dict))
print(bitcoin_dict)
# convert dict to pandas dataframe
bitcoin_df = pd.DataFrame().T
print("Bitcoin df:", len(bitcoin_df))

# convert columns to float
datestring = f'{bitcoin_dict[0]["date"]}'
# print(bitcoin_df)
bitcoin_df = bitcoin_df.astype(bitcoin_dict[0]['date'])

print("Bitcoin df:", len(bitcoin_df))
f'{bitcoin_dict[0]["date"]}'
bitcoin_df['date'] = pd.to_datetime(str(bitcoin_dict[0]['date']).split("\n"), unit='ms')
print("Bitcoin df:", len(bitcoin_df))

# set index to open_time
bitcoin_df.set_index('date', inplace=True)
print("Bitcoin df:", len(bitcoin_df))


bitcoin_df['candle_normalized'].plot()
plt.show()

# plot
bitcoin_df['volume'].plot()
plt.show()

# plot
bitcoin_df['quote_asset_volume'].plot()
plt.show()

# plot
bitcoin_df['number_of_trades'].plot()
plt.show()

# plot
bitcoin_df['open'].plot()
plt.show()

# plot
bitcoin_df['high'].plot()
plt.show()

# plot
bitcoin_df['low'].plot()
plt.show()

# plot
bitcoin_df['close'].plot()
plt.show()


# merge dataframes
bitcoin_df = bitcoin_df.merge(candles_normalized_df, left_index=True, right_index=True)
print("Bitcoin df:", len(bitcoin_df))

# create new columns
bitcoin_df['100ma'] = bitcoin_df['close'].rolling(window=100, min_periods=0).mean()
bitcoin_df['200ma'] = bitcoin_df['close'].rolling(window=200, min_periods=0).mean()
bitcoin_df['50ma'] = bitcoin_df['close'].rolling(window=50, min_periods=0).mean()
bitcoin_df['20ma'] = bitcoin_df['close'].rolling(window=20, min_periods=0).mean()
bitcoin_df['10ma'] = bitcoin_df['close'].rolling(window=10, min_periods=0).mean()
bitcoin_df['5ma'] = bitcoin_df['close'].rolling(window=5, min_periods=0).mean()
bitcoin_df['3ma'] = bitcoin_df['close'].rolling(window=3, min_periods=0).mean()
bitcoin_df['2ma'] = bitcoin_df['close'].rolling(window=2, min_periods=0).mean()


# create subplots
fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

# plot data
ax1.plot(bitcoin_df.index, bitcoin_df['close'], label='close')
ax1.plot(bitcoin_df.index, bitcoin_df['100ma'], label='100ma')
ax1.plot(bitcoin_df.index, bitcoin_df['200ma'], label='200ma')
ax2.bar(bitcoin_df.index, bitcoin_df['candle_normalized'])

# set labels
ax1.set_ylabel('Price')
ax2.set_ylabel('Volume')
ax2.set_xlabel('Date')

# set legend
ax1.legend()

# show plot
plt.show()

# save plot
# fig.savefig('bitcoin.png', dpi=fig.dpi)

# save data
# bitcoin_df.to_csv('bitcoin.csv')










# print(candles_normalized)
# exit()
# for k,v in bitcoin_dict.items():
#     print(f'{k}:\n{v}')

# for i in bitcoin_dict.keys():
#     print(i)
#     print(bitcoin_dict[i][>'close'])
# x = [timestamp_convert(float(bitcoin_dict[i]['unix']), get_time=0) for i in bitcoin_dict.keys()]
# x = [bitcoin_dict[i]['date'].split(" ")[0] for i in bitcoin_dict.keys()]
x = [int(i) for i in bitcoin_dict]
y = [float(bitcoin_dict[i]['close']) for i in bitcoin_dict]
y.reverse()

date_raw = [bitcoin_dict[k]['date'].split(" ")[0] for k in bitcoin_dict]
# date = [f'{d.split("-")[2]}/{d.split("-")[1]}/{d.split("-")[0]}' for d in date_raw]
# pprint(date)
# pprint(date_raw)
draw_1d(x,y)
# draw_1d(date_raw,y)
# draw_1d(candles_normalized.keys(), candles_normalized.values())

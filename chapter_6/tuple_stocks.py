import datetime
from collections import namedtuple

def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)


mid_value, date = middle(
    ("FB", 177.46, 178.67, 175.79), datetime.date(2020, 9, 30)
)


stock = "FB", 75.00, 75.03, 74.90
high = stock[2]  # 75.00
current, high = stock[1:3]  # 75.00 75.03


Stock = namedtuple("Stock", ["symbol", "current", "high", "low"])
stock2 = Stock("FB", 177.46, high=178.67, low=175.79)

stock2.high  # 175.79
symbol, current, high, low = stock
current  # 177.46

stock.current = 74.98  # Traceback ... AttributeError: can't set attribute
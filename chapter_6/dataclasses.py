from dataclasses import make_dataclass
from dataclasses import dataclass
from pprint import pprint


Stock = make_dataclass("Stock", "symbol", "current", "high", "low")


class StockRegClass:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low


@dataclass
class StockDecorated:
    name: str
    current: float
    high: float
    low: float


@dataclass
class StockDefaults:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


stock = Stock("FB", 177.46, high=178.67, low=175.79)
stock  # Stock(symbol='FB', current=177.46, high=178.67, low=175.79)
stock.current  # 177.46
stock.current = 178.25
stock  # Stock(symbol='FB', current=178.25, high=178.67, low=175.79)

stock.unexpected_attribute = 'allowed'
stock.unexpected_attribute  # 'allowed'


#  Example 2
stock_reg_class = StockRegClass("FB", 177.46, high=178.67, low=175.79)
stock_reg_class2 = StockRegClass("FB", 177.46, 178.67, 175.79)

stock_reg_class2 == stock_reg_class  # False

stock2 = Stock("FB", 177.46, 178.67, 175.79)
stock == stock2  # True

#  Example 3
StockDefaults('FB')  # StockDefaults(name='FB', current=0.0, high=0.0, low=0.0)
StockDefaults('FB', 177.46, 178.67, 175.79)  # StockDefaults(name='FB', current=177.46, high=178.67, low=175.79)

#  Example 4 - dataclass ordered
stock_ordered1 = StockOrdered("FB", 177.46, high=178.67, low=175.79)
stock_ordered2 = StockOrdered("FB")
stock_ordered3 = StockOrdered("FB", 178.42, high=179.28, low=176.39)

stock_ordered1 < stock_ordered2  # False
stock_ordered1 > stock_ordered2  # True

pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))
# [StockOrdered(name='FB', current=0.0, high=0.0, low=0.0),
# StockOrdered(name='FB', current=177.46, high=178.67, low=175.79),
# StockOrdered(name='FB', current=178.42, high=179.28, low=176.39)]


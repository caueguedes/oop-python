stocks = {
    "GOOG": (1235.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84)
}

stocks["GOOG"]  # (1235.20, 1242.54, 1231.06)
stocks["RIM"]  # Traceback ... KeyError: 'RIM'

stocks.get("RIM")  # None
stocks.get("RIM", "Not Found")  # Not Found

stocks.setdefault("GOOG", "Invalid")  # (1235.20, 1242.54, 1231.06)
stocks.setdefault("BBRY", (10.87, 10.76, 10.90))  # (10.87, 10.76, 10.90)
stocks["BBRY"]  # (10.87, 10.76, 10.90)

for stock, values in stocks.items():
    print(f"{stock} last value is {values[0]}")
# GOOG last value is 1235.2
# MSFT last value is 110.41
# BBRY last value is 10.5

stocks["GOOG"] = (1245.21, 1252.64, 1245.18)
stocks["GOOG"]  # (1245.21, 1252.64, 1245.18)

random_keys = {}
random_keys["a_string"] = "some_string"
random_keys[5] = "an_integer"
random_keys[25.2] = "floats_work_too"
random_keys[("abc", 123)] = "so do tuples"


class AnObject:
    def __init__(self, a_value):
        self.a_value = a_value


my_object = AnObject(14)
random_keys[my_object] = "we can even store objects"
my_object.a_value = 12
try:
    random_keys[[1, 2, 3]] = "we can't store lists thought"
except BaseException:
    print("unable to store list\n")

for key, value in random_keys.items():
    print("{} has value {}".format(key, value))


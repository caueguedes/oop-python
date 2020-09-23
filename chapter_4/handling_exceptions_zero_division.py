def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is not a good idea!"


print(funny_division(0))  # Zero is not a good idea!
print(funny_division(50.0))  # 2.0
print(funny_division("hello"))  # TypeError: unsupported operand type(s) for /: 'int' and 'str'.


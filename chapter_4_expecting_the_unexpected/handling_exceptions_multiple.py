def funny_division2(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
            return 100 / divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


for val in (0, "hello", 50.0, 13):
    print("Testing {}:".format(val), end=" ")  # end concatenate " " after the print
    print(funny_division2(val))


# Testing 0: Enter a number other than zero
# Testing hello: Enter a number other than zero
# Testing 50.0: 2.0
# Testing 13: Traceback (most recent call last): ... ValueError: 13 is an unlucky number


def funny_division3(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13")
        raise

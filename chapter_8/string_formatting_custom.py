import datetime

print("{the_date:%Y-%m-%d %I:%M%p }".format(
    datetime.datetime.now()))

# implement __format__


# format method
template = "abc {number:*^10d} "
template.format(number=32)  # 'abc ****32****'
template.format(number=84)  # 'abc ****84****'

#positional
"{0} world".format("hello")
#indexing
"{} {}".format('hello', "world")

from functools import total_ordering
from operator import itemgetter


@total_ordering
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < other.string

    def __eq__(self, other):
        return all((
            self.string == other.string,
            self.number == other.number,
            self.sort_num == other.sort_num
        ))

    def __repr__(self):
        return f"{self.string}:{self.number}"


l = ["hello", "HELP", "helo"]
l.sort()
l  #   # ['HELP', 'Helo', 'hello']

l.sort(key=str.lower)
l  # ['hello', 'Helo', 'HELP']


l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key=itemgetter(1))
l  # [('p', 1), ('y', 2), ('t', 3), ('h', 4), ('o', 5), ('n', 6)]

# also are attrgetter and methodcaller for dicts and objects




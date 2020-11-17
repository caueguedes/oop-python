class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return f"{self.string}:{self.number}"




a = WeirdSortee("a", 4, True)
b = WeirdSortee("b", 3, True)
c = WeirdSortee("c", 2, True)
d = WeirdSortee("d", 1, True)


weird_list = [a, b, c, d]
print(weird_list)  # [a:4, b:3, c:2, d:1]

weird_list.sort()
print(weird_list)  # [d:1, c:2, b:3, a:4]

for item in weird_list:
    item.sort_num = False

weird_list.sort()
print(weird_list)  # [a:4, b:3, c:2, d:1]

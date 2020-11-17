number = 5


def funky_function(number=number):
    print(number)


number = 6
funky_function(8)  # 8
funky_function()  # 5
print(number)  # 6

# This happen because the default is set when the function is loaded(when the value is 5)


def hello(b=[]):
    b.append('a')
    print(b)


hello()  # ['a']
hello()  # ['a', 'a']
# Way around is => iargument = argument if argument else []

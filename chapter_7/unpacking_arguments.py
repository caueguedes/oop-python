def show_args(arg1, arg2, arg3="Three"):
    print(arg1, arg2, arg3)

some_args = range(3)
more_args = {
    "arg1": "One",
    "arg2": "Two"
}

print("Unpacking a sequence:", end=" ")
show_args(*some_args)  # Unpacking a sequence: 0 1 2

print("Unpacking a dict:", end=" ")
show_args(**more_args)  # Unpacking a dict: One Two Three


x = {'a': 1, 'b': 2}
y = {'b': 11, 'c': 3}
z = {**x, **y}
z  # {'a': 1, 'b': 11, 'c': 3}

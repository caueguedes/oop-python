len([1, 2, 3, 4])  # 4

# why not MyObject.__len__()
# every time a method or attribute is called on an object, it also calls the __getattribute__ method


# all() && any()  accept an iterable object and return true if all or any of the
# values evaluate to True

eval("print('oi')")
exec("print('oi')")
compile()
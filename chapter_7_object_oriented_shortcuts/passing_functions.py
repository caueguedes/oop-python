def my_function():
    print("The function was called")


my_function.description = "A silly function"


def second_function():
    print("The second was called")


second_function.description = "A sillier function"


def another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()


another_function(my_function)
# The description: A silly function
# The name: my_function
# The class: <class 'function'>
# Now I'll call the function passed in
# The Function Was Called

another_function(second_function)
# The description: A sillier function.
# The name: second_function
# The class: <class 'function'>
# Now I'll call the function passed in
# The second was called

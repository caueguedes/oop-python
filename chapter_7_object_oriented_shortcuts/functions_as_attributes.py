class A:
    def print(self):
        print("My class is A")


def fake_print():
    print("my class is not A")


a = A()
a.print()  # My class is A

a.print = fake_print
a.print()  # my class is not A


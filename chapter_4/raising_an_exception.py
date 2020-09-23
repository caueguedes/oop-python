class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


e = EvenOnly()
e.append("a string")  # ... File "even_integers.py", line 7, in add

e.append(3)  # ... File "even_integers.py", line 9, in add

e.append(2)
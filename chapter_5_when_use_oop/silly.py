class Silly:
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("Your are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")

s = Silly()
s.silly = "funny"  # You're making silly funny

s.silly  # You're getting silly 'funny'

del s.silly  # Whoah, you killed silly!

help(Silly)

# Help on class Silly in module __main__:
# class Silly(builtins.object)
# | Data descriptors defined here:
# |
# | __dict__
# |     dictionary for instance variables (if defined)
# |
# | __weakref__
# |     list of weak references to the object (if defined)
# |
# | silly
# |   This is a silly property

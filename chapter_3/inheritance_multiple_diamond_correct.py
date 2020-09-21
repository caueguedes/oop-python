class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class.")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_let_calls = 0

    def call_me(self):
        super().call_me(self)
        print("Calling method on Left Class.")
        self.num_let_call += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me(self)
        print("Calling method on Right Class.")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Sub Class.")
        self.num_sub_calls += 1


s = Subclass()
s.call_me()
# Calling method on Base Class
# Calling method on Right Subclass
# Calling method on Left Subclass
# Calling method on Subclass
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)  # 1 1 1 1

class InvalidWithdrawal(Exception):
    pass


class InvalidPersonalizedWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"account doesn't have $&{amount}")
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


try:
    raise InvalidWithdrawal("You don't have $50 in your account")
except InvalidWithdrawal:
    pass


try:
    raise InvalidPersonalizedWithdrawal(25, 50)
except InvalidPersonalizedWithdrawal as exception:
    print("I'm sorry, but your withdrawal is more than your balance by "
          f"${exception.overage()}")

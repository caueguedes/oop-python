class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)


if __name__ == "__main__":
    inventory = Inventory()
    observer = ConsoleObserver(inventory)
    inventory.attach(observer)

    inventory.product = "Widget"
    # 0
    # Widget

    observer2 = ConsoleObserver(inventory)
    inventory.attach(observer2)

    inventory.quantity = 5
    # 5
    # Widget
    # 5
    # Widget

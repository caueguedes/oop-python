class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


color = Color("#0000ff", "bright red")
print(color.name)  # bright red

color.name = "red"
print(color.name)  # red

color.name = ""  # Traceback ... Exception: Invalid Name
class OneOnly:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton


if __name__ == '__main__':
    only1 = OneOnly()
    only2 = OneOnly()

    only1 == only2  # True
    only1  # <__main__.OneOnly object at 0xb71c008c>
    only2  # <__main__.OneOnly object at 0xb71c008c>

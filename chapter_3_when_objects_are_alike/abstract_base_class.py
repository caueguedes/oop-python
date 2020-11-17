import abc


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @property
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstracmethods__) <= attrs:
                return True

            return NotImplemented


class Wav(MediaLoader):
    pass


x = Wav()  # ... TypeError: Can't instantiate abstract class Wav with abstract methods ext, play


class Ogg(MediaLoader):
    ext = '.ogg'

    def play(self):
        pass

o = Ogg()


issubclass(Ogg, MediaLoader)  # True
isinstance(Ogg(), MediaLoader)  # True
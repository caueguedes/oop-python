import weakref


class CarModel:
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model
        return model

    def __init__(
            self, model_name,
            air=False,
            tilt=False,
            cruise_control=False,
            power_locks=False,
            alloy_wheels=False,
            usb_charges=False,
    ):
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charges
            self.initted = True

    def check_serial(self, serial_number):
        print(
            "Sorry, we are unable to check "
            "the serial number {0} on the {1} "
            "at this time".format(serial_number, self.model_name)
        )


class Car:
    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self):
        return self.model.check_serial(self.serial)


if __name__ == '__main__':
    dx = CarModel("FIT DIX")
    lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
    car1 = Car(dx, "blue", "12345")
    car2 = Car(dx, "black", "12346")
    car3 = Car(lx, "red", "12347")

    id(lx)  # 3071620300
    del lx
    del car3

    import gc
    gc.collect()  # 0

    lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
    id(lx)  # 3071576140

    lx = CarModel("FIT LX")
    id(lx)  # 3071576140
    lx.air  # True

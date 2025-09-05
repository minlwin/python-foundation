# Base class with a common method
class Device:
    def power(self):
        pass  # placeholder (to be overridden)


# Different objects implementing their own version of power()
class TV(Device):
    def power(self):
        print("TV turns on 📺")


class SoundSystem(Device):
    def power(self):
        print("Sound system starts playing 🎶")


class AirConditioner(Device):
    def power(self):
        print("Air conditioner starts cooling ❄️")


# Using polymorphism
devices = [TV(), SoundSystem(), AirConditioner()]

for device in devices:
    device.power()  # Same method call, different behaviors

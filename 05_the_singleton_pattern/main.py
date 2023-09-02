class ChocolateBoiler:
    class __ChocolateBoiler:
        def __init__(self):
            self.empty = True
            self.boiled = False

        def fill(self):
            if self.empty:
                self.empty = False
                self.boiled = False
                print("Filling the boiler with a milk/chocolate mixture")
            else:
                print("The boiler is already filled")

        def drain(self):
            if not self.empty and self.boiled:
                print("Draining the boiled milk and chocolate")
                self.empty = True
            else:
                print("The boiler is empty or not boiled")

        def boil(self):
            if not self.empty and not self.boiled:
                print("Boiling the milk and chocolate")
                self.boiled = True
            else:
                print("The boiler is empty or already boiled")

    instance = None

    def __new__(cls):
        if not ChocolateBoiler.instance:
            ChocolateBoiler.instance = ChocolateBoiler.__ChocolateBoiler()
        return ChocolateBoiler.instance

    def get_instance(self):
        if self.instance is None:
            self.instance = self._ChocolateBoiler()
        return self.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)


def test():
    boiler = ChocolateBoiler()
    boiler2 = ChocolateBoiler()

    boiler.fill()
    boiler2.fill()
    boiler2.boil()

    boiler.boil()
    boiler2.boil()

    boiler.drain()
    boiler2.drain()
    boiler.boil()


if __name__ == "__main__":
    # python3 05_the_singleton_pattern/main.py
    test()

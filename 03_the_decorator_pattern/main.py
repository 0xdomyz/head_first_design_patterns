# python3 ./03_the_decorator_pattern/main.py

# beverages


class Beverage(object):
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    def cost(self):
        pass


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"

    def cost(self):
        return 1.05


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99


# condiment decorators


class CondimentDecorator:  # may not be necessary in Python
    def get_description(self):
        pass


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()


class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Steamed Milk"

    def cost(self):
        return 0.10 + self.beverage.cost()


# test


def make_order():
    Beverage = Espresso()
    print(f"{Beverage.get_description()} ${Beverage.cost()}")

    Beverage2 = DarkRoast()
    Beverage2 = Mocha(Beverage2)
    Beverage2 = Mocha(Beverage2)
    Beverage2 = Whip(Beverage2)
    print(f"{Beverage2.get_description()} ${Beverage2.cost()}")

    Beverage3 = HouseBlend()
    Beverage3 = Soy(Beverage3)
    Beverage3 = Mocha(Beverage3)
    Beverage3 = Whip(Beverage3)
    print(f"{Beverage3.get_description()} ${Beverage3.cost()}")


if __name__ == "__main__":
    make_order()

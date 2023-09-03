from pizza_store_ingredients import *


class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.veggies = self.ingredient_factory.create_veggies()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class PizzaIngredientFactory:
    def create_dough(self):
        pass

    def create_sauce(self):
        pass

    def create_cheese(self):
        pass

    def create_veggies(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        pass


class NYPizzaIngredientFactory:
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory:
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        veggies = [BlackOlives(), Spinach(), Eggplant()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


class PizzaStore:
    def __init__(self):
        self.ingredient_factory = None

    def create_pizza(self, pizza_type):
        raise NotImplementedError

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def __init__(self):
        super().__init__()
        self.ingredient_factory = NYPizzaIngredientFactory()

    def create_pizza(self, pizza_type):
        pizza = None

        if pizza_type == "cheese":
            pizza = CheesePizza(self.ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(self.ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(self.ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(self.ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        return pizza


if __name__ == "__main__":
    # python3 pizza_store.py
    ny_store = NYPizzaStore()
    ny_store.order_pizza("cheese")
    ny_store.order_pizza("veggie")
    ny_store.order_pizza("clam")
    ny_store.order_pizza("pepperoni")

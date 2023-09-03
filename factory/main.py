class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(f"    {topping}")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class PizzaStore:
    def order_pizza(self, pizza_type) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    def create_pizza(self, pizza_type) -> Pizza:
        raise NotImplementedError


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type) -> Pizza:
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        elif pizza_type == "veggie":
            return NYStyleVeggiePizza()
        else:
            raise ValueError("Invalid pizza type: %s" % pizza_type)


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type) -> Pizza:
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        else:
            raise ValueError("Invalid pizza type: %s" % pizza_type)


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")


NYStylePepperoniPizza = NYStyleCheesePizza
NYStyleClamPizza = NYStyleCheesePizza
NYStyleVeggiePizza = NYStyleCheesePizza


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")


ChicagoStylePepperoniPizza = ChicagoStyleCheesePizza
ChicagoStyleClamPizza = ChicagoStyleCheesePizza
ChicagoStyleVeggiePizza = ChicagoStyleCheesePizza


def test():
    ny_store = NYStylePizzaStore()
    chicago_store = ChicagoStylePizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.name}\n")


if __name__ == "__main__":
    # python3 04_the_factory_pattern/main.py
    test()

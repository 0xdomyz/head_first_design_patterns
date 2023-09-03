class CaffineBeverageWithHook:
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        pass

    def pour_in_cup(self):
        print("Pouring into cup")

    def add_condiments(self):
        pass

    def customer_wants_condiments(self):
        return True


class CoffeWithHook(CaffineBeverageWithHook):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

    def customer_wants_condiments(self):
        answer = input("Would you like milk and sugar with your coffee (y/n)? ")
        if answer.lower().startswith("y"):
            return True
        else:
            return False


class TeaWithHook(CaffineBeverageWithHook):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

    def customer_wants_condiments(self):
        answer = input("Would you like lemon with your tea (y/n)? ")
        if answer.lower().startswith("y"):
            return True
        else:
            return False


def test():
    tea = TeaWithHook()
    coffee = CoffeWithHook()

    print("\nMaking tea...")
    tea.prepare_recipe()

    print("\nMaking coffee...")
    coffee.prepare_recipe()


if __name__ == "__main__":
    # python3 caffine_beverage.py
    test()

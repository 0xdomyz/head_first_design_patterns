class MenuItem:
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price


class PancakeHouseMenu:
    def __init__(self):
        self.menu_items = []
        self.add_item(
            "K&B's Pancake Breakfast",
            "Pancakes with scrambled eggs, and toast",
            True,
            2.99,
        )
        self.add_item(
            "Regular Pancake Breakfast",
            "Pancakes with fried eggs, sausage",
            False,
            2.99,
        )
        self.add_item(
            "Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49
        )
        self.add_item(
            "Waffles",
            "Waffles, with your choice of blueberries or strawberries",
            True,
            3.59,
        )

    def add_item(self, name, description, vegetarian, price):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def get_menu_items(self):
        return self.menu_items

    def __iter__(self):
        return iter(self.menu_items)


class DinerMenu:
    def __init__(self):
        self.menu_items = {}
        self.number_of_items = 0
        self.max_items = 6
        self.add_item(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )
        self.add_item("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.add_item(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )
        self.add_item(
            "Hotdog",
            "A hot dog, with saurkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )

    def add_item(self, name, description, vegetarian, price):
        item = MenuItem(name, description, vegetarian, price)
        if self.number_of_items >= self.max_items:
            print("Sorry, menu is full! Can't add item to menu")
        else:
            self.menu_items[self.number_of_items] = item
            self.number_of_items += 1

    def get_menu_items(self):
        return self.menu_items

    def __iter__(self):
        return iter(self.menu_items.values())


class Waitress:
    def __init__(self, pancake_house_menu, diner_menu):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        pancake_iterator = iter(self.pancake_house_menu)
        diner_iterator = iter(self.diner_menu)
        print("MENU\n----\nBREAKFAST")
        self.print_menu_items(pancake_iterator)
        print("\nLUNCH")
        self.print_menu_items(diner_iterator)

    def print_menu_items(self, iterator):
        for item in iterator:
            print(f"{item.name}, {item.price} -- {item.description}")


if __name__ == "__main__":
    # python3 iterate_2_menus.py
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    waitress = Waitress(pancake_house_menu, diner_menu)
    waitress.print_menu()

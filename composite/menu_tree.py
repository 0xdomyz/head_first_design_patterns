class MenuComponent:
    def add(self, menu_component):
        raise NotImplementedError

    def remove(self, menu_component):
        raise NotImplementedError

    def get_child(self, i):
        raise NotImplementedError

    def print(self):
        raise NotImplementedError


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def print(self):
        print(f"  {self.name}", end="")
        if self.vegetarian:
            print("(v)", end="")
        print(f", {self.price}")
        print(f"    -- {self.description}")


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.menu_components = []
        self.name = name
        self.description = description

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, i):
        return self.menu_components[i]

    def print(self):
        print(f"\n{self.name}, {self.description}")
        print("---------------------")
        for menu_component in self.menu_components:
            menu_component.print()


class waitress:
    def __init__(self, all_menus):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print()


if __name__ == "__main__":
    # python3 menu_tree.py
    pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    dinner_menu = Menu("DINNER MENU", "Lunch")
    cafe_menu = Menu("CAFE MENU", "Dinner")
    dessert_menu = Menu("DESSERT MENU", "Dessert of course!")

    all_menus = Menu("ALL MENUS", "All menus combined")

    all_menus.add(pancake_house_menu)
    all_menus.add(dinner_menu)
    all_menus.add(cafe_menu)

    dinner_menu.add(
        MenuItem(
            "Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True,
            3.89,
        )
    )

    dinner_menu.add(dessert_menu)

    dessert_menu.add(
        MenuItem(
            "Apple Pie",
            "Apple pie with a flakey crust, topped with vanilla icecream",
            True,
            1.59,
        )
    )

    cafe_menu.add(
        MenuItem(
            "Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True,
            3.99,
        )
    )

    pancake_house_menu.add(
        MenuItem(
            "K&B's Pancake Breakfast",
            "Pancakes with scrambled eggs, and toast",
            True,
            2.99,
        )
    )

    waitress = waitress(all_menus)
    waitress.print_menu()

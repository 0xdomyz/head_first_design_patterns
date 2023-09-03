class Duck:
    def quack(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")


class Turkey:
    def gobble(self):
        pass

    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


def test():
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    duck.quack()
    duck.fly()

    print("\nThe TurkeyAdapter says...")
    turkey_adapter.quack()
    turkey_adapter.fly()


if __name__ == "__main__":
    # python3 turkey_adapter.py
    test()

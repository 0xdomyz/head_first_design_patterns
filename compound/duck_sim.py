# the main interface
class Quackable:
    def quack(self):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


# the subject interface
class QuackObservable:
    def register_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class Observable(QuackObservable):
    def __init__(self, duck):
        self.observers = []
        self.duck = duck

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.duck)


class Observer:
    def update(self, duck):
        raise NotImplementedError


class Quackologist(Observer):
    def update(self, duck):
        print(f"Quackologist: {duck} just quacked")


# ducks


class MallardDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        print("Quack")
        self.notify_observers()


class RedheadDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        print("Quack")
        self.notify_observers()


class DuckCall(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        print("Kwak")
        self.notify_observers()


class RubberDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        print("Squeak")
        self.notify_observers()


# geese
class Goose:
    def honk(self):
        print("Honk")


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.observable = Observable(self)
        self.goose = goose

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        self.goose.honk()
        self.notify_observers()


# flock


class Flock(Quackable):
    def __init__(self):
        self.quackers = []

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def register_observer(self, observer):
        for quacker in self.quackers:
            quacker.register_observer(observer)

    def notify_observers(self):
        raise NotImplementedError


# decorator


class QuackCounter:
    number_of_quacks = 0

    def __init__(self, duck):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.number_of_quacks += 1

    @staticmethod
    def get_quacks():
        return QuackCounter.number_of_quacks

    def register_observer(self, observer):
        self.duck.register_observer(observer)

    def notify_observers(self):
        self.duck.notify_observers()


# factory
class CountingDuckFactory:
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedheadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())


# simulator


class DuckSimulator:
    def __init__(self, duck_factory=None):
        self.duck_factory = duck_factory

    def simulate(self):
        mallard_duck = duck_factory.create_mallard_duck()
        redhead_duck = duck_factory.create_redhead_duck()
        duck_call = duck_factory.create_duck_call()
        rubber_duck = duck_factory.create_rubber_duck()

        goose = Goose()
        goose_adapter = GooseAdapter(goose)

        flock_of_ducks = Flock()
        flock_of_ducks.add(mallard_duck)
        flock_of_ducks.add(redhead_duck)
        flock_of_ducks.add(duck_call)
        flock_of_ducks.add(rubber_duck)
        flock_of_ducks.add(goose_adapter)

        flock_of_mallards = Flock()
        for _ in range(4):
            flock_of_mallards.add(duck_factory.create_mallard_duck())

        flock_of_ducks.add(flock_of_mallards)

        quackologist = Quackologist()
        flock_of_ducks.register_observer(quackologist)

        print("\nDuck Simulator: With Observer")
        self.simulate_duck(flock_of_ducks)

        print(f"\nThe ducks quacked {QuackCounter.get_quacks()} times")

    def simulate_duck(self, duck):
        duck.quack()


if __name__ == "__main__":
    # python3 duck_sim.py
    duck_factory = CountingDuckFactory()
    simulator = DuckSimulator(duck_factory)
    simulator.simulate()

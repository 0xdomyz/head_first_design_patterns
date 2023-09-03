# run: python3 01_the_strategy_pattern/main.py

# client

class Duck:
    def __init__(self):
        self.fly_behaviour = None
        self.quack_behaviour = None

    def set_fly_behaviour(self, fly_behaviour):# dont need this in python
        self.fly_behaviour = fly_behaviour

    def set_quack_behaviour(self, quack_behaviour):
        self.quack_behaviour = quack_behaviour

    def perform_fly(self):
        self.fly_behaviour.fly()

    def perform_quack(self):
        self.quack_behaviour.quack()

    def swim(self):
        print("All ducks float, even decoys!")

class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.set_fly_behaviour(FlyWithWings())
        self.set_quack_behaviour(Quack())

class RedheadDuck(Duck):
    def __init__(self):
        super().__init__()
        self.set_fly_behaviour(FlyWithWings())
        self.set_quack_behaviour(Quack())

class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.set_fly_behaviour(FlyNoWay())
        self.set_quack_behaviour(Squeak())

class DecoyDuck(Duck):
    def __init__(self):
        super().__init__()
        self.set_fly_behaviour(FlyNoWay())
        self.set_quack_behaviour(MuteQuack())

# encapsulated fly behavioural

class FlyBehaviour:
    def fly(self):
        raise NotImplementedError
    
class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I'm flying!")

class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly")


# encapsulated quack behavioural

class QuackBehaviour:
    def quack(self):
        raise NotImplementedError
    
class Quack(QuackBehaviour):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<< Silence >>")

class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak")

# test

class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.set_fly_behaviour(FlyNoWay())
        self.set_quack_behaviour(Quack())

class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print("I'm flying with a rocket!")

def mini_duck_simulator():
    mallard = MallardDuck()
    print("Mallard Duck")
    mallard.perform_fly()
    mallard.perform_quack()

    model = ModelDuck()
    print("Model Duck")
    model.perform_fly()
    model.set_fly_behaviour(FlyRocketPowered())
    model.perform_fly()

if __name__ == "__main__":
    mini_duck_simulator()

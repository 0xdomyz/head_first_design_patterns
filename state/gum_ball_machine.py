class State:
    def insertQuarter(self):
        raise NotImplementedError

    def ejectQuarter(self):
        raise NotImplementedError

    def turnCrank(self):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError


class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.set_state(self.gumballMachine.has_quarter_state)

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")


import random


class HasQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert another quarter")

    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.set_state(self.gumballMachine.no_quarter_state)

    def turnCrank(self):
        print("You turned...")
        winner = random.randint(0, 9)
        if winner == 0 and self.gumballMachine.count > 1:
            self.gumballMachine.set_state(self.gumballMachine.winner_state)
        else:
            self.gumballMachine.set_state(self.gumballMachine.sold_state)


class GumballSoldState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball")

    def dispense(self):
        self.gumballMachine.release_ball()
        if self.gumballMachine.count > 0:
            self.gumballMachine.set_state(self.gumballMachine.no_quarter_state)
        else:
            print("Oops, out of gumballs!")
            self.gumballMachine.set_state(self.gumballMachine.out_of_gumballs_state)


class OutOfGumballsState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert a quarter, the machine is out of gumballs")

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")


class WinnerState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball")

    def dispense(self):
        print("YOU'RE A WINNER! You get two gumballs for your quarter")
        self.gumballMachine.release_ball()
        if self.gumballMachine.count == 0:
            self.gumballMachine.set_state(self.gumballMachine.out_of_gumballs_state)
        else:
            self.gumballMachine.release_ball()
            if self.gumballMachine.count > 0:
                self.gumballMachine.set_state(self.gumballMachine.no_quarter_state)
            else:
                print("Oops, out of gumballs!")
                self.gumballMachine.set_state(self.gumballMachine.out_of_gumballs_state)


class GumballMachine:
    def __init__(self, numberGumballs):
        self.count = numberGumballs

        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = GumballSoldState(self)
        self.out_of_gumballs_state = OutOfGumballsState(self)
        self.winner_state = WinnerState(self)

        if self.count > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.out_of_gumballs_state

    def insert_quarter(self):
        self.state.insertQuarter()

    def eject_quarter(self):
        self.state.ejectQuarter()

    def turn_crank(self):
        self.state.turnCrank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1

    def __str__(self):
        return "Mighty Gumball\nInventory: {}\n".format(self.count)


if __name__ == "__main__":
    # python3 gum_ball_machine.py
    gumballMachine = GumballMachine(5)

    print(gumballMachine)
    gumballMachine.insert_quarter()
    gumballMachine.turn_crank()
    print("")

    print(gumballMachine)
    gumballMachine.insert_quarter()
    gumballMachine.eject_quarter()
    gumballMachine.turn_crank()
    print("")

    print(gumballMachine)
    gumballMachine.insert_quarter()
    gumballMachine.turn_crank()
    gumballMachine.insert_quarter()
    gumballMachine.turn_crank()
    gumballMachine.eject_quarter()
    print("")

    print(gumballMachine)
    gumballMachine.insert_quarter()
    gumballMachine.insert_quarter()
    gumballMachine.turn_crank()
    gumballMachine.insert_quarter()
    gumballMachine.turn_crank()
    gumballMachine.insert_quarter()
    gumballMachine.turn_crank()
    print("")

# python3 11_the_proxy_pattern/main.py


class Person:
    def __init__(self):
        self.name = None
        self.gender = None
        self.interests = None
        self.rating = 0


class PersonImpl(Person):
    def __init__(self):
        super().__init__()
        self.rating_count = 0

    def get_rating(self):
        if self.rating_count == 0:
            return 0
        return self.rating / self.rating_count

    def set_rating(self, rating):
        self.rating_count += 1
        self.rating += rating


class OwnerInvocationHandler:
    def __init__(self, person):
        self.person = person

    def __getattr__(self, name):
        if name.startswith("get_"):
            return getattr(self.person, name)
        elif name == "set_rating":
            raise AttributeError()
        elif name.startswith("set_"):
            return getattr(self.person, name)
        else:
            raise AttributeError()


if __name__ == "__main__":
    person = PersonImpl()
    person.set_rating(5)
    person.set_rating(4)
    print(person.get_rating())

    person = OwnerInvocationHandler(person)
    person.name = "Joe"
    print(person.name)
    print(person.get_rating())
    try:
        person.set_rating(5)
    except AttributeError:
        print("AttributeError, can't set rating")

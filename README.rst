Head first design patterns
==============================

Summary of patterns by categories
----------------------------------

Creational Patterns
^^^^^^^^^^^^^^^^^^^

Involve object instantiation and all provide a way to decouple a client 
from the objects it needs to instantiate.

- Abstract Factory:

    Provide an interface for creating families of related or dependent objects 
    without specifying their concrete classes.

- Builder (less used):

    Encapsulate the construction of a product and allow it to be constructed in steps.

- Factory:

    Define an interface for creating an object, but let subclasses decide which class 
    to instantiate. Factory Method lets a class defer instantiation to subclasses.

- Prototype (less used):

    When creating an instance of a class is expensive or complicated.

- Singleton:

    Ensure a class only has one instance, and provide a global point of access to it.


Structural Patterns
^^^^^^^^^^^^^^^^^^^

Let you compose classes or objects into larger structures.

- Adapter:

    Convert the interface of a class into another interface clients expect. 
    Adapter lets classes work together that couldn't otherwise because of 
    incompatible interfaces.

- Bridge (less used):

    Vary not only your implementations, but also your abstractions.

- Composite:

    Compose objects into tree structures to represent part-whole hierarchies. 
    Composite lets clients treat individual objects and compositions of objects 
    uniformly.

- Decorator:

    Attach additional responsibilities to an object dynamically. 
    Decorators provide a flexible 
    alternative to subclassing for extending functionality.

- Facade:

    Provide a unified interface to a set of interfaces in a subsystem. 
    Facade defines a higher-level interface that makes the subsystem easier to use.

- Flyweight (less used):

    When one instance of a class can be used to provide many "virtual instances".

- Proxy:

    Provide a surrogate or placeholder for another object to control access to it.

Behavioral Patterns
^^^^^^^^^^^^^^^^^^^

Concerned with how classes and objects interact and distribute responsibility.

- Chain of Responsibility (less used):

    When you want to give more than one object a chance to handle a request.

- Command:

    Encapsulate a request as an object, thereby letting you parameterize clients 
    with different requests, queue or log requests, and support undoable operations.

- Interpreter:

    To build a interpreter for a language.

- Iterator:

    Provide a way to access the elements of an aggregate object sequentially 
    without exposing its underlying representation.

- Mediator (less used):

    To centralize complex communications and control between related objects.

- Memento (less used):

    When you need to be able to return an object to one of its previous states;
    for instance, if your user requests an “undo.”.

- Observer:

    Define a one-to-many dependency between objects so that when one object changes 
    state, all its dependents are notified and updated automatically.

- State:

    Allow an object to alter its behavior when its internal state changes. 
    The object will appear to change its class. It's a technique to manage
    state-dependent behavior.

- Strategy:

    Define a family of algorithms, encapsulate each one, and make them interchangeable.
    Strategy lets the algorithm vary independently from clients that use it.

- Template Method:

    Define the skeleton of an algorithm in an operation, deferring some steps to
    subclasses.
    Template Method lets subclasses redefine certain steps of an algorithm 
    without changing the algorithm's structure.

- Visitor (less used):

    When you want to add capabilities to a composite of objects 
    and encapsulation is not important.

Design principles
-----------------

- Encapsulate what varies.

- Program to an interface, not an implementation.

- Favor composition over inheritance.

- Strive for loosely coupled designs between objects that interact.

- Classes shuold be open for extension but closed for modification.

- Depend upon abstractions. Do not depend upon concrete classes.
  The dependency inversion principle.

- Principle of least knowledge: talk only to your immediate friends.

- Don't call us, we'll call you. Your framework should call your subclass methods, 
  not the other way around.

- A class should have only one reason to change. One class, one responsibility.
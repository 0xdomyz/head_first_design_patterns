Head first design patterns
==============================

Summary of patterns by categories
----------------------------------

Creational Patterns
^^^^^^^^^^^^^^^^^^^

Involve object instantiation and all provide a way to decouple a client 
from the objects it needs to instantiate.

    - Factory
    - Singleton

Structural Patterns
^^^^^^^^^^^^^^^^^^^

Let you compose classes or objects into larger structures.

    - Adapter
    - Decorator
    - Facade
    - Proxy

Behavioral Patterns
^^^^^^^^^^^^^^^^^^^

Concerned with how classes and objects interact and distribute responsibility.

    - Command
    - Iterator
    - Observer:

        Define a one-to-many dependency between objects so that when one object changes 
        state, all its dependents are notified and updated automatically.

    - State
    - Strategy:

        Define a family of algorithms, encapsulate each one, and make them interchangeable.
        Strategy lets the algorithm vary independently from clients that use it.

    - Template Method


Design principles
-----------------

- Encapsulate what varies.

- Program to an interface, not an implementation.

- Favor composition over inheritance.

- Strive for loosely coupled designs between objects that interact.
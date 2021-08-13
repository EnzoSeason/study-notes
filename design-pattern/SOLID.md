# SOLID

SOLID is composed by 5 principles.

## Single Responsibility Principle (SRP)

A class or module should have a single responsibility.

> A module can be composed by one or more than one classes.

There are some simple metrics for SRP.

- **The lines of code a class** shouldn't be too much (<200). **The parameters of a function** shouldn't be too much (<10).

- **The private methods** shouldn't be too much.

- **The name of the class** should be **specific**. (Abstract class is not included.)

However, it's not always good to follow this rule. **We don't split a small class into tiny pieces**. It also makes the code hard to maintain.

## Open Closed Principle

Software entities (modules, classes, functions, etc.) should be **open for extension , but closed for modification**.

It doesn't mean not making modification. It means making **mininum modification**, and the modification doesn't have or has little inpect on the old codes.

The ways to extend the code are:

- Polymorphism
- Dependency Injection
- Programming based on interfaces rather than implementation
- most of the design patterns (for example, decoration, strategy, template, chain of responsibility, state)

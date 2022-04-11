## Process Oriented Programming vs Object Oriented Programming

### Process Oriented Programming

Like OOP, POP is a coding style.

It's based on the **functions**. It's good at dealing with a process.

### Advantages of OOP

- In application, the processes are crossed, one depends on another. POP is not good at it, while OOP solves this problems.

- OOP has **Encapsulation, Abstraction, Inheritance, Polymorphism**, which help us maintain the application.

### Bad design in OOP

Some bad design will turn OOP to POP, let the codes hard to maintain. We should avoid following design.

#### Too many getters and setters

It exposes the private attributes, loses the **encapsulation** of OOP.

#### Too many static attributes and methods

We like setting **all the constant value** as static attributes, and put them in a class. Then, we can use them without initializing an instance.

This design lose the **encapsulation** of OOP, turns OOP into POP. The disadvantages are:

- hard to maintain

- slow to compile

To solve it, there are two ways.

- split a single "static" class, and use **meaningful names** for the new classes.

- DO NOT use "static" class. Declare the static value inside the classes.


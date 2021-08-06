# Abstract class vs Interface

## Abstract class

- Abstract class can't be instantised. It can only be inherited.

  > Because there are abstract functions in the abstract class.

- Abstract class has attributes and methods.

- The class that inherits the abstract class must override the abstract functions.

When a class inherits an abstract class, there is the `is-a` relationship between the classes

The advantages are:

- reuse the code. (DRY)

- avoid initializing the parent class accendentally.

- avoid forgetting to implement the methods.

## Interface

- Interface has methods, but no attributes

- Interface's methods can't be implemented.

- The class that implements the interface must implement all the methods in the interface.

When a class implements an interface, there is the `has-a` relationship between the classe and the interface.

The advantages are:

- decoupling the codes:

  The interface declares the methods of the class. The use only needs to know what methods can be used, doesn't
  need to think about how these methods are implemented.

## Practice

- When we want to **reuse code**, we think about the **abstract class**. When we want to **abstract the code**, we look for the **interface**.

- Usually, we first create child class, then create abstract parent class, while we first design the interface then write the class.

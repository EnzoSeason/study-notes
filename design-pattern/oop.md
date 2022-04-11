## OOP

### Basic

OOP is a programming style based on the **class** or **object**.

It has 4 main features, **Encapsulation, Abstraction, Inheritance, Polymorphism**.

### Encapsulation

By exposing **the limited access**, the class authorizes the outside to **access internal data ONLY through the function** provided by the class.

In the practice, we set **all the attributes of a class private**, and we create `get` or `set` functions to access or modify them.

The advantage is that

- The attributes won't be accidentally changed.

- It makes the class easy to use since there are less access.

### Abstraction

Encapsulation mainly talks about how to hide information and protect data, abstraction talks about how to **hide the specific implementation of functions**.

In the practice, we **implement a class by an interface**. The class can use all the functions of the interface without understanding these functions.

The advantage is:

- Easier to code since we use the existed functions.

### Inheritance

Inheritance is used to express **the is-a relationship between classes**.

Inheritance lets the child not only **inherits** parent's functions, but also **override** them.

The advantage is:

- DRY (Don't Repeat Yourself): The class can use the function in its parent class.

  > Composition can do the same. Sometimes, it's better than the inheritance.

The disadvantage is:

- Over-used inheritance is hard to maintain. That's why, sometimes, composition is better.

### Polymorphism

With the polymorphism, the parent class can be replaced its child.

There are 3 ways to realise the polymorphism.

- **inherit the parent class** and **override** its functions

- **implement the interface** and **implement** its functions.

- **duck-typing** (it appears in dynamic programming language because the tying is not required).

  Two classes have **no relationship** but have **a function shared the same name**. In this case, we can call this function and have different results, which depends on the instance we initialize.

  ```python
    class Logger:
        def record(self):
            print(“I write a log into file.”)

    class DB:
        def record(self):
            print(“I insert data into db. ”)

    def test(recorder):
        recorder.record() ## polymorphism

    def demo():
        logger = Logger()
        db = DB()
        test(logger)
        test(db)
  ```

The advatage is:

- Improve code **scalability and reusability**.
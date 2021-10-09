#  Introduction

When we program, we need to consider:

- maintainability

  - extensibility

  - flexibility

- readability

- simplicity

- reusability

- testability

![intro](./img/intro.png)

## OOP (Oriented Object Programming)

It's a popular coding style.

It has many useful feature, such as **Encapsulation, Abstraction, Inheritance, Polymorphism**.

It's the foundation of design pattern.

## Design Principles

Design principles are some **experience summaries** that guide our code design.

We need to grasp the **original intention of its design**, what programming problems it can solve, and what application scenarios it has.

- SOLID:

  - Single-responsibility principle:

    A class or module should have a **single responsibility**.

  - Open–closed principle:

    Software entities (modules, classes, functions, etc.) should be **open for extension , but closed for modification**.

  - Liskov Substitution Principle:

    If **S is a subtype of T**, then **objects of type T may be replaced with objects of type S**, without breaking the program.
  
  - Interface Segregation Principle:

    Clients should ONLY be forced to depend upon interfaces that they do use.
  
  - Dependency Inversion Principle:

    High-level modules shouldn’t depend on low-level modules. Both **modules should depend on abstractions**. In addition, abstractions shouldn’t depend on details. **Details depend on abstractions.**

- KISS: Keep It Simple and Stupid.

- YAGNI: You Ain’t Gonna Need It

- DRY: Don’t Repeat Yourself

- Law of Demeter (The Least Knowledge Principle): Each unit should only talk to its friends; Don’t talk to strangers.

## Design Patterns

Design Patterns are the solutions or design ideas that are summarized for some design problems often encountered in software development.

Most design patterns have to solve the problem of **code scalability**.

The difficulty of learning is to understand what problems they can solve, master **typical application scenarios**, and know how to not over-apply.

## Programming specification

It mainly solves the problem of **code readability**.

## Refactoring

It keeps the **code quality**. We need **Design Principles** and **Design Patterns** to refactor codes.

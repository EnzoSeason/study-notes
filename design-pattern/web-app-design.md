# Web App System Design

## Anemic Domain Model: Model View Controller (MVC)

In backend, there are 3 types of classes.

- Repository: It visites **data**.
- Service: It deals with **business logic**.
- Controller: It exposes the **endpoints**.


In **Service**, we have 2 classes, `Service` and `BussinessObject`. **BussinessObject (BO)** class processes **data only**. It hasn't logic codes which are in the Service class.

The class that **only contains data** are called **Anemic Domain Model**.

**Anemic Domain Model** splits the data and the operation, destroyes the **encapsulation** of OOP. **Data can be modified without the limit.**

## Rich Domain Model: Domain Driven Design (DDD)

DDD also has 3 types of classes, Repository, Service, Controller. But in Service, It has **Service** class and **Domain** class.

Unlike BussinessObject, Domain has **data and bussiness logic**. We use **Service** to connect **Repository** to get data, and put other bussiness logic code to **Domain**.

To sum up, **Domain** is a **BO** with **methods**.


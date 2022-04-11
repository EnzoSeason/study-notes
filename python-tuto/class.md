## Class

### constructor

```python
class Student:
    def __init__(self, name):
        self.name = name
```

`__init__` is constructor in Python class. There are other special methods in Python:

- `__str__` / `__repr__`:

    - `__str__`: string seen by user
    - `__repr__`: string seen by developer

    ```python
    class Student:
        def __init__(self, name):
          self.name = name
        def __str__(self):
            return 'Student object (name=%s)' % self.name
        __repr__ = __str__ # common trick for display

    s = Student('Michael')
    print(s) ## Student object (name=Michael)
    ```

- `__iter__` / `__next__`: The instance is iterable.

  - `__getitem__`: use for search / slice, for example `students[0]`, `students[1:3]`

- `__slots__`: limits of dynamic binding
    
    ```python
    class Student:
        __slots__ = ('name', 'age')
    
    s = Student() 
    s.name = 'Michael'
    s.age = 25
    s.score = 99 ## AttributeError: 'Student' object has no attribute 'score'
    ```

- `__getattr__`: when an inexistent attr is called, this function is triggered.

    ```python
    class Chain:

        def __init__(self, path=''):
            self._path = path

        def __getattr__(self, path):
            return Chain('%s/%s' % (self._path, path))

        def __str__(self):
            return self._path

        __repr__ = __str__
    
    Chain().status.user ## /status/user
    ```

- `__call__`: make instance callable

    ```python
    class Student:
        def __init__(self, name):
            self.name = name

        def __call__(self):
            print('My name is %s.' % self.name)
    
    s = Student('Michael')
    s() # My name is Michael.
    ```

### private attribute

```python
class Student:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
```

`__name` is a private attr.

`@property` makes life easier.

```python
class Student:

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
```

We can get / set `birth`, but `age` is read only.

### Inheritance

```python
class Animal:
    def __init__(self):
        print('init animal')

    def run(self):
        raise Exception('run not implemented.')

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('init dog')

    def run(self):
        print('dog runs')

dog = Dog()
isinstance(dog, Animal) # True
isinstance(dog, Dog) # True
```

This is a trick to force `Dog` override `run` function of `Animal`, use `raise Exception`.

We can also use `@abstractmethod` to decorate `run`, which makes `Animal` an abstract class. But abstract class has 2 limits:

- It can't be instanced
- All the abstract method must be override by the child class.

#### MixIn

Python allows inherits **multiple class**. Some classes provides services. We call them `MixIn`.

```python
class Animal:
    pass

class RunnableMixIn:
    def run(self):
        print('Running...')

class Dog(Animal, RunnableMixIn):
    pass
```

Dog is an animal, dog can run, but dog isn't a runnable. So we let dog inherit Animal and RunnableMixIn

### Class attribut vs Instance attribut

```python
class Student:
    IDENTITY = "student"

    def __init__(self, id):
        self.id = id;

print(Student.IDENTITY) ## student

jack = Student(1);
print(jack.id); ## 1
```

> DO NOT use the same name for class attr and instance attr.

### class method vs static method

class method does the tasks which can't be done by `__init__`.

The first params is `cls`.

```python
class Document: 
    WELCOME_STR = 'Welcome! The context for this book is {}.' 
    
    def __init__(self, title, author, context): 
        self.title = title 
        self.author = author 
        self.__context = context
        
    @classmethod 
    def create_empty_book(cls, title, author): 
        return cls(title=title, author=author, context='nothing')
```

In this example, the class method builds an empty context document.

static method is the method of class, not instance.

It hasn't `self` or `cls`.

```python
class Document:
    WELCOME_STR = 'Welcome! {}'

    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

print(Document.get_welcome('indeed nothing'))
```


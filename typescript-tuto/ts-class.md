#  Class & Interface

# #  Class

```typescript
class Department {
    name: string;

    constructor(n: string) {
        this.name = n;
    }
}

const accouting = new Derpartment("Accounting");
```

# # #  key word: this

`this` is tricky, for example. 

```typescript
class Department {
    // ... basic init
    describe() {
        console.log("Dep. " + this.name);
    }
}

const accouting = new Derpartment("Accounting");
cost accoutingCopy = {describe: accounting.describe};

accouting.describe(); // Dep. Accounting
accountingCopy.describe(); // Dep. undefinded
```
In this example, `this` in `accountingCopy` is binded to the dummy object `{describe: accounting.describe}`. This object doesn't has `name` property, so its output is undefinded. 

TypeScript can notify developper that there has missing property by passing `this` as a parameter into the methods in Class (just like the Class in Python).

```typescript
class Department {
    // ... basic init
    describe(this: Departement) {
        console.log("Dep. " + this.name);
    }
}
```

# # #  Inheritance

extend existing classes to create new ones using inheritance.

```typescript
class ITSupport extends Departement {
    developpers: string[];
    constructor(employees: string[]) {
        super("IT");
        this.developpers.push(...employees);
    }
} 
```

# # #  private protected, public modifier

The key word `private` can make `property`or `method` of the class only accessable by Class, not by Public.

```typescript
class Department {
    // ... basic init
    private employees: string[] = [];
}
```

shortcut: using `private / public` keyword, we can `defind and initialize` the property in constructor's parameters. 

```typescript
class Department {
    // ... basic init
    // public name: string
    constructor(public name:string){
        // this.name = name;
    }
}
```

The `protected` modifier acts much like the `private` modifier with the exception that members declared protected can also be accessed within `deriving classes`.

A `constructor` may also be marked protected. This means that the class **cannot be instantiated outside of its containing class**, but can be extended.

# # #  readonly modifier

Readonly properties must be initialized at their declaration or in the constructor. And they can not be modified.

```typescript
class Department {
    // ... basic init
    constructor(
        private readonly _id: number, 
        private _name: string){}
}
```

# # #  getter and setter

```typescript
class Department {
    // ... basic init
    get name(): string {
        return this._name;
    }

    set name(newName: string) {
        this._name = newName;
    }
}
```

# # #  Static Properties

They are visible on the class itself rather than on the instances.

```typescript
class Department {
    // ... basic init
    static showCompany() {
        console.log("test company");
    }
}

Department.showCompany();
```

# # #  Abstract Classes

Abstract classes are base classes from which other classes may be derived. They **may not be instantiated directly**.

Unlike an interface, an abstract class **may contain implementation details** for its members.

Methods within an abstract class that are marked as abstract **do not contain an implementation** and **must be implemented in derived classes**. 

```typescript
abstract class Department {
    // ... basic init
    abstract describe(): void
}

class ITSupport extends Departement {
    // ... basic init
    describe(): void {
        console.log("Dep. IT");
    }
}
```

# # #  singleton

```typescript
class ITSupport extends Departement {
    private static instance: ITSupport;
    static getInstance (): ITSupport {
        if (this.instance) { // "this" refers to the class ITSupport
            return this.instance;
        } else {
            this.instance = new ITSupport(["a"]);
            return this.instance;
        }
    }
    
    // private constructor
    private constructor(public developpers: string[]) {
        super("IT");
    }
}
```

# # #  Optional property

add `?` after property name

```typescript
class A {
    constructor(public id?: number){}
}
```


[Full example](../src/ts-class.ts)


# #  Interface

DO NOT exist in JavaScript

[Full example](../src/ts-interface.ts)

`private`, `public` or `protected` can not be used in Interface, but `readonly` can.

# # #  Function type

We can defind a Function type by: 

```typescript
type AddFn = (a: number, b: number) => number
```

We can also use the Interface to do it: 


```typescript
interface AddFn {
    (a: number, b: number) => number
}
```


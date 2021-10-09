#  Decorator

Decorators are used for meta programming to add extra configuration or extra logic.

Angular is heavily depended on Decorator.

# #  Basic

```typescript
function logger(constructor: Function) {
    console.log(constructor);
}

@logger
class Test {
    constructor(
        public name: string
    ) {}
}
```

`logger()` is executed when `Test` is **definded**, not is **instantiated**.

# #  Decorator Factory

```typescript
function Logger(message: string) {
    return function(constructor: Function) {
        console.log(message);
        console.log(constructor);
    }
}

@Logger('Logging Person')
class Test {
    constructor(
        public name: string
    ) {}
}
```

# # #  Order of decorator

```typescript
function Logger(message: string) {
    return function(constructor: Function) {
        console.log(message);
    }
}

@Logger('Logging Person1')
@Logger('Logging Person2')
class Test {
    constructor(
        public name: string
    ) {}
}

// Output
// Logging Person2
// Logging Person1
```
The first Decorate Factory executes first, then put its returned function into a **STACK**. The second does the same.

That's why the output is printed from bottom to up.

# #  Return a class in Decorator

To let the logic in Derator runs while the class is **instantiated**, we can return the class (technically, the constructor function) in Decorator.

```typescript
function WithTemplate(template: string, hookId: string) {
    console.log('TEMPLATE FACTORY');
    return function<T extends { new (...args: any[]): {name: string} }>(
      originalConstructor: T
    ) {
      return class extends originalConstructor {
        constructor(..._: any[]) {
          super();
          console.log('Rendering template');
          const hookEl = document.getElementById(hookId);
          if (hookEl) {
            hookEl.innerHTML = template;
            hookEl.querySelector('h1')!.textContent = this.name;
          }
        }
      };
    };
  }

@WithTemplate('<h1>My Person Object</h1>', 'app')
class Test {
    constructor(
        public name: string
    ) {}
}
```

# #  Autobind

```typescript
class Printer {
    message = "It works.";

    showMessage() {
        console.log(this.message);
    }
}

const p = new Printer();
const button = document.querySelector('button');
button.addEventListener('click', p.showMessage); // output after clicking: undefined.
```

To fix this problem, we need bind the object `p` to the `p.showMessage`.

```typescript
button.addEventListener('click', p.showMessage.bind(p));
```

Or, we can create a decorator to bind `p`.

```typescript
function Autobind(_: any, _2: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    const adjDescriptor: PropertyDescriptor = {
      configurable: true,
      enumerable: false,
      get() {
        const boundFn = originalMethod.bind(this);
        return boundFn;
      }
    };
    return adjDescriptor;
}

class Printer {
    message = "It works.";

    @Autobind
    showMessage() {
        console.log(this.message);
    }
}
```

# #  Validation

```typescript
interface ValidatorConfig {
  [property: string]: {
    [validatableProp: string]: string[]; // ['required', 'positive']
  };
}

const registeredValidators: ValidatorConfig = {};

function Required(target: any, propName: string) {
  registeredValidators[target.constructor.name] = {
    ...registeredValidators[target.constructor.name],
    [propName]: [...registeredValidators[target.constructor.name][propName], 'required']
  };
}

function PositiveNumber(target: any, propName: string) {
  registeredValidators[target.constructor.name] = {
    ...registeredValidators[target.constructor.name],
    [propName]: [...registeredValidators[target.constructor.name][propName], 'positive']
  };
}

function validate(obj: any) {
  const objValidatorConfig = registeredValidators[obj.constructor.name];
  if (!objValidatorConfig) {
    return true;
  }
  let isValid = true;
  for (const prop in objValidatorConfig) {
    for (const validator of objValidatorConfig[prop]) {
      switch (validator) {
        case 'required':
          isValid = isValid && !!obj[prop];
          break;
        case 'positive':
          isValid = isValid && obj[prop] > 0;
          break;
      }
    }
  }
  return isValid;
}

class Course {
  @Required
  title: string;
  @PositiveNumber
  price: number;

  constructor(t: string, p: number) {
    this.title = t;
    this.price = p;
  }
}
```


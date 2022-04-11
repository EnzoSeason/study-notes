# React Internals

## HOC (Higher-Order Components)

`render` function must return:

* a virtual element

* an array of virtual elements with the prop `key`

However, the array is not readable, the better way is to **wrap virtual elements in a virtual elements**

```javascript
const Aux = props => props.children;

export default Aux;
```

```html
<Aux>
    <!-- some virtual elements -->
</Aux>
```

`Aux` is HOC. React provides a same built-in HOC, `Fragment`.

HOC does two things:

1. wrap an array of virtual elements
2. add extra information to an array of virtual elements

HOC can be created in 2 ways:

* as a Component

    **WithClass.js** (Upper case indicates it's a component)
    ```javascript
    const WithClass = props => (
        <div className={props.classes}>{props.children}</div>
    );

    export default WithClass;
    ```

    **App.js**
    ```javascript
      render () {
        return (
            <WithClass classes="App">
            </WithClass>
        );
    }
    ```

* as a closure (a function enclosed with lexical environment))

    **withClass.js** (L ower case indicates it's a function)
    ```javascript
    const withClass = (WrappedComponent, className) => {
        return props => (
            <div className={className}>
                <WrappedComponent {...props}/>
            </div>
        );
    }

    export default withClass;
    ```

    **App.js**
    ```javascript
    render () {
        return (
            <Fragment>
            </Fragment>
        );
    }

    export default withClass(App, 'App');
    ```

    To pass props: `<WrappedComponent {...props}/>`

## PropTypes

To define the type of the props

```javascript
import PropTypes from 'prop-types';

class Greeting extends React.Component {
  render() {
    return (
      <h1>Hello, {this.props.name}</h1>
    );
  }
}

Greeting.propTypes = {
  name: PropTypes.string
};
```

## Refs

Refs provide a way to access DOM nodes or React elements created in the render method.

Avoid using refs for anything that can be done declaratively.

There are 3 ways:

* function: pass function to `rel`

    ```javascript
    class MyInput extends Component {
        componentDidMount() {
            this.inputEl.focus();
        }
        render() {
            <input rel={(el) => this.inputEl = el}>
        }
    }
    ```

* `React.createRef()`: create an elementRef and pass it to `ref`

    ```javascript
    class MyInput extends Component {
        constructor(props) {
            super(props);
            this.inputElementRef = React.createRef();
        }
        componentDidMount() { 
            this.inputElementRef.current.focus();
        }
        render() {
            <input rel={this.inputElementRef}>
        }
    }
    ```

* `useRef`: React hook

    ```javascript
    const MyInput = props => {
        const inputElementRef = useRef(null);
        // Similar to componentDidMount and componentDidUpdate:
        useEffect(() => {
            inputElementRef.current.focus();
        })
        
        return <input rel={inputElementRef}>
    }
    ```

## Context

Context provides a way to pass data through the component tree without having to pass props down manually at every level.

Sometimes, the same data needs to be accessible by many components in the tree, and at different nesting levels. Context lets you “broadcast” such data, and changes to it, to all components below. 

1. create context (AuthContext.js)

    ```javascript
    const AuthContext = React.createContext({
        authenticated: false,
        login: () => {}
    })
    ```

2. provide context (ParentClass.js)

    ```html
    <AuthContext.Provider value={
        {
            authenticated: this.authenticated
            login: this.loginHandler
        }
    }>
        <!-- the components consume the AuthContext -->
    </AuthContext.Provider>
    ```

3. consume context (MyClass.js)

    ```html
    <AuthContext.Consumer>
        {context => context.authenticated 
            ? <p>logged in</p> 
            : <p>not logged in</p> 
        }
    </AuthContext.Consumer>
    ```

    or, another way to consume context is using `contextType`

    ```javascript
    class MyClass extends React.Component {
        // subscribe the context
        static contextType = AuthContext;
        // This lets you consume the nearest current value of that Context type using this.context. 
        // You can reference this in any of the lifecycle methods including the render function.
        render() {
            let authenticated = this.context.authenticated;
            /* render something based on the value */
        }
    }
    ```
    However, you can only subscribe to a single context using this API.

    React hooks also can access the context.

    ```javascript
    const authContext = useContext(AuthContext);
    console.log(authContext.authenticated);
    ```
## Basic

### To create an HTML element

`React.createElement(el, props, ...children)`

* `el`: HTML element, like `div`

* `props`: the attributes of element

* `children`: the children of current element

```javascript
React.createElement(
    'div',
    {id: 'myDiv'},
    React.createElement('h1', null, 'Hi, JSX')
);
```

is equal to

```html
<div id="myDiv">
    <h1>Hi, JSX</h1>
</div>
```

### To create a component

* use `function`:

    ```javascript
    const Person = () => {
        return <p>Hi</p>
    }
    export default Person;
    ```

* use `class`

    ```javascript
    export default class Person extends Component {
        render() {
            return <p>Person</p>
        }
    }
    ```

Then, the component can be used:

```javascript
import Person from './Person/Person';

<Person />
```

#### props

1. To pass props to children, use `props.[propName]`

    props can be a **value**, or a **ref of function**.

    * use `function`:

        ```javascript
        const Person = (props) => {
            return <p onClick="props.changeName">{props.name}</p>
        }
        export default Person;
        ```

    * use `class`

        ```javascript
        export default class Person extends Component {
            render() {
                return <p onClick="props.changeName">{this.props.name}</p>
            }
        }
        ```

    ```javascript
    import Person from './Person/Person';

    <Person name="myName" />
    ```

    To pass function to children:

    ```javascript
    import Person from './Person/Person';

    class App extends Component {
        changeName = name => {
        //TODO
        };

        render() {
            return (
                <Person changName={this.changeName.bind(this, 'new name')} />
                // or, but can be inefficient
                <Person changName={() => this.changeName('new name')} />
            )
        }
    }
    ```

2. To pass children to children, use `props.children`

    * use `function`:

        ```javascript
        const Person = (props) => {
            return <div>{props.children}</div>
        }
        export default Person;
        ```

    * use `class`

        ```javascript
        export default class Person extends Component {
            render() {
                return <div>{this.props.children}</div>
            }
        }
        ```

    ```javascript
    import Person from './Person/Person';

    <Person>
        <div>Something to say</div>
    </Person>
    ```

3. receive data from children, use `event`

    ```javascript
    // in parent component
    class App extends Component {
        nameChanged = event => {
            console.log(event.target.value);
        }
        render() {
            return <Person nameChanged={this.nameChanged} >;
        }
    }
    ```

    ```javascript
    const Person = props => {
        return <input onChange={props.nameChanged}/>
    }
    ```

#### state

React components can have state by setting `this.state` in their constructors.

`this.state` should be considered as private to a React component that it’s defined in.

```javascript
// only class-based component
export default class Person extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: null,
        };
    }
    render() {
        return <p>{this.props.name}: {this.props.children}</p>
    }
}
```

to update `this.state`

* use `this.setState({value: 'some value'})`

* use React hook, `useState`, in function-based component.

    ```javascript
    const [myState, setMyStateFn] = useState({value: 'some value'});
    ```

    `useState` returns `myState` and `setMyStateFn`. `setMyStateFn` will update (not merge) the **whole** `myState`. 
    
    To avoid deleting state, use `useState` multi times for each state

Practice: use class to create `Stateful` component, use function to create `Stateless` component.

Use `Stateless` component as much as possible. It's much easier to maintain the project.

To set state correctly while using previous state:

```javascript
this.setState((prevState, props) => {
    return {
        couter: prevState.counter + 1
    }
})
```
### Styling

1. css file

    ```css
    .Person {
        /* some style*/
    }
    ```

    ```javascript
    import './Person.css'

    const Person = props => {
        return <div className="Person"></div>
    }
    ```

2. inline style

    ```javascript
    const Person = props => {
        const style = {
            margin: 10px;
        }
        return <div style={style}></div>
    }
    ```

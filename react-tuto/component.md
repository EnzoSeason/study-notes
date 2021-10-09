#  Component

# #  class-based vs functional

\ | class-based | functional
--- | --- | ---
props | yes, `this.props` | yes, it's from the input
state | yes, `this.state` | yes, `useState()`
lifecyle | yes | no

Class-based component is more powerful, it could be used as a **Stateful** component.

Functional componenet is simpler, it can be used as a **Stateless** component.

# #  lifecycle

# # #  Mounting

1. **constructor(props)**

    * Call `super(props)`, FIRST
    * Set up **State**, DO NOT call other functions, such as http request.

    ```javascript
    class MyComponent extends Component {
        constructor(props) {
            super(props);
            this.state = {name: 'my-component'};
        }
    }
    ```

    or, an easier way to set state:

    ```javascript
    class MyComponent extends Component {
        state = {name: 'my-component'};
    }
    ```

2. getDerivedStateFromProps(props, state)  

    *rarely used*, sync the state from props

    ```javascript
    class MyComponent extends Component {
        static getDerivedStateFromProps(props, state) {
            return state;
        }
    }
    ```

3. **render()**

    1. return JSX of current component
    2. render its child components

4. **componentDidMount()**

    * call other functions, such as http request
    * DO NOT cause re-rendering, like update states.

# # #  updating

1. getDerivedStateFromProps(props, state)

2. shouldComponentUpdate(nextProps, nextState)

    decide whether the component should be updated / re-rendered.

    It's for performance improvement, prevent useless update

    ```javascript
    class MyComponent extends Component {
        shouldComponentUpdate(nextProps, nextState) {
            if (this.state.person === nextState.person) {
                return false;
            }
            return true;
        }
    }
    ```

    In this case, when the `state.person` isn't changed, the component will not be updated. So, it's very important that:

    Always manipulate **the copy of state**.

3. **render()**

4. getSnapshotBeforeUpdate(prevProps, prevState)

5. **componentDidUpdate()**

    * call other functions, such as http request

# #  useEffect

`useEffect` makes functional component accessable to lifecycles:

* componentDidMount()

* componentDidUpdate()

```javascript
// Similar to componentDidMount and componentDidUpdate:
useEffect(() => {
    // Update the document title using the browser API
    // http request
});
```

# # #  control `useEffect`

pass the second param:

```javascript
useEffect(
    () => {},
    [props.person]);
```

That means, ONLY `props.person` changes, the component can be updated

If you don't want to update component at all, only init component, pass an empty array.

```javascript
useEffect(
    () => {},
    []);
```

# # #  cleanup

Sometime, we need cleanup, like remove event listener.

In lifecycle, there is a function, `componentWillUnmout()`.

`useEffect` can do cleanup, too.

```javascript
useEffect(
    () => {
        return () => { cleanup(); },
    }
);
```

# #  React.memo()

In class-based component, we need `shouldComponentUpdate` to control the update.

If you want to control the update in Functional Component, use `React.memo`.

```javascript
export default React.memo(MyComponent)
```

It will check if the `props` is changed.

Be careful of the update check. In a lot of cases, the stateless child component always is updated while its stateful parent component changes. In these cases, the update check is useless.

# #  PureComponent

A common case, we don't update component unless one of the props is updated, we use `PureComponent`.

```javascript
class MyComponent extends PureComponent {
    // useless codes because PureComponent is extended
    // shouldComponentUpdate(nextProps, nextState) {
    //     if (this.props.a !== nextProps.a ||
    //         this.props.b !== nextProps.b ||
    //         this.props.c !== nextProps.c ||
    //         this.props.d !== nextProps.d ) {
    //             return true;
    //     }
    //     return false
    // }
}
```
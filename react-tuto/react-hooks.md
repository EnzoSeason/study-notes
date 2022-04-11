## React Hooks

React hooks can be use ONLY in:

* functional components
* custom React hooks

### useState

The most important hook. It allows functional component to use **state**.

```javascript
// states includes: title: string, amount: number
const [title, setTitle] = useState('');
const [amount, setAmount] = useState(0);

// two-way binding

// setStateFn can take the new value
<input type="text" id="title" 
    value={title}
    onChange={event => setTitle(event.target.value)}/>

// setStateFn can take a function with previous state
<input type="number" id="amount" 
    value={amount}
    onChange={event => setAmount(prevState => event.target.value)}/>
```

* `useState` returns *2* results: *state* and *setStateFn* 

* state can be anything (in class based component, state must be an object). 

* state should be as easy as possible. we can use multiple `useState`

* after *setStateFn* executed, the component will be rerendered.

    > `setState1(value); setState2(value);` These 2 *setStateFn* ONLY trigger one rendering. Same as `this.setState()`

### useEffect

Another very useful React Hook. It controles the **side effect**, which is NOT affected on rendering DOM, such as:

* http request

It is executed **after every component's render cycle**

#### usage

```javascript
useEffect(() => {
    // TODO
});
```

This works as `componentDidUpdate`. It is executed **everytime when** component is rendered.

```javascript
useEffect(() => {
    // TODO
}, []);
```
This works as `componentDidMount`. It is executed **the first time when** component is rendered.

The second param controls the dependencies of re-execution. `[]` means NOTHING will trigger the re-execution.

However, we can provide dependencies. For exemple, `[data]` means re-execute the `useEffect` **everytime when** `data` is changed.

#### clean up function

`return` inside of `useEffect` is a clean up function. It runs before the next time component rendering or unmount.

```javascript
useEffect(() => {
  const subscription = props.source.subscribe();
  return () => {
    // Clean up the subscription
    subscription.unsubscribe();
  };
});
```

### useCallback

`useCallBack` caches the function. When the component is rerendered, the function will NOT be created again.

```javascript
const memoizedFn = useCallback(params => {
    // TODO
}, []);
```

As `useEffect`, the second param controls the dependencies. If one of the dependencies changes, the function will be re-created.

`useCallback(fn, deps)` is equivalent to `useMemo(() => fn, deps)`.

> Good practice: add `useCallBack` to the function which will be passed into child component.

### useMemo

Returns a memoized value. This optimization helps to avoid expensive calculations on every render.

If no array is provided, a new value will be computed on every render.

```javascript
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

### useRef

`useRef` holds a mutable value (as a pointer pointed to a memory).

Its props: `current` has access to the value.

```javascript
// create ref
const inputEl = useRef(null); // init by null

// assign ref
<input ref={inputEl} type="text" />

// use ref
console.log(inputEl.current.value);
```

### useReducer

An alternative to `useState`. It is usually preferable when :

* state logic involves multiple sub-values

* the next state depends on the previous one

```javascript
const initialState = {count: 0};

const reducer = (state, action) => {
    switch (action.type) {
    case 'increment':
      return {count: state.count + 1};
    case 'decrement':
      return {count: state.count - 1};
    default:
      throw new Error();
  }
};

[state, dispatch] = useReducer(reducer, initialState);

<button onClick={() => dispatch({type: 'decrement'})}>-</button>
<button onClick={() => dispatch({type: 'increment'})}>+</button> 
```

React guarantees that **dispatch function** identity is stable and won’t change on re-renders. This is why it’s **safe to omit** from the `useEffect` or `useCallback` dependency list.

### useContext

`useContext(MyContext)` is equivalent to `static contextType = MyContext` in a class, or to `<MyContext.Consumer>`, only lets you :
 * read the context 
 * subscribe to its changes (the component will be re-rendered if the context is changed)

 You still need a `<MyContext.Provider>` above in the tree to provide the value for this context.

 ```javascript
 // theme-context.js
 const themes = {
  light: {
    foreground: "#000000",
    background: "#eeeeee"
  },
  dark: {
    foreground: "#ffffff",
    background: "#222222"
  }
};

// create the context
const ThemeContext = React.createContext(themes.light);
```

```javascript
// App.js

// provider the context
function App() {
  return (
    <ThemeContext.Provider value={themes.dark}>
      <DeepTree />
    </ThemeContext.Provider>
  );
}
```

```javascript
// ThemeButton.js

// consume the context
// ThemedButton is a child of DeepTree
// ThemedButton will be re-rerendered if theme context changes.
function ThemedButton() {
  const theme = useContext(ThemeContext);
  
  return (
    <button style={{ background: theme.background, color: theme.foreground }}>
        I am styled by theme context!
    </button>
  );
}
```

### useContext

It passes data to components without using `props`., like `Redux`.

BUT, it shouldn't be used for **high frequence changes**. Because it lacks of improvement of performance.

It can be used for `user auth info`, `theme`, etc.

### Custom Hooks

The idea of custom hooks shares logic. (avoid doulbing codes)

1. The hooks is a **function**, named starts with `use`.

2. we can use built-in React Hooks in custom hooks


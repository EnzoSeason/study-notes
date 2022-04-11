# Redux

When we want to use **some data in the whole app**, we can pass it by `query parmeters` or `props`. But it's not convenient.

Redux is what you need.

## install 

```command
npm install redux react-redux
```

## Basic

Redux is a state management tool. It's independant to React. It has some concepts.

### Store

Store saves all the states in App. Only Reducers can update it.

```javascript
const store = redux.createStore(rootReducer);
```

### Reducers

It updates the store according to the actions.

Attention: current state is based on the **copy** of previous state

```javascript
// store/reducer.js
const rootReducer = (state = initialState, action) => {
    if (action.type === 'ADD_COUNTER') {
        return {
            ...state,
            counter: state.counter + action.value
        };
    }
    return state;
};
```

### Actions

Actions tell the Reducers how to update the Store. It can be **dispatched**.

```javascript
const action = {type: 'ADD_COUNTER', value: 10};
store.dispatch({type: 'ADD_COUNTER', value: 10});
```

### subscribe

Once Store is updated, it will tell all the components which subscribe it.

```javascript
store.subscribe(() => {
    console.log('[Subscription]', store.getState());
});
```
## react-redux

* `<Provider>`: inject Redux store into React

    ```javascript
    // index.js
    const store = createStore(reducer);

    ReactDOM.render(<Provider store={store}><App /></Provider>);
    ```

* **connect**: a HOC function

    * state

        ```javascript
        // Counter.js

        // pass state in store to component as props
        const mapStateToProps = state => {
            return {
                ctr: state.counter
            }
        }

        export default connect(mapStateToProps)(Counter);
        ```

        ```javascript
        // Counter.js

        // in the Counter class
        <div>{this.props.ctr}</div>
        ```
    
    * dispatch

        ```javascript
        // Counter.js

        // pass dispatch in store to component as props
        const mapDispatchToProps = dispatch => {
            return {
                onMyClick: () => dispatch({type: 'CLICK'});
            }
        }

        export default connect(mapStateToProps, mapDispatchToProps)(Counter);
        ```

        ```javascript
        // Counter.js

        // in the Counter class
        <button onClick={this.props.onMyClick}></button>
        ```

## Multi Reducers

use `combineReducers` to combine multi reducers into one

```javascript
const rootReducer = combineReducers({
    ctr: counterReducer,
    res: resultReducer,
});

const store = createStore(rootReducer);
```

To access `counterReducer`, we use `state.ctr`

```javascript
// Counter.js

const mapStateToProps = state => {
    return {
        ctr: state.ctr.counter
    }
}
```

However, in `counterReducer.js`, we can't access the `state`.


## update state immutably

[Immutable Update Patterns](https://redux.js.org/recipes/structuring-reducers/immutable-update-patterns/)

In Redux, always create a **new** state based on the old one.

There are two ways:

* Object.assign

    ```javascript
    const newState = Object.assign({}, state);
    newState.counter = state.counter + 1;
    return newState
    ```

* spread operator

    ```javascript
    return {
        ...state,
        counter: state.counter + 1
    };
    ```

manipulate the array

```javascript
function insertItem(array, action) {
  let newArray = array.slice()
  newArray.splice(action.index, 0, action.item)
  return newArray
}

function removeItem(array, action) {
  let newArray = array.slice()
  newArray.splice(action.index, 1)
  return newArray

  // or

  return array.filter((item, index) => index !== action.index)
}

function updateObjectInArray(array, action) {
  return array.map((item, index) => {
    if (index !== action.index) {
      // This isn't the item we care about - keep it as-is
      return item
    }

    // Otherwise, this is the one we want - return an updated value
    return {
      ...item,
      ...action.item
    }
  })
}
```


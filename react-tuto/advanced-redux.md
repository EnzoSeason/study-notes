# Advanced Redux

## Middleware

```javascript
// index.js

const logger = store => next => action => {
    console.log('Middleware', store.getState());
    const result = next(action);
    return result;
}

const store = createStore(rootReducer, applyMiddleware(logger));
```

`logger` will be executed when state in store changes.

## Redux DevTool

Install redux devtool on chrome, and add a middleware.

```javascript
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(rootReducer, composeEnhancers(applyMiddleware(logger)));
```

`compose` in Redux package is like `combineReducers`. It combines middlewares.

## Action Creator

action creator is the function **dispatchs action**.

```javascript
export const ADD_PERSON = "ADD_PERSON";
export const DELETE_PERSON = "DELETE_PERSON";

export const addPerson = () => {
    return {
        type: ADD_PERSON
    }
}

export const deletePerson = personId => {
    return {
        type: DELETE_PERSON,
        personId
    }
}
```

To use action creator:

```javascript
const mapDispatchToProps = dispatch => {
    return {
        addPerson: () => dispatch(actionType.addPerson()),
        deletePerson: (personId) => dispatch(actionType.deletePerson(personId)), 
    }
}
```

## Async Action
 
Action creator is powerful. It can handle async codes:

1. install `redux-thunk` middleware.

    ```javascript
    import thunk from 'redux-thunk';
    const store = createStore(rootReducer, composeEnhancers(applyMiddleware(logger, thunk)));
    ```

2. create an action creator which **dispatch asynchronously** an action

    ```javascript
    const deletePerson = personId => {
        return dispatch => {
            // an async func
            // For example, a http request
            setTimeout(() => {
                dispatch({type: 'DELETE_PERSON', id: personID});
            }, 3000);
        }
    }
    ```

## Action Creator vs Reducer

Since both Action Creator and Reducer can update state, when should we place the logic.

Personnaly, I prefer Reducer.

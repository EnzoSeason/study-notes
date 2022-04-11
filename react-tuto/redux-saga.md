## Redux Saga

[doc](https://redux-saga.js.org/)

A library that aims to make application **side effects** (i.e. asynchronous things like : 

* data fetching

* impure things like accessing the browser cache) 

easier to manage.

### example

Saga contains `generators`

* `yield` in `generator`: finish `yield` line, then run the next line.

* `put`: dispatch an action in saga

```javascript
// store/sagas/auth.js
import { put } from 'redux-saga/effect';

import * as actions from '../actions/index.js';

export function* signInSaga(action) {
    // start sign in
    yield put(actions.authStart());
    // prepare sign in
    const payload = {
        email: action.email,
        password: action.password
    };
    const url = "my-api.com";
    // sign in, and get the response
    try {
        const response = yield axios.post(url, payload);
        // save data
        localStorge.setItem('token', response.data.idToken);
        localStorge.setItem('expiresIn', response.data.expiresIn);
        // sign in successfully
        yield put(actions.authSuccess());
        yield put(actions.checkExpiration(response.data.expiresIn));
    } catch (err) {
        yield put(actions.authFailed(err)); 
    }
}
```

To trigger saga, first, we need an action received by saga.

```javascript
// store/actions/auth.js

export signIn = (email, password) => {
    return {
        type: actionType.SIGN_IN,
        email: email,
        password: password
    }
}
```

then, register saga

```javascript
// store/saga/index.js
import { takeEvery } from 'redux-saga';

import * as actionType from '../actions/actionType.js';
import { signInSaga } from './auth';

export function* wathAuth() {
    yield takeEvery(actionType.SIGN_IN, signInSaga);
}
```

finally, add saga to redux, and run saga.

```javascript
// index.js
import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga'
import { wathAuth } './store/sagas/index.js';

// some other codes ...

// create the saga middleware
const sagaMiddleWare = createSagaMiddleWare();
// mount it on the Store
const store = createStore(
    rootReducer,
    applyMiddleware(sagaMiddleWare)
);
// then run the saga
sagaMiddleWare.run(wathAuth);
```

### More function in redux-saga

* `call`: call the function. make Unit test easier

* `all`: merge multi function into one

* `takeEvery` vs `takeLastest`
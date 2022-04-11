## Redux Hooks

### useDispatch

```javascript
// outside Component Function

const mapDispatchToProps = dispatch => {
    return {
        addIngredient: (ingName) => dispatch(actions.addIngredient(ingName)),
    }
}
```

replace by

```javascript
// inside Component Function

 const addIngredient = (ingName) => dispatch(actions.addIngredient(ingName));
```

### useSelector

```javascript
// outside Component Function

const mapStateToProps = state => {
    return {
        price: state.burgerBuilder.price
    }
}
```

replace by

```javascript
// inside Component Function

const price = useSelector(state => state.burgerBuilder.price);
```
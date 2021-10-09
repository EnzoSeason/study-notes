#  Lists and Conditionals

# #  Conditional

Unlike Angular, there isn't `ngIf` in React.

* user `condition ? case true : case false` inline

    ```javascript
    const Person = props => {
        return (
            <div>
                {
                    props.isAdmin
                    ? <div id="admin"></div>
                    : <div id="notAdmin"></div>
                }
            </div>
        );
    }
    ```

* split the code

    ```javascript
    const Person = props => {
        let part = null;
        if (props.isAdmin) {
            part = <div id="admin"></div>;
        } else {
            part = <div id="notAdmin"></div>;
        }

        return <div>{ part }</div>;
    }
    ```

# #  List

React don't have `ngFor`, but we can use JS to do it directly.

```javascript
let persons = this.state.persons.map(person => {
    return <Person key={person.id} />;
})
```

`key` is required by React to create a list. `key` must be unique.

# #  state management

1. JS returns the **ref** of an Object
2. Always use `setState` to manipulate the state

That means, always **copy the `this.state.attr`** when we want to manipulate `attr`.

```javascript
let persons = null;

// always copy the state
// for a list
persons = this.state.persons.slice();
// or
persons = [...this.state.persons];
// for an object
const id = 1;
const ownerIndex = persons.findIndex(person => person.id === id);
let owner = null;
owner = Object.assign({}, this.state.persons[ownerIndex]);
// or
owner = {...this.state.persons[ownerIndex]};

// manipulate
persons = persons.pop();
owner.name = 'Jack';


// set state
this.setState({
    owner: owner,
    persons: persons
});
```

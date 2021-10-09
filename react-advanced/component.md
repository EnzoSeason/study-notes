# Component

The component is the core of React. It composes the React App.

## Basic

1. Component is a **pure function**. Only the `props` and the `states` can change it.

> Pure function: The function always returns the same result when it receives the same input. And it doesn't cause any side effect.

2. Component doesn't interest in the detail. When it changes, it rebuilds itself instead of updating a part of it.

3. Component'data is one-way-binding

   - Input: pass data as `props` into the component
   - Output: pass the function into the component, and bind it on an `event`, such as `onClick`, `onChange`, etc.


## Rule

1. make small and simple component

   If the component is too big, split it

2. DRY(don't repeat yourself)

   reuse the component as much as possible
   do not store useless state

3. use stateless component as much as possible. use `props` to pass in data
   Stateless component is easier to write and maintain. `state` increases the complexity of the component.

## Controlled component vs Uncontrolled component

A controlled component is only controlled by the `state`.

```js
<input value={this.state.val} onChange={handleInputChange}>
```

Either `value` or `onChange` is missing, the input value won't be changed. Because the `state` is not changed. So that the component won't be rebuilt.

It's the recommanded way to deal with `input`, `select` or `textarea`.


Uncontrolled component is not controlled by the `state`. It's the tradition way to code, using DOM API. It loses the track of `state`.

## life cycle

1. Mounting

    1. constructor()

      initialize state

    2. getDerivedStateFromProps()

      initialize state from props

    3. render()

    4. componentDidMount()

2. Updating

    1. getDerivedStateFromProps()

    2. shouldComponentUpdate()

    3. render()

    4. getSnapshotBeforeUpdate()

    5. render()

    6. componentDidUpdate()

3. Unmounting

    1. componentWillUnmout()

## Virtual DOM

React doesn't update DOM tree directly. It creates virtual DOM. When an update comes, it will **differ 2 virtual DOM tree** and update part of the tree. The time complexity of `diff` is `O(n)`.

`diff` function uses **BFS**. It reads the tree **level by level**.

- If the nodes' position is changed, React switches the nodes.

- If the node's attributes are changed, React removes it and creates a new one.

- If the node changes the level, React won't deal with it. React only **remove a node** or **add a node**.

React makes some supposes.

- DOM is relatively stable. It's rare that a node changes the level.

- The sibling nodes have an unique id, `key`. So that, React can know their position and switches them.


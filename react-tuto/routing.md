# Routing

## set up

use `react-route-dom` package

Wrap the App with BrowserRouter

```javascript
<BrowserRouter>
    <App />
</BrowserRouter>
```

## Route

* render: 

    ```javascript
    <Route path="/" exact render={() => <div>Home</div>} />
    ```

    Attention: without `exact`, it will match the routes that have `/`, which means all the routes.

* component:

    ```javascript
    <Route path="/posts" component={Posts} />
    ```

## Switch

find one of its children, from top to bottom, to fit the current url.

This means that you should put `<Route>s` with more specific (typically longer) paths **before** less-specific ones.

```javascript
<Switch>
    <Route path="/posts" component={Posts} />
    <Route render={() => <NotFound />} />
    {/* <Route path="/" component={Home} />*/}
</Switch>
```

## Route info

The information of Route, like `match.url`, `match.params` is passed into the component as `props`.

While the children components haven't access to this info, we use `withRouter`.

```javascript
export default withRouter(ChildComponent);
```

## Link

instead of using `<a>`, which will reload the whole app, using `<Link>` to navigate inside the app.

```javascript
<Link to="/">Home</Link>

<Link to={{
    pathname: "/search",
    hash: "#search",
    search: "?quick-submit=true"}}>Search</Link>
```
> `Link` of react-route-dom wraps `<a />`.

`<NavLink />` adds `active` class to Link, we can **style the Link** by CSS:

```css
a.active {
    color: red;
}
```

We can override the name of class by `activeClassName`:

```javascript
<NavLink to="/" exact activeClassName="home-active">
```

```css
a.home-active {
    color: red;
}
```

`activeStyle` can set the inline-style of NavLink

## absolute vs relative path

* absolute

    ```javascript
    <Link to="/" exact>Home</Link>
    ```

* relative

    add `/1` after the current url

    ```javascript
    <Link to={this.props.match.url + "/1"}>Page 1</Link>
    ```

## Route params

```javascript
<Link to="/post/new" exact>new</Link>
<Link to="/post/:id" exact>post</Link>
```

Put the route with params at the **end** of all routes, avoid pass `new` to `:id`

to extract route params, we can use `props.match.params`:


```javascript
// Home.js
<Link to="/post/:id" exact component={Post}>post</Link>
```

```javascript
// Post.js 
componentDidMount() {
    const id = this.props.match.params.id; 
}
```

## navigating programmatically

```javascript
props.history.push('/post/new');
```

which navigates to a new page.

## Redirection

```javascript
<Redirection from="/" to="/posts" />
```

redirect after post created

```javascript
postHandler = () => {
    this.setState({
        redirect: true
    });
}

render() {
    const redirect = <Redirect to="/posts" />;
    return (
        <Fragment>
            {this.state.redirect ? redirect : null}
            <div>Something else</div>
        </Fragment>
    );
}
```

### redirect vs push

`this.props.history.push('/posts')` can also change the page, but:

* push just add the new page into stack. We can click back to return the current page.

* redirect can the remove the current page in the stack, and add the new page into the stack

    redirect is equal to `this.props.history.replace('/posts')`

## Guards

There hasn't a Guard which is like the one in Angular, but we can control is in 2 ways

* render

    ```javascript
    {this.state.isAuth ? <Secret /> : null}
    ```

* redirect

    ```javascript
    componentDidMount() {
        axios.get('/secrets-access').then(
            res => {
                if (!res.data.isAuth) {
                    this.props.history.replace('/non-secret');
                }
            }
        )
    }
    ```

## Lazy Loading

To load the components asynchronous, use `React.lazy` & `Suspense`

Like `React.Fragment`, `React.lazy` & `Suspense` is for React 16+

```javascript
// import Post from '../Post'

const Post = React.lazy(() => import('../Post'));


render() {
    return (
        <Route
            path="/post"
            render={() => (
                <Suspense fallback={<div>Loading...</div>}>
                    <Post />
                </Suspense>
            )}
        />
    );
}
```

or, we can create our HOC lazy: [lazyComponent](../react-basic/src/HOC/lazyComponent.js)

to use it: 

```javascript
const LazyPerson = lazyComponent(() => import('./Person/Person'));

const lazyPerson = (
    <LazyPerson 
    name={this.state.name}>
        <span>lazy</span>
    </LazyPerson>
);
```


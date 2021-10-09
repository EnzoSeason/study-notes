#  HTTP

# #  call api

use `axios` to call api in the lifecycle: 

* **componentDidMount**

* componentDidUpdate

    be careful, state changes will trigger component update. It may cause infinit loop, here.

```javascript
componentDidMount() {
    axios.get('/api/posts').then(
        response => {
            this.setState({posts: response.data});
        }
    ); 
}
```

# #  handle error

```javascript
axios.get('/api/posts')
    .then(response => {})
    .catch(error => {})
```

# #  interceptor

We can manipulate the request and response using axios:

* axios.interceptors.request.use()

* axios.interceptors.response.use()

# # #  add

in the root: `index.js`

```javascript
axios.interceptors.request.use(
    request => {

        return request;
    },
    error => {
        return Promise.reject(error);
    }
);
```

# # #  remove

```javascript
componentDidMount() {
    this.myInterceptor = axios.interceptors.request.use(() => {/*...*/});
}

componentWillUnmount() {
    axios.interceptors.request.eject(this.myInterceptor);
}
```

# #  Global configuration

In the root: `index.js`

# # #  base url

```javascript
axios.defaults.baseUrl = "www.my-api.com";

axios.get('/posts'); // www.my-api.com/posts
```

# # #  authorization

```javascript
axios.defaults.header.common['Authorization'] = "AUTH TOKEN";
```

# #  Instance of axios

It's another way to set global configuration.

In the root, create `axios.js`

```javascript
const AxiosInstance = axios.create({
    baseUrl: 'www.my-api.com',
});
instance.defaults.header.common['Authorization'] = "AUTH TOKEN";

export default AxiosInstance;
```
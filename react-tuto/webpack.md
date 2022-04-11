# webpack

## basic

webpack run on **Node.js**. There are 4 important concepts:  

1. entry: **one file, at least**. could be root js file (app.js)

2. loaders: file-type transformations, for example, 
    
    `babel-loader` for `*.js`, `css-loader` for `*.css`

2. plugins: works after loaders

4. output

## React project

We need to install a lot of package to init a React project. Here is an example:

[package.json](./code/package.json)


To config webpack, we use `webpack.config.js`. It is used on node.js:

[webpack.config.js](./code/webpack.config.js)


## babel

It handles js file.

* In `webpack.config.js`, we tell webpack to use babel handle js file

* In `.babelrc`, we config babel

[example](./code/.babelrc)

## css file

There are 2 loaders which deal with css files

* `css-loader`: parse css files
* `style-loader`: inject css into html

## assets

need `url-loader` and `file-loader`

## Production

* create a file, `webpack.config.prod.js`

* set `mode: 'production'`

* run `webpack --config webpack.config.prod.js`
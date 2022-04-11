# Next.js Test

The article will talk about how to test Next.js

## install packages

Our next app is written by Typescript. We need to install some packages

```command
npm install -D @testing-library/dom @testing-library/react @testing-library/jest-dom @testing-library/dom jest babel-jest @types/jest ts-jest
```

```json
{
    "@testing-library/dom": "^7.29.4",
    "@testing-library/jest-dom": "^5.11.9",
    "@testing-library/react": "^11.2.5",
    "@types/jest": "^26.0.20",
    "babel-jest": "^26.6.3",
    "jest": "^26.6.3",
    "ts-jest": "^26.5.1",
}
```

## create `.babelrc`

Once these have been installed, the next step is to create a `.babelrc` configuration file to instruct `babel` to use the custom preset for Next.js. 

`.babelrc` is at the root of the project.

```json
{
  "presets": ["next/babel"]
}
```

## create `jest.config.js`

create a blank `jest.config.js` at the root of project.

```command
npx ts-jest config:migrate jest.config.js
```

`ts-jest` will create a `jest.config.js` in console. Copy it.

```javascript
module.exports = {
  moduleFileExtensions: ["js", "json", "jsx", "node", "ts", "tsx"],
  globals: {
    "ts-jest": {
      tsconfig: "jest.tsconfig.json",
      babelConfig: true,
    },
  },
  testMatch: ["**/*.(test|spec).(ts|tsx)"],
  testPathIgnorePatterns: ["/node_modules/", "/.next/"],
  coveragePathIgnorePatterns: ["<rootDir>/node_modules/", "<rootDir>/.next/"],
  coverageReporters: ["json", "lcov", "text", "text-summary", "clover"],
  moduleNameMapper: {
    "\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$":
      "<rootDir>/__mocks__/fileMocks.js",
    "\\.(css|less|scss)$": "<rootDir>/__mocks__/styleMocks.js",
  },
  preset: "ts-jest",
};
```

All the tests must written in the file named as `*.(test|spec).(ts|tsx)`.

If you config the path alias in `tsconfig.json`, we need to config it in `jest.config.js`, too.

```json
// tsconfig.json
{
  "baseUrl": ".",
  "paths": {
    "@components/*": ["components/*"],
    "@layouts/*": ["layouts/*"],
    "@styles/*": ["styles/*"],
  }
}
```

```javascript
// jest.config.js
moduleNameMapper: {
  "@layouts/(.*)": "<rootDir>/layouts/$1",
  "@components/(.*)": "<rootDir>/components/$1",
  "@styles/(.*)": "<rootDir>/styles/$1",
},
```

Next, we need create `jest.tsconfig.json` and `mocks`.

## create `jest.tsconfig.json`

`jest.config.js` needs it. It extends `tsconfig.json` and sets `"jsx": "react"`.

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "jsx": "react"
  }
}
```

## create scripts

add command to `package.json`

```json
{
  scripts: {
    "test": "jest --watch",
    "coverage": "jest --collect-coverage"
  }
}
```

run `npm run test` when you need to write the test

run `npm run coverage` to see code coverage.

## create mocks

Files and styles is not interested in Tests. We create the `mocks` at `/__mocks__/`.

```javascript
// fileMock.js
module.exports = "placeholder-file";
```

```javascript
// styleMock.js
module.exports = {};
```

## mock services

We don't want to use http connection in unit test. We need to mock it.

1. create mock service

    In `__mocks__`, we create mock service. Usually, we mock the functions, such as `get`, `post`, etc. We return a `Promise` having `resolve` and `reject`.

2. register mock service to `jest.config.js`

    As other mocks, we register service mocks in `moduleNameMapper`.

    After registration, mock service will replace the real service in unit tests

3. use `jest.mock()` on mock service

    In unit test, we don't use mock service directly. `jest.mock` helps us trigger `resolve` or `reject`. It makes testing much easier.




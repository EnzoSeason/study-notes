# Preparation

This tuto is writen in TypeScript.

## Server

The server uses `Express`. It serves 2 things:

* `index.html` of client folder (`client.js` is import by HTML, so it's served, too)
* all the needed files from `Three`

Server used `common.js` to run JavaScript code, so in `tsconfig.js`, we need to specify it.

```json
"compilerOptions": {
    // ... other settings
    "module": "commonjs",
    "esModuleInterop": true
},
```

## Client

We write codes in `client.ts`, then this file is tranlated into `client.js` and imported by `index.html`.

If we need to import file into `client.ts`, we must config the paths.

```json
"compilerOptions": {
    // ... other settings
    "baseUrl": ".",
    "paths": {
        "/build/three.module.js": ["../../node_modules/three/src/Three"],
        "/jsm/*": ["../../node_modules/three/examples/jsm/*"],
    }
}
```

## npm run dev

To run the project, we need to run 3 commands:

* `tsc -p ./src/client -w` : watch and compile client-side codes
* `tsc -p ./src/server -w` : watch and compile server-side codes
* `nodemon ./dist/server/server.js`: run dev server
    > `nodemon` command is more powerful then `node`because it can automatically restart the node application when file changes in the directory are detected.

To run these 3 commands in one, we use `concurrently`.

Add command in `package.json`

```json
{
    // other configs
    "scripts": {
        "dev" : "concurrently -k \"tsc -p ./src/client -w\" \"tsc -p ./src/server -w\" \"nodemon ./dist/server/server.js\""
    },
}
```

`-k`: kill other processes if one exits or dies
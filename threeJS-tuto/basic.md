## Basic

### Object 3D

The most common things you will do with an Object3D:

- Rotation: number

- Position: number

- Scale: number

- Visibility: boolean


```typescript
const cube: THREE.Mesh = new THREE.Mesh(geometry, material);

// cube.rotation
// cube.position
// cube.scale
// cube.visible
```

Three.js applies **Transformation matrix** on original object. That means original geometry of the object is NOT changed. 

If we want to create a new geometry of the object:

```typescript
const newGeometry = new THREE.BoxGeometry();
cube.geometry.dispose(); // clear the old geometry in the memory
cube.geometry = newGeometry;
```

As you can see, 3D object has 2 parts: **Geometry** and **Material**.

### Geometry

It defines the shape of object, like Box, Cylinder, Text, etc.

Three.js always, first, create a Buffer Geometry, which improves the performance.

### Material

There are some props for material

- transparent: boolean

- opacity: number, it works when transparent === true

- depthTest: boolean, whether ignore the distance between camera and object. Default is true (not ignored).

- depthWrite: boolean, When drawing 2D overlays it can be useful to disable the depth writing in order to layer several things together without creating z-index artifacts.

- visible: boolean

- side: 1 | 2 | 3, set Front side, Back side or Double side visible 

When the material needs to be update, set the flag `needsUpdate` to true. It tells WebGL re-render the object.
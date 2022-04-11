## Mesh

### MeshBasicMaterial

The simplest mesh in Three.js. It doesn't need light or texture settings. It helps you create an 3D object quickly. (with wireframe === true)

There are some props can be modify:

- color

- wireframe

- texture

- reflectivity: reflect the enviroment texture

- refractionRatio: zoom in or out the reflection

- combine: combine texture and reflection

### MeshNormalMaterial

It's also a simple mesh. It doesn't need light or texture settings, either.

It provides flatShading which doesn't exist in BaseMaterial.

## MeshMatcapMaterial

It doesn't need light. It can map image on the object.


### MeshLambertMaterial

This material needs light. However, we can set `emissive` to show it.

### MeshPhongMaterial

This material needs light, and it can control the shininess of the reflection. It is useful for polish object.

It is expensive.


## MeshStandardMaterial

It needs light, and it is expensive.

It provides 2 more options:

- roughness

- metalness

## MeshPhysicalMaterial

It is an extention of MeshStandardMaterial. It has reflectivity and refractionRatio.


### MeshToonMaterial

Toon shading or Cel shading, it makes the object more cartoonish.
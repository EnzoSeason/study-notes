## Maps

### Specular Map

It's a **texture image** that affects:

- surface highlight

- environment map of the MeshPhongMaterial, looks like a frosted glass

The **MeshLambertMaterial**, **MeshPhongMaterial** and the **MeshToonMaterial**, the meshes *require light*, have the SpecularMap option.

In practice:

1. In Specular map, white part is full specular and black is not specular.

2. `THREE.TextureLoader` loads the specular map. `mesh.specularMap` uses it.

3. The texture (specular map) will be shown in the light by the reflection.

### Roughness Map and Metalness Map

The roughnessMap and metalnessMap are the specularMap equivalents for the MeshStandardMaterial and the MeshPhysicalMaterial.

### Bump Map

An image texture to create a bump map.

The Bump map doesn't actually affect the geometry of the object, only the **lighting**. It helps improve the view of 3D (make 2D image bump up).

### Displacement Map

An image that can be used to alter the geometry of a mesh.

The value of **each pixel** is used to change **the position of the vertices** of the mesh. 

### Material Repeat and Center

Where material textures sit on a geometry can be changed by changing their **UV co-ordinates**.

We can use `texture.repeat` to select (zoom in or zoom out) a part of the object, `texture.center` to move the focus.

### Texture Mipmaps

Three.js creates different sizes of texture,and renders them on the object depending **how far away it is from the camera**.

`texture.magFilter` is for **close view**, when the pixel being textured maps to an area **less than or equal** to one texture element (texel).

`texture.minFilter` is for **far view**, when the pixel being textured maps to an area **greater than** one texture element (texel).

### Custom Mipmaps

`texture.mipmaps` is an **array of function**. We can create custom function, and apply on it.

### Anistropic Filtering

Anisotropic Filtering allows us to improve the quality of the Mipmaps.
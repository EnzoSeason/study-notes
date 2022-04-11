## Light

They all extend from the **THREE.Light base class**, which in turn also extends from the **Object3D base class**.

The base class properties:

- color
- intensity
- isLight (Read Only)
- receiveShadow
- shadow

### Ambient Light

The most common light is Three.js.

- Lights all objects in the scene equally, except for self illuminating objects such as MeshBasicMaterial, meshNormalMaterial and MeshMatcapMaterial.

- Light is spread equally in all directions and distances.

- Doesn't cast shadows.

- Materials won't show shading depending on geometry normals and there will be no specular affect, so meshes in front of other meshes will be invisible if they have identical materials or even a single colour map texture.

### Directional Light

The light rays from a DirectionalLight are parallel in the direction.

### Hemisphere Light

The Threejs Hemisphere light is very like a directional light but also with settings to project the light in the reverse direction:

- sky color: `color`

- ground color: `groundColor`

### Point Light

A light that gets emitted from **a single point** in all **directions**.

- distance: Maximum range of the light. Default is 0 (no limit).

- decay: The amount the light dims along the distance of the light. Default is 1.

### Spot light

A Point light with more controls

- distance

- decay

- angle : Maximum angle of light dispersion from its direction whose upper bound is Math.PI/2

- penumbra : Percent of the **spotlight cone** that is attenuated due to penumbra. Takes values between zero and 1. Default is zero.

### Spot Light Shadow

The Spot Light Shadow uses a **PerspectiveCamera** frustum to calculate the shadows.

### Directional Light Shadow

The Directional Light Shadow uses an **OrthographicCamera** to calculate the shadows. This is because the light rays from the DirectionalLight are parallel.
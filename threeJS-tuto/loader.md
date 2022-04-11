# Loader

- blender: tools to create 3D models, animations, etc
- [mixamo](https://www.mixamo.com): 3D models

## OBJ Model Loader

There are many DCC (Digital Content Creation) tools that can create models in **OBJ format**.

When importing an OBJ, the default material will be a white **meshPhongMaterial** so you will need **at least one light** in your scene.

```javascript
objLoader.load(
  "models/cube.obj", // url of model
  (object) => {
    // manipulate model

    // add model to scene
    scene.add(object);
  },
  (xhr) => {
    // loading process
    console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
  },
  (error) => {
    console.log(error);
  }
);
```

## MTL Loader

MTL is the **material** information used by an **OBJ** file.

```javascript
const mtlLoader = new MTLLoader();
mtlLoader.load(
  "models/monkey.mtl",
  (materials) => {
    materials.preload(); // preload materials

    // load obj mapped by materials
    const objLoader: OBJLoader = new OBJLoader();
    objLoader.setMaterials(materials);
    objLoader.load(
      "models/monkey.obj",
      (object) => {
        scene.add(object);
      },
      (xhr) => {
        console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
      },
      (error) => {
        console.log("An error happened");
      }
    );
  },
  (xhr) => {
    console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
  },
  (error) => {
    console.log("An error happened");
  }
);
```

## GLTF Model Loader (popular)

glTF is a specification for the efficient transmission and loading of 3D scenes and models.

glTF **minimizes both the size of 3D assets**, and the runtime processing needed to unpack and use those assets.

A glTF file may contain one or more scenes, meshes, materials, textures, skins, skeletons, morph targets, animations, lights and cameras. **(everything)**

Assets can be provided in either JSON (.gltf) or binary (.glb) format.

```javascript
const loader = new GLTFLoader();
loader.load(
  "models/monkey.glb",
  function (gltf) {
    // add to scene
    scene.add(gltf.scene);
  },
  (xhr) => {
    console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
  },
  (error) => {
    console.log(error);
  }
);
```

## DRACO Loader

The DRACO loader is used to load geometry **compressed with the Draco library**.

Compressed geometry can be **significantly smaller**, but at the **cost of additional decoding time** on the client side browser.

glTF files can also be compressed using the DRACO library, and they can also be loaded using the glTF loader.

```javascript
var dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath('/js/libs/draco/');
dracoLoader.setDecoderConfig({ type: 'js' });

const loader = new GLTFLoader();
loader.setDRACOLoader(dracoLoader);
loader.load(
    // ...
);
```

## FBX Model Loader
The FBX format is used to provide interoperability between **digital content creation applications** and **game engines** such as Blender, Maya, Autodesk, Unity, Unreal and many others. 

It supports many features such as 3D models, scene hierarchy, materials, lighting, animations, bones and more.

```javascript
const fbxLoader: FBXLoader = new FBXLoader();
fbxLoader.load(
    'models/kachujin_g_rosales.fbx',
    (object) => {
        scene.add(object);
    },
    (xhr) => {
        console.log((xhr.loaded / xhr.total * 100) + '% loaded')
    },
    (error) => {
        console.log(error);
    }
)
```

## STL Model Loader

The STL model format is widely used for rapid prototyping, 3D printing and computer-aided manufacturing.

STL files describe only the surface geometry of a three-dimensional object without any representation of color, texture or other common 3d modelling attributes.

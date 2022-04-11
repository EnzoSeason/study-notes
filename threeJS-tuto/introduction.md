## Introduction

### Scene, Renderer, Camera

- Scene:

  Scene allows you to **set up** what is to be rendered by three.js.

  We can have **multiple scenes**. When you have a scene, you can then add **objects and lighting**.

- Renderer:

  The Renderer displays the scene onto a **HTML Canvas Element**.

  By default it uses **WebGL**. So, the coordinate is:

    * x: left to right (朝右)
    * y: bottom to top (朝上)
    * z: back to front (朝外)

- Camera

  There are many types of Cameras in Threejs.

  The **Perspective projection** is designed to mimic the way the human eye sees. It is a very common projection mode.

  The **Orthographic projection** is like a cube in itself where the perspective remains constant **regardless of it's distance from the camera**.

### Tools

- stats: It can monitor the performance (fps, MS, MB). [link](https://github.com/mrdoob/stats.js/)

- Dat GUI: A lightweight graphical user interface for changing variables. [link](https://github.com/dataarts/dat.gui)

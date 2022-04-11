## Signature detection

### Introduction

Recently, I've worked on an innovation project, **signature detection**. It judges whether a document is signed. It's a very interesting project. I would like to share this experience, bringing an innovation project from the lab to production. The project is on my website, [Signature Detection](https://seasonliu.com/station/signature-detection). It's free to use :)

This project is split into several phases.

1. Do experiments: **explore ideas** and **find a solution**

2. Make a package: realize the solution **by coding**

3. Create a backend API: put codes into a **web application**

4. Create a frontend UI: **show the results** and **interact with users**

This article will walk through all these stages. Let's go!

### Do experiments

In this stage, The primary question we should think about is **whether the project doable?** We need to come out the ideas **as much as possible** and test them **as fast as possible**.

For example, to detect a signature, we can detect

- the handwriting
- the curves
- the area size of connected pixels
- the number of the pixels at the bottom of the image
- …

As you can see, the object we detect becomes more and more **general**. The solution becomes **less and less reliable**, however, the project becomes **more and more doable**. During the experiments, we need to find the balance between reliability and doability.

I chose **the area size of connected pixels** as the indicator of the signature. I chose it because the size of the signature is neither too big nor too small in a document. It's relatively unique. Besides, the handwriting and curves are difficult to detect, and the signature can appear at any place in a document. So, I crossed out the other 3 options.

The application I used to do experiments is [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/). My programming language is Python.

### Make a package

If **the width of the ideas** is the key point of the previous stage, **the depth of an idea** is the core of the current stage. We need to consider the **as many details as possible**. After this stage, we should be able to deliver an early version of the product.

In this project, I created 4 classes.

- Loader: It reads both image files and PDF files, and creates a mask. The mask is a 2-dimension matrix which contains only 2 value. "255" represents a pixel. The rest is "0".
- Extractor: It creates the regions from the sets of connected pixels. What's more, it removes the huge or little regions, only keeps the regions of middle size.
- Cropper: It crops all the regions in a file.
- Judger: It judges whether a region contains a signature based on the ratio of its height and width and the ratio of pixels.

More details, such as **unit tests**, are presented at my GitHub repository, [signature_detection](https://github.com/EnzoSeason/signature_detection).

Since the product is created, the next problem is how to deliver it. There are two ways.

1. create a package and pull it to a public or private repository
2. send the files to the client directly

It depends on **the scale of the project** and **the scale of the teams**.

If it's just a demo and created by a single developer, sending the files directly is more efficient. It's a very common scenario for an innovation project.

However, if the project is long-term maintained and shared with other developers, making a package is more appropriate.

The package of signature detection is on [PyPI](https://pypi.org/project/signature-detect/).

### Create a backend API

The backend API is a web application. It takes cares of

- run the product we've created
- save the data before and after running the product
- send the data to the frontend

Since I used Python, I chose Django as my web application framework. MySQL is my database. I deployed them using containers. more specifically, I used docker-compose. The advantage of docker-compose is

- **easy to switch** between dev mode and production mode
- **easy to extend**. My Django application and my database are run in different containers in the same network. If we need another service, such as Redis for caching, we run another container in this network
- **easy to upgrade**. If the application becomes bigger and bigger, we need more advanced features, such as CD/CI, monitoring, container-orchestration, etc, to help us maintain the application. It's easy to upgrade.

More details are presented in another article on my website, [Django Set up](https://seasonliu.com/station/topics/seasonliu/api-setup).

### Create a frontend UI

Finally, It's the last stage. We've created the product and prepared the application to run it. Now, we need an interface for users. It's the bridge between our product and the users.
For the signature detection project, the frontend should allow users

- to upload the file
- to get the detection results
- to create, remove or update the results.

I feel the frontend development is more difficult than the backend for an innovation project. Because the interaction is much more complicated for an innovation project than a normal one. It usually requires deals with images, uses multiply web APIs, on different devices.

I'm not saying that the backend is simple. The challenge of the backend is the high concurrency, which is after the early stage. However, the early stage is essential for an innovation project. It decides whether the project can survive.

So, my suggestion is to pay more attention to **the Frontend and the package** than the backend when we run an innovation project.

### Conclusion

We've talked about running an innovation project. **The ideas and the presentation** are the core. 

To get the best idea, we need to think **widely and deeply**. To have a great presentation, we need to master advanced frontend knowledge, which evolutes very fast.

Last but not least, we need to develop **quickly**. The market changes all the time. Our project needs to evolute with the market. 

Hope you enjoy it and see you next time.

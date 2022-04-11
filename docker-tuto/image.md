## Image

### Important concepts

1. Image layers

    Docker doesn't store entire image in a bundle. It stores each layer of an image, only once.

2. union file system

    A same image layer can be shared in different images.

3. container

    A container just a single read/write layer on the top of image. It's usually very small.

### Get an image

`docker pull <image>`

### Name

Image doesn't have name. To identify an image, we use:

`<user>/<repo>:<tag>`

An Image can have multiple tags.

### Build an image

`Dockerfile` is an instruction of building an image.

`docker image build -t <name> PATH`

If `PATH` is `.`, it means we build image based on the `Dockerfile` in the current repo.
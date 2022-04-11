## Django Set up

### Previously

[Previously](https://github.com/EnzoSeason/study-notes/blob/main/seasonliu/frontend-setup.md), we have set up the front-end, which includes configuring server, domain and Nginx.

This article will talk about setting up API powered by Django and DRF(Django Rest Framework).

API is deployed by `docker compose`. I will present how to create `docker-compose.yml` and `DockerFile`.

### `docker-compose.yml`

API contains, at least, 2 parts, **database** and **web application**. 

I choose `MySQL` as database and create a django application. So, `docker-compose.yml` is as followed.

```yml
version: "3.9"

services:
  db:
    image: mysql
  
  django_app:
    depends_on:
      - db
```

I use offical `MySQL` docker image. To initialize a mysql database, we need.
- create `root` password and database
  
  It's required by the [offical image](https://hub.docker.com/_/mysql).

- create a database and expose the port `3306`

   The database is connected and used by web application


- mount the data and the configuration

   Once the docker container is destroyed, all the data inside will be cleared. We need to mount the data and the configuration on the host machine using `volumes`.

So, `docker-compose.yml` becomes:

```yml
version: "3.9"

services:
  db:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: my-password
      MYSQL_DATABASE: my-database
    volumes:
      - mysql_data:/var/lib/mysql
      - mysql_config:/etc/mysql
  
  django_app:
    depends_on:
      - db

volumes:
  mysql_data:
  mysql_config:
```

Now, let's set up web application. We assume that the image of application is saved in the docker hub, called `repo/my-api`. As setting the database, we use the docker hub image.

Next, we copy all the codes, which is under the folder `django_app`, into the container with **bind mounting**.

Finally, we expose a port for nginx.

```yml
django_app:
  image: repo/my-api
  volumes:
    - ./django_app:/code
  ports:
    - 8000:8000
  depends_on:
    - db
```

The full `docker-compose.yml` is as followed.

```yml
version: "3.9"

services:
  db:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: my-password
      MYSQL_DATABASE: my-database
    volumes:
      - mysql_data:/var/lib/mysql
      - mysql_config:/etc/mysql

  django_app:
    image: repo/my-image
    volumes:
      - ./django_app:/code
    ports:
      - 8000:8000
    depends_on:
      - db

volumes:
  mysql_data:
  mysql_config:
```

Since we use Django as the web application, there are some difference between `dev` mode and `production` mode. 

I use `docker-compose.override.yml` to override the configuration for `dev` mode, and `docker-compose.prod.yml` for `production`.

In `dev` mode, we **build the image locally** and push it to the docker hub. Besides, we use `runsever` to start the application.

```yml
## docker-compose.override.yml
version: "3.9"

## dev config
services:
  django_app:
    build: "./django_app"
    command: python manage.py runserver 0.0.0.0:8000 --settings=core.settings.local
```

To build the image, run `docker-compose build`.

To run the application in the `dev` mode, launch `docker-compose up`.

In `production` mode, we do NOT build the image, and we use `gunicorn` to start the application.

```yml
## docker-compose.prod.yml
version: "3.9"

## prod config
services:
  django_app:
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

To run the application at background, launch:

```command
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### DockerFile

`DockerFile` describes how the image is built. We can followed the [offical example](https://docs.docker.com/language/python/build-images/).

I use `python` as the base image. It's big, but it contains all the tools I need. We can choose `slim` version. Then, we need add extra package by ourselves.

Since I use `opencv` in the project, I need to install its `c++` codes. [This DockerFile](https://github.com/janza/docker-python3-opencv/blob/master/Dockerfile) presents all the packages needed.

```DockerFile
FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/build

## set extra env variable
## ENV OPENCV_VERSION="4.5.1"

## install extra packages
## RUN apt-get -qq update \ 
## && apt-get -qq install -y --no-install-recommends ...

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
```

Now, run `docker-compose build` to build the image. Once the image is built, we can push it to the docker hub. Before that, we should [create a repo](https://docs.docker.com/docker-hub/repos/).

```command
docker tag <container> repo/my-api
docker push repo/my-api
```

### Initialize Django Application

Creating a django application is simple. We should move under the `django_app` and run the CLI.

```command
cd django_app
docker-compose run django_app django-admin startproject core
```

Now, in the `core` folder, there is a `settings.py`. Remove it and create a folder called `settings`. Inside `settings`, create 3 files:
- `base.py`
- `local.py`
- `production.py`

> Replace `core.settings` by `core.setting.base` in other files, such as `manage.py`.

> In `wsgi.py`, replace `core.settings` by `core.setting.production`

As we discussed before, it's slightly different between `dev` mode and `production` mode. `local.py` and `production.py` are for these 2 modes. Both of them extends `base.py`.

> DO NOT commit `local.py` and `production.py` in git.

Django can't server static files in `production` mode. A commmon difference is, in `dev` mode, the static files are served by `runserver`, while, in `production` mode, they are served by the third party, such as **S3** of **AWS**.


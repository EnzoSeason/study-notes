## Plugins

### Sentry
#### install
We can use sentry to monitor our application.

To install sentry, we can download `zip` file on the server, then `unzip` it.

Then, ensure that docker is installed, go to the repo and run `./install.sh`

> sentry needs 4G of RAM at least.

After installation, run `docker-compose up -d`, then we can use sentry on `127.0.0.1:9000`

#### create a sentry project
In `settings` of sentry app, first, we create a **Team**, then, **Project**.

After than, sentry will tell us how to config our app to use sentry.

#### usage of sentry

Sentry can collect automatically:

- uncaught error
- error log (`logger.error`)

We can also send our custom message / error to sentry using `capture_message` / `capture_exception`.

Sentry creates many SDK for different frameworks and languages.

### REST framework

[official](https://www.django-rest-framework.org/)

It opens api to outside. To use it, we need:

1. install packages

2. config `settings.py` to enable REST framework and set the authentication

3. config `urls.py` to create:

   - `Serializers`

   - `ViewSets` of api pages

   - `Routers` of api

### Redis

Redis is cache tool.

Before starting, we need to install `redis` on the host.

Then install `django-redis`. [offical](https://github.com/jazzband/django-redis)

Follow the official docs to set up django-redis, then add middleware:

```python
## setting.py

MIDDLEWARE =[
    ...,
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    ...
]
```

The **order** is important. That means, for **each view**, django always,

1. searches it in the cache
2. do something common
3. update the cache

### Celery

Celery is a simple, flexible, and reliable **distributed system**. It’s a **task queue** with focus on real-time processing.

[official](https://docs.celeryproject.org/en/stable/getting-started/introduction.html#get-started)

#### Installation

We need to install `Celery` and its `Bundles`, such as `redis,auth, msgpack`

#### First step

[example](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps)

In this example, we create a simple task. We set `redis` as the broker, and we save the task results in redis

1. run a worker server

   To run it: `celery -A tasks worker --loglevel=INFO`

   That means we execute our app (`-A`), named `tasks` with the `worker`. `tasks` is the **name of the python file**.

2. call the task

   We create another script to call `add` function in `tasks.py`.

3. monitor the tasks

   We use [Flower](https://docs.celeryproject.org/en/stable/userguide/monitoring.html?highlight=flower#flower-real-time-celery-web-monitor) to monitor.

   After installing, run monitor of the `task`:

   - `celery -A tasks flower`

#### Celery with django

[official](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)

There are some custom settings for `recruitment` project:

```python
## recruitment/recruitment/celery.py

## set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('recruitment')
```

To make it work:

1. start redis:

   ```command
   redis-server
   ```

2. start the worker:

   ```command
   DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment worker --loglevel=INFO
   ```

3. start the monitor (optional):

   ```command
   DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment flower
   ```

#### Celery with django beat

[official](https://django-celery-beat.readthedocs.io/en/latest/)

This extension enables you to store the **periodic task schedule** in the **database**.

##### install

1. intall `pip install django-celery-beat`

2. add `django_celery_beat` into `INSTALLED_APPS` in `settings`

3. migrate database: `python manage.py migrate`

4. start beat

    ```command
    DJANGO_SETTINGS_MODULE=settings.local celery -A recruitment beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ```

    It tells beat to store **periodic task schedule** in the **database**. (`--scheduler django_celery_beat.schedulers:DatabaseScheduler`)

##### add Periodic Tasks

[doc](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html)

### Other plugins

- Django debug toolbar

- django-silk: analyze performance bottleneck

- haystack django: search

- django notifications

- django markdown editor

- simple UI: django Admin UI

- django-crispy-forms: forms UI

- django-simple-captcha
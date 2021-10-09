#  Development

# #  generate a back office of an existed database

It's common that we have a running back-end, and we need create new back office on it.

Django can easily generate a back office, which is connected to the existed database.

1. create a django project: `django-admin startproject backOffice`

2. set database config

   ```python
   #  settings/base.py
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'myDatabase',
            'USER': 'myUser',
            'PASSWORD': 'myPassword',
            'HOST': '127.0.0.1',
            'PORT': '5432'
       }
   }

   #  use DatabaseRouter to config which database to use
   DATABASE_ROUTERS = ['settings.router.DatabaseRouter']
   ```

   ```python
   #  settings/router.py

   class DatabaseRouter:
    route_app_labels = {'running'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'running'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'running'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        DO NOT migrate running database !
        """
        if app_label in self.route_app_labels:
            return False
        return True
   ```

3. generate `models.py`: `python manage.py inspectdb > models.py`

   [Integrating Django with a legacy database](https://docs.djangoproject.com/en/3.1/howto/legacy-databases/)

# #  Middleware

What is Middleware ? 

It's the hook that handles custom request / response, such as auth, safety block, log, buffer, monitoring, etc.

There are 2 ways to create middleware:

1. function

   ```python
   def simple_middleware(get_response):
       #  one-time config and init
       
       def middleware(request):
           #  codes exec for each request
           #  before the view is called
           
           response = get_response(request)
           
           #  codes exec for each request
           #  before the view is called
           return response
       
       return middleware
   ```

2. class

   ```python
   class SimpleMiddleware:
       def __init__(self, get_response):
           #  one-time config and init
           self.get_response = get_response
   
       def __ceil__(self, request):
           #  codes exec for each request
           #  before the view is called
   
           response = self.get_response(request)
   
           #  codes exec for each request
           #  before the view is called
           return response
   ```

The process of make a custom middleware:

1. create a middleware

2. register the middleware in setting

   `MIDDLEWARE` in `setting.py` est executed from top to bottom.

# #  i18n

Django can set i18n easily.

1. use i18n

    There are 2 ways

    - `_('')`: in `.py` file, import `from django.utils.translation import gettext_lazy as _`

    - `{% translate '' %}`: in `.html` template, use `translate keywork`


2. init `locale`: 

    create / update `locale` folder at the root of the project, and run :
    
        python manage.py makemessages -l <language_you_need>
    
    modify the `.po` file, then run

        python manage.py compilemessages

3. config setting:

    - enable `django.middleware.locale.LocaleMiddleware`

    - add `LOCALE_PATHS`

# #  Security
# # #  XSS Attack

Hacker saves js script into database using form. When the site **renders the data**, js script is executed.

To avoid this, use `render` method created by Django

# # #  CSRF Attack

Hacker creates another website and try to let superuser click on it. So that, he can get the auth of superuser.

To avoid that, add `CsrfViewMiddleware` of Django. It will create and check **csrf token** of each request.

# # #  SQL Injection Attack

Hacker adds extra SQL in the query of database.

To avoid that, DO NOT use raw SQL, such as `SELECT * FROM my_table WHERE name = %s' % name`

# #  Media: upload files

# # #  upload to server

1. cofig media path

    ```python
    #  settings/base.py

    MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
    MEDIA_URL = '/media/'
    ```

2. add url

    ```python
    #  recruitment/urls.py

    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    ```

3. add FileField in model

    ```python
    #  models.py

    #  picture will be saved at /media/images
    picture = models.ImageField(
        upload_to='images/', 
        blank=True, 
        verbose_name=_('picture')) 
    
    #  attachment will be saved at /media/file
    attachment = models.FileField(
        upload_to='file/', 
        blank=True, 
        verbose_name=_('cv'))
    ```

    migrate the database.

4. add `picture` and `attachment` into `class ResumeAdmin` in `admin.py`

# # #  upload to cloud (recommanded)

# #  Signal

Django includes a “signal dispatcher” which helps allow **decoupled applications** get notified when actions occur elsewhere in the framework.




## Basic

### init project

1. install anaconda

2. install django: `conda install django`

3. install django plugin in PyCharm

   preferences -> Project -> Python Interpreter

   use anaconda to create a project env, and install django plugin

4. create project: `django-admin startproject myProject`, then `cd myProject`

5. create database (par defalut: sqllite): `python ./manage.py migrate`

6. create superuser: `python ./manage.py createsuperuser`

7. run dev server: `python ./manage.py runserver`

### create App and Model

1. create App in Project: `python ./manage.py startapp myApp`

   A django project can have multiple Apps. All the Apps need to be registered in `setting.py` of the project.

   ```python
   INSTALLED_APPS = [
        ## other APPS
       'myApp'
   ]
   ```

2. create Model

   Model is a class. It is used to create the table in database.

   > Optional: In order to see the model in admin page, we need to register it into `admin.py` of App.

   ```python
   ## myApp/admin.py
   
   from myApp.models import myModel
   
   admin.site.register(myModel)
   ```

3. make migration: `python manage.py makemigrations`

4. migrate: `python manage.py migrate`
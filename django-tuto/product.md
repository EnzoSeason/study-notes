#  Product

# #  init a product

MVP (Minimum viable product) is the main product development strategy.
*minimum dev, maximum iteration.*

# #  database principles

- basic:

    - clear: the name of the tables, attributes must be clear

    - unique: one table for one use case, do not stock useless info

    - primary key: pk must be unique

- complete

    - complete: all the import data is saved

    - searchable: data has *created_date* and *updated_date*

    - identical: The same data should NOT be saved in different tables.

- extend:

    - split the text: long text can be stocked individually, like an extra k-v database

    - split the history: seperate the current data and historical data

    - add the index: index helps search.

    - DO NOT use JOIN: never search 2 or more table at one time

# #  LDAP user

1. install `django-python3-ldap`

2. config [setting.py](../recruitment/settings/base.py)

3. run `python .manage.py ldap_sync_users`

# #  import csv

Django can create **commands**. We use custom command to import csv.

1. put csv on the server

2. create file in folder: `management/commands`

3. create command: [import_candidates.py](../recruitment/interview/management/commands/import_candidates.py)

4. run command

   `python manage.py import_candidates --path /path/to/your/file.csv`

# #  Export csv

We can add **export csv** action to [admin page](../recruitment/interview/admin.py).

1. create export csv function

   The function reads data from database, and returns a http response with `content_type='text/csv'`

2. add the function into `actions` in `ModelAdmin`

# #  Logs

We can config **logs** in [setting.py](../recruitment/settings/base.py)

- formatters: config format of logs

- handlers: how to log

- logger: use handlers to write logs (root is a special logger)

We can make custom logger, too.

```python
import logging

logger = logging.getLogger(__name__)
logger.info('my log')
```

# #  env settings

We can create different env for different modes (dev, test, prod, etc)

1. create python package (a folder with `__init.py`), named `settings`

2. create `base.py` as base settings, and point to it

   ```python
   #  manage.py
   import os
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')
   ```

3. create `local.py`, `production.py`, which imports `base.py`

   ```python
   #  production.py
   from .base import *
   
   DEBUG = False
   ALLOWED_HOSTS = ["127.0.0.1"]
   ```
   
   put `local.py` in `.gitignore`

4. run server: `python manage.py runserver --settings=settings.local`



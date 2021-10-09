#  Django Unit Test

Django Unit Test extends `unittest` of Python. The common use case is as followed.

```python
#  <parent>/tests/test_myclass.py

from django.test.testcases import TestCase

class MyClassTestCase(TestCase):
    def test_my_func(self):
        #  do something to test the codes
        self.assertEqual(test_result, expected_result)
```

To run the test,

```command
docker-compose run django_app python run manage.py test
```

If there are special settings for unit test, we can add settings flag, `--settings=core.settings.unittest`.

To see the code coverage, we need to install the package `coverage`, and run the command

```
docker-compose run django_app coverage run manage.py test
docker-compose run django_app coverage report -i -m --skip-covered
```

I like skipping covered lines and errors.


# #  Mock

Making Mocks in Django is simple. We can use **decorators** on the functions.

- `@override_settings` can override the Django settings in the `settings.py` or `settings/<env>.py`.

- `@patch` is used to mock the **function in the class**. To make the unit tests easy, we should create classes.

   > The order of `@patch` and the order of **parameters** are important.

```python
#  <parent>/tests/test_myclass.py

from unittest.mock import patch
from django.test.testcases import TestCase

class MyClassTestCase(TestCase):

    @override_settings(SOME_SECRET="12345")
    @patch("SomeParentClass.SomeClass.second_func")
    @patch("SomeParentClass.SomeClass.first_func")
    def test_my_func(self, first_func, second_func):
        first_func.return_value = {}
        second_func = None
        #  do something to test the codes
        self.assertEqual(test_result, expected_result)
```


#  JSON

`json` package in python can easily serialize/deserialize between json and python object.

json | python data type
--- | ---
[] | list
{} | dict
"string" | str
123.45 | int / float
true/false | boolean
null | None

# #  Python data => json

`json.dumps`

```python
import json

d = dict(name='Bob', age=20, score=88)
json.dumps(d)

# # #  output # # # 
'{"age": 20, "score": 88, "name": "Bob"}'
```

# #  json => python data

`json.loads`

```python
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

#  {'age': 20, 'score': 88, 'name': 'Bob'}
```

# #  json <=> python class instance

Class instance => json, we can use `default` in `json.dumps`.

- create custom function to let `json.dumps` use
- use `__dict__` of the class instance.

```python
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

#  {"age": 20, "name": "Bob", "score": 88}

print(json.dumps(s, default=lambda obj: obj.__dict__))
#  {"age": 20, "name": "Bob", "score": 88}
```

json => class object, we can use `object_hook` in `json.loads`

```python
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
#  <__main__.Student object at 0x10cd3c190>
```
# CRUD

## [Document API](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/docs.html)

Action | Call | Description
--- | --- | ---
Create | `POST my_index/_doc {"user": "Jack"}` | Create a document (ID is auto genereted)
Index | `PUT my_index/_doc/1 {"user": "Jack"}` | Create / Remove and Create (version is increased) a document with the given id
Read |  `GET my_index/_doc/1` | Get a document
Delete | `DELETE my_index/_doc/1` | Delete a document

## Other APIs

API | Call | Description
--- | --- | ---
Create | `PUT my_index/_create/1 {"user": "Jack"}` | Create a document, throw an error if the document exists
[Update](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/docs-update.html) | `POST my_index/_update/1 {"doc": {"user": "Jack"}}` | Update a document, throw an error if the document doesn't exist
# CRUD

## The endpoints having `_doc`

Action | Call | Description
--- | --- | ---
Create | `POST my_index/_doc` | Create a document (ID is auto genereted)
Index | `PUT my_index/_doc/1` | Create / remove and create a document with the given id
Read |  `GET my_index/_doc/1` | Get a document
Delete | `DELETE my_index/_doc/1` | Delete a document

## Other endpoints

Action | Call | Description
--- | --- | ---
Create | `PUT my_index/_create/1` | Create a document, throw an error if the document exists
Update | `POST my_index/_update/1` | Update a document, throw an error if the document doesn't exist
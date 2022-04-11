# Relation

There are two ways to present the relation.

There is no strict rule to tell which method to use. It depends on the use cases.

- Embedded document

  It's **easy to read and write**, but the size of a document can be huge.

  > Attention: the max size of a document is 16 MB.

  It may **waste the space of storage** if there are duplication, and **waste the bandwidth** if we fetch the related collections which aren't uses.

- references

  use **ObjectId**.

  It's used when you want to fetch the data of a collection but don't want the data of its related collections.

  It can **reduce the size of a document** and **save the bandwidth**. However, you need multiple requests if you need the related collections.

## One to One

For example, a patient has one disease summary.

Usually, we use _Embedded document_ if there is no reason to split them.

## One to Many

For example, a question has many answers.

Usually, we use _Embedded document_ if there is no reason to split them.

## Many to Many

An author has many books, and a book has many authors.

Usually, we use _reference_ to split them.

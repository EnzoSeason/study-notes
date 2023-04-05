# Search

## Mechanism

There are 2 steps in the search: **Query** && **Fetch**

- Query: When the Coordinating node receives the request, it will ask some shards (e.g. 3 shards out of 6) for data. The selected shards will **sort documents** and return a list of `_id` of size.

- Fetch: The Coordinating node will reorder all the sorted `_id` list and return the result

## Sort

ES uses `doc_value` for sorting by **field** on documents. For example, sorting all the logs by creation data.

`doc_value` is a different index created along with **inverted index**.

## Pagination

ES returns **10** documents by default.

There are 2 parameters: `from` and `size`. ES will pick `0` to `from` documents from **each shard**, sort, and pick `0` to `size` documet. Therefore, either `from` or `size` is too big will affect the performance. The default value is `100000`

### search after API

It improves the performance of the pagination with limits:

- Don't support `from`

- Must add the **last result** of the previous search in the next search

- The sort must be defined before search, and it must be **unique**. Therefore, we usually add `_doc`.

### Scroll API

If we want to get **all the documents** of an index, we can use it.

Scroll API will create a **snapshot** on the index when it is called. Therefore, the documents indexed after Scrol API call won't be fetched.

## Lock

ES provides `if_seq_no` + `if_primary_term` as the lock for concurrent writing operation.

Besides, if ES is used as a log system while there has another database that provides `version`, we use set `?version=<version>&version_type=external` in the path as a lock.

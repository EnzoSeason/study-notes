# Search

## Mechanism

There are 2 steps in the search: **Query** && **Fetch**

- Query: When the Coordinating node receives the request, it will ask some shards (e.g. 3 shards out of 6) for data. The selected shards will **sort documents** and return a list of `_id` of size.

- Fetch: The Coordinating node will reorder all the sorted `_id` list and return the result
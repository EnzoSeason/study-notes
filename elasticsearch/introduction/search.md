# Search

Elasticsearh creates **[inverted index](https://www.elastic.co/guide/cn/elasticsearch/guide/current/inverted-index.html)** for searching. It helps search a term in all the documents.

Elasticsearch uses **Analyzer** to process the text to **terms**. Analyzer has:

1. Char filter

   It applies

   - remove html tags
   - mapping the characters (e.g. replace `a` by `b`)
   - pattern replace

2. Tokenizer

   It splits the text to **terms**. It chooses the delimiter, such as whitespace, `\W`, `;`, etc.

3. Token filter

   It handles the token, such as removing the stopword, applying lowercase, etc.

We can use `_analyze` API to play with it.

Usually, the same analyzer should be applied at index time and at search time, to ensure that the terms in the query are in the same format as the terms in the inverted index. Sometimes, though, it can make sense to use a different analyzer at search time, such as when using the edge_ngram tokenizer for autocomplete or when using search-time synonyms. [source](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-analyzer.html)

## Match Query vs Match Pharse Query

The relation of terms in Match Query is **OR**, while in Match Pharse Query is **and**.

In Match Pharse Query, the order of terms matters. We can get more results by increasing **slop**.
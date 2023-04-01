# Search

## Term search & Constant Score

Term is the **minimum unit** of the context.

ES will **not tokenize** term during the search.

For example, there are 3 indexes.

```json
POST /products/_bulk
{ "index": {"_id" : 1} }
{ "uid" : "QWE-2-OPJP", "name" : "iPhone" }
{ "index": {"_id" : 2} }
{ "uid" : "KHK-4-YNUI", "name" : "iPad" }
{ "index": {"_id" : 3} }
{ "uid" : "TUB-9-TYBUD", "name" : "Apple watch" }
```

And we term query the `name`.

```json
POST /products/_search
{
  "query": {
    "term": {
      "name": {
        // "value": "iPhone" Don't work since indexing has tokenized the word, and term search doesn't
        "value": "iphone"
      }
    }
  }
}
```

Since term search doesn't tokenize, we should search the **keyword**.

```json
POST /products/_search
{
  "query": {
    "term": {
      "name.keyword": {
        "value": "iPhone"
      }
    }
  }
}
```

Besides, **term search** supports **prefix search**, **wildcard search\***, **range query**, **exists query**.

```json
POST /products/_search
{
  "query": {
    "term": {
      "uid": {
        "value": "qwe"
      }
    }
  }
}
```

Sometime, we **don't need the score**, we can use **constance score** to let ES stop using `query `. Instead, ES will use the `filter` which applies the **cache** to improve the performance.

```json
POST /products/_search
{
  "query": {
    "constant_score": {
      "filter": {
        "term": {
          "name.keyword": "iPhone"
        }
      }
    }
  }
}
```

## Match Query

![match-query](./images/match-query-process.png)

## Bool Query

- Query: calculate the score
- Filter: do NOT calculate the score

![bool-query](./images/bool-query.png)

```json
POST /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "price": {
              "gte": 500
            }
          }
        }
      ],
      "should": [
        {
          "term": {
            "name.keyword": {
              "value": "iPhone"
            }
          }
        },
        {
          "term": {
            "name.keyword": {
              "value": "iPad"
            }
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}
```

The body can be **nested**. The level indicates the **priority**.

## Boosting query

`boosting` controls the **weight** of the term.

- `> 1`: positive impact, increase the weight
- `0 - 1`: positive impact, decrease the weight
- `< 0`: negative impact

For example, query the product of Apple, not the apple food.

```json
POST /products/_search
{
  "query": {
    "boosting": {
      "positive": {
        "match": {
          "context": "apple"
        }
      },
      "negative": {
        "context": "pie"
      },
      "negative_boost": 0.2
    }
  }
}
```

## Multi Match

Sometimes, we want to search by **different fields** in a query. Multi Match is created for it.

![multi-match](./images/multi-match.png)

- `best_fields` is the same as [dis_max](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/query-dsl-dis-max-query.html).

- `most_fields` uses extra fields to improve search results

```json
PUT /titles
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "english",
        "fields": {
          "std": {
            "type": "text",
            "analyzer": "standard"
          }
        }
      }
    }
  }
}

POST /titles/_bulk
{"index":{"_id":1}}
{"title":"My dog barks"}
{"index":{"_id":2}}
{"title":"There are a lot of barking dogs on the street"}

POST /titles/_search
{
  "query": {
    "multi_match": {
      "type": "most_fields",
      "query": "barking dogs",
      "fields": [
        "title", // This field is analysed by `english`. Both docs have the same terms, `dog` and `bark`.
        "title.std" // This field is analysed by `standard`, it keeps the orginal terms.
      ]
    }
  }
}
```

- `most_fields` can apply `and` operation. We use `cross_fields` for that.


## Function Score

We can apply functions to the calcation of score.

For example, we have 3 documents with the same title but different votes.

```json
POST /blogs/_bulk
{"index":{"_id":1}}
{"title":"test", "vote":0}
{"index":{"_id":2}}
{"title":"test", "vote":100}
{"index":{"_id":3}}
{"title":"test", "vote":10000}
```

We can **multiply the `vote` to the score** which will change the hits order.

```json
POST /blogs/_search
{
  "query": {
    "function_score": {
      "query": {
        "multi_match": {
          "type": "best_fields", 
          "query": "test",
          "fields": ["title"]
        }
      },
      "functions": [
        {
          "field_value_factor": {
            "field": "vote"
            "modifier": "log1p", // function applied on `vote`
            "factor": 5 // factor of the modifier
          }
        }
      ],
      "boost_mode": "sum" // default is multiply, now is sum
    }
  }
}
```

We can return a random order of a list of blog. What's more, we use `seed` to make the order won't be changed for the same user.

```json
POST /blogs/_search
{
  "query": {
    "function_score": {
      "random_score": {
        "seed": 314159265352
      }
    }
  }
}
```
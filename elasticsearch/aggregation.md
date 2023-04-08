# Aggregation

Aggregation is an **attribute** of Search API.

```json
POST employees/_search
{
    "size": 0 // Since we don't need the items
    "aggs": {
        "max_salary": {
            "max": {
                "field": "salary"
            }
        },
        "min_salary": {
            "min": {
                "field": "salary"
            }
        },
    }
}
```

## Bucket

It can split the data into different buckets

```json
POST employee/_search
{
    "size": 0,
    "aggs": {
        "age_buckets": {
            "terms": {
                "field": "age",
                "size": 3
            }
        }
    }
}
```

## Nested aggregation

We can put an aggregation under another one.

```json
POST employees/_search
{
    "size": 0 // Since we don't need the items
    "aggs": {
        "job_buckets": {
            "terms": {
                "fields": "job.keyword"
            },
            "aggs": {
                "senior_employees": {
                    "top_hits": {
                        "size": 3,
                        "sort": [
                            {
                                "age": {
                                    "order": "desc"
                                }
                            }
                        ]
                    }
                }
            }
        }
    }
}
```

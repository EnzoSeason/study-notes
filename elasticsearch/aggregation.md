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

## Pipeline aggregation

Apply functions on the results of aggregation.

```json
POST employees/_search
{
    "size": 0 // Since we don't need the items
    "aggs": {
        "jobs": {
            "terms": {
                "fields": "job.keyword"
            },
            "aggs": {
                "avg_salary": {
                    "avg": {
                        "field": "salary"
                    }
                }
            }
        },
        "min_salary_by_jobs": {
            "min_bucket": { // pipeline function
                "bucket_path": "jobs>avg_salary" // bucket_path indicates it's a pipeline aggregation
            }
        }
    }
}
```

## Query + Aggregation

`Query` gives a **range** for aggregation result.

```json
POST employees/_search
{
    "size": 0,
    "query": { // the employee should be over 30 years old.
        "range": {
            "age": {
                "gte": 30
            }            
        }
    },
    "aggs": {
        "max_salary": {
            "max": {
                "field": "salary"
            }
        }
    }
}
```
# Data Pipeline

Data pipelines move data from one place to another. They pass **data packets** one by one.

The key considerations for designing a data pipeline are:
- Latency: 
- throughout: How much data can be fed into the pipe per unit of time.

## Stage

1. Data Extraction: extract data from one source or multiples

2. Data Ingestion: ingest data into the pipeline

3. Data Transformation

4. Data Loading: load data into the destination

5. Scheduling or Triggering

6. Monitoring

7. Maintaining and Optimization

## Monitoring keys

- Lantency

- Throughput

- Warnings, errors, and failures: from network, source, destination, etc

- Utilization rate: How fully the resource are used by the pipeline.

- Logging and alerting


## Performance

There are some key points impact the performance of the pipeline

- unbalanced load

    Some stages cost more time to process than others. It will lower the performance of the entire pipeline.

    Solution: Parallelize the workers for the heavy step.

-  stage synchronization

    The data flows to one stage to another won't ber smooth all the time.

    Solution: put an I/O buffer between the stages. It will regulate the flow, improve the throughout, distribute loads on parallelized stages.

## Batch vs Streaming

Batch pipelines:

- operate on the batch data

- could running periodically

- could be initiated by the data size or other triggers

- focus on **accurancy**, not **latency**

Streaming pipelines:

- ingest data in a rapid succession (e.g. credit card transactions, social media events)

- for real-time results

- events need to be processed when they happened

- events can be loaded to the storage

- users can publish/subscribe to the event steam


### Lambda Architecture

It combines batch and streaming data. It balances the accurancy and latency.

- batch data -> batch layer -> Serving layer

- streaming data -> speed layer -> Serving layer

## Modern data pipeline features

- Automation: Pipeline is fully automated

- Ease of use: ETL rule recommendations

- Drag-and-Drop UI

- Transformation support: enable complex calculations

- Security and compliance: Data encryption and Compliance (GDPR, HIPAA, etc) 
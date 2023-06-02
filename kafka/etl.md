# ETL

ETL stands for: Extraction, Transformation, and Loading.

## Extraction

The data source can be:

- paper
- web
- audio/video
- finanical reports
- transactions
- social media
- weather
- IoT
- ...

There are some use cases

- Integrating disparated structured data sources via APIs

- Capaturing events via APIs

- Monitoring with edge computing


## Transformation

Transformation includes

- Data Typing: (e.g. typing a record of CSV into a `UserData`)
- Data structuring (e.g. json file to DB table)
- Anonymizing, encrypting
- Cleaning
- Normalizing
- Filtering, sorting, aggregating
- Joining data source

### Schema-on-read vs Schema-on-write

Schema-on-read **predefines schema** while schema-on-write doesn't.

## Loading

The following aspects should be considered while designing loading.

### Full vs Increamental

Full loading loads an initial history into a database.

Increamental loading **inserts** data.

### Scheduled vs On-demand

### Batch vs Streaming

In between, we have micro-batch loading.

### Push vs Pull

### Parallel vs Serial




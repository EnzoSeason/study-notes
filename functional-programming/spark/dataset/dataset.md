# Dataset

Dataset

- It's a **typed** distributed collections of data

- It unifies the APIs of **dataframe** and **RDD**.

- It needs **structured data**.

Dataframe is a dataset.

```scala
type Dataframe = Dataset[Row]
```

Dataset is a compromise between **dataframe** and **RDD**.

- Dataset has **type information** while dataframe doesn't.
- Dataset gets more optimization of performance while RDD doesn't.

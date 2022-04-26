# Data frame

A data frame is **a collection of columns**. It is similar to a table in spreadsheets or SQL.

- Columns should be **named**.

- Data stored can be different types.

- Each data column should contain **the same number of data items**, even some of those are missing.

## Tibble

Tibbles are like **steamlined data frames**.

- Never change the **data types of the input**
- Never change the **names of the your variables**.
- Never create row names
- Make printing easier

## Tidy data (R)

It's a way of **standardizing the organization of data** within R.

- Variables are organized into columns.
- Observations are organized into rows.
- Each value must have its own cell.

## Basic functions in R to work with a data frame

- `head()`: return the first 6 rows of a data frame

- `str()`: return the structure of a data frame

- `colname()`: return the column names of a data frame

- `mutate()`: manipulate the data frame, like adding a new column.

## Data cleaning

Cleaning functions help you **preview and rename data** so that it’s easier to work with.

- `skim_without_charts()`: return a summary of a data frame

- `glimpse()`: return a transposed data frame. (rows to columns, columns to rows)

- `select()`: include or exclude a column

- `rename()`: rename a column name

- `rename_with()`: rename all column names. It's usually worked with `toupper` or `tolower`.

- `clean_names()`: ensure that there's only **charactors, numbers and underscores** in the names.

## Organizing data

Organizational functions help you **sort, filter, and summarize** your data.

Usually, they work with the **pipe**.

- `arrange()`: sort the data

  ```r
  # sort the data by level
  raw_data %>% arrange(level)
  ```

- `group_by()`:

  ```r
  # find the mean income of each year
  raw_data %>% group_by(year) %>% drop_na() %>% summarize(mean_income = mean(income))
  ```

- `filter()`:

  ```r
  # find the data of 2020
  raw_data %>% filter(year == "2020")
  ```

## Transforming data

Transformational functions help you **separate and combine data**, as well as **create** new variables.

- `separate()`: separate a column into multiple

  ```r
  separate(employee, name, into=c("first_name", "last_name", sep=" "))
  ```

- `unite()`: merge columns

  ```r
  unite(employee, "name", first_name, last_name, sep=" ")
  ```

- `mutate()`: add new columns

  ```r
  employee %>% mutate(year_salary=month_salaire * 12)
  ```

## Bias function

The bias function **compares the actual outcome of the data with the predicted outcome** to determine whether or not the model is biased.

It calculates **the average difference** between the actual and predicted values

```r
bias(actual_data, predicted_data)
```

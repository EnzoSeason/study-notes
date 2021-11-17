# SQL

SQL can

- handle huge amounts of data
- be adapted and used with multiple database programs
- offers powerful tools for cleaning data.

Analysts can use SQL and spreadsheets to perform arithmetic, use formulas, and join data.

Standard SQL works with a majority of databases and requires a small number of syntax changes to adapt to other dialects.

Data stored in a SQL database is useful to a project with multiple team members because they can:

- access the data at the same time

- use SQL to interact with the database program

- track changes to SQL queries across the team.

## Spreadsheet vs SQL

| Spreadsheet                                          | SQL                                                                |
| ---------------------------------------------------- | ------------------------------------------------------------------ |
| Smaller data sets                                    | Larger datasets                                                    |
| Enter data manually                                  | Access tables across a database                                    |
| Create graphs and visualizations in the same program | Prepare data for further analysis in another software              |
| Built-in spell check and other useful functions      | Fast and powerful functionality                                    |
| Best when working solo on a project                  | Great for collaborative work and tracking queries run by all users |

## Basic data cleaning

1. Inspect the column

   The keywords, `DISTINCT`, and the functions, `MAX, MIN, LENGTH` help us to inspect the column.

2. Fill in the missing data

   After inspecting the data, we can use `UPDATE` syntax to fill in the missing data

3. Removing the outliers

   We can either `DELETE` or `UPDATE` the outliers.

4. Ensuring consistency

   We use `TRIM` to remove the extra space.

## Advanced data cleaning

- `CAST`: convert the data type

  For exemple, `CAST(price AS FLOAT64)`.

  It converts the data type of `price` to `FLOAT64`

- `CONCAT`: concatenate the strings

- `COALESCE`: return non-null value

  For exemple, `COALESCE(product, product_code) AS product_info`.

  If `product` is null, it will return `product_code` instead.

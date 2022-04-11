## SQL

### Capitalization and case sensitivity

With SQL, capitalization usually **doesn’t matter**. The only time that capitalization does matter is when it is inside quotes.

To write SQL queries like a pro:

- use all caps for clause starters (e.g., SELECT, FROM, WHERE, etc.).

- Functions should also be in all caps (e.g., SUM())

- Column names should be all snake_case.

- Table names should be in camelCase.


### Comments as reminders

Use `--` or `/* */`

```sql
/*
Date: November 10, 2021
Author: Jijie LIU
*/
SELETE
    dummy_key, -- It's another comment
FROM
    tableMagic
```
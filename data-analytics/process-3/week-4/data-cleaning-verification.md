# Data cleaning verification

Verification and reporting are the next steps for a data analyst after the data is cleaned. 

Verification is a process to confirm that a data cleaning effort was well-executed and the resulting data is accurate and reliable.

The first step in the verification process is to compare cleaned data with the original, uncleaned dataset and compare it to what is there now.

It involves:

- rechecking your clean dataset
- doing some manual clean ups if needed
- taking a moment to sit back and really think about the original purpose of the project.

  - Consider the business problem

    You mush ensure that syour data will actually make it possible to solve your business problem.

  - Consider the goal

    If the goal of getting this feedback is to make improvements to that product?

    Whether the data you've collected and cleaned will actually help your company achieve that goal?

  - Consider the data

    That means thinking about where the data came from and testing your data collection and cleaning processes.

## Common problems

- **Sources of errors**: Did you use the right tools and functions to find the source of the errors in your dataset?

- **Null data**: Did you search for NULLs using conditional formatting and filters?

- **Misspelled words**: Did you locate all misspellings?

- **Mistyped numbers**: Did you double-check that your numeric data has been entered correctly?

- **Extra spaces and characters**: Did you remove any extra spaces or characters using the TRIM function?

- **Duplicates**: Did you remove duplicates in spreadsheets using the Remove Duplicates function or DISTINCT in SQL?

- **Mismatched data types**: Did you check that numeric, date, and string data are typecast correctly?

- **Messy (inconsistent) strings**: Did you make sure that all of your strings are consistent and meaningful?

- **Messy (inconsistent) date formats**: Did you format the dates consistently throughout your dataset?

- **Misleading variable labels (columns)**: Did you name your columns meaningfully?

- **Truncated data**: Did you check for truncated or missing data that needs correction?

- **Business Logic**: Did you check that the data makes sense given your knowledge of the business?

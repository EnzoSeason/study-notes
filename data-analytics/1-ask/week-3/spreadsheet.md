## Spreadsheets

Spreadsheet is used to **organize the data** and do the **calculation**.

The first step of organizing the data is to **sort and filter** data.

The calculation involves using **formulas and functions**.

### Data life cycle

let’s explore how spreadsheets relate to each phase of the data life cycle: **plan, capture, manage, analyze, archive, and destroy**.

- **Plan** for the users who will work within a spreadsheet by developing organizational standards.

  This can mean formatting your cells, the headings you choose to highlight, the color scheme, and the way you order your data points.

- **Capture** data by the source by connecting spreadsheets to other data sources, such as an online survey application or a database.

- **Manage** different kinds of data with a spreadsheet.

  This can involve **storing, organizing, filtering, and updating** information.

  Spreadsheets also let you decide **who can access the data**, how the information is shared, and how to keep your data safe and secure.

- **Analyze** data in a spreadsheet to help make better decisions.

  Some of the most common spreadsheet analysis tools include **formulas** to aggregate data or create reports, and **pivot tables** for clear, easy-to-understand visuals.

- **Archive** any spreadsheet that you don’t use often, but might need to reference later with built-in tools.

  This is especially useful if you want to store **historical data** before it gets updated.

- **Destroy** your spreadsheet when you are certain that you will never need it again, if you have better backup copies, or for legal or security reasons.

  Keep in mind, lots of businesses are required to follow certain rules or have measures in place to make sure data is destroyed properly.

### Fomulas

- **Absolute referencing**:

  `=$A$10` has absolute referencing for both the column and the row value.

  Absolute references will not change when you copy and paste the formula in a different cell.

  To easily switch between absolute and relative referencing in the formula bar, highlight the reference you want to change and press the **F4 key**.

- **Data range**: When you click into your formula, the colored ranges let you see which cells are being used in your spreadsheet.

#### Errors

- **#DIV/0** : divide a value in a cell by zero or by an empty cell.

  use `IFERROR(A1/B1, 'div error')` to avoid.

- **#N/A**: The data in your formula can't be found by the spreadsheet.

- **#NAME?**: A formula's name isn't recognized or understood.

- **#NUM!**: A formula's calculation can't be performed as specified by the data.

- **#REF!**: Cells being referenced in a formula have been deleted.

- **#VALUE!**: A general error indicating a problem with a formula or with referenced cells.


### Functions

The preset commands, such as `SUM`, `AVERAGE`,`MAX`, `MIN`.
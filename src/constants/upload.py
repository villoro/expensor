"""
    upload data related constants
"""

INSTRUCTIONS_P1 = """## Format of data to upload
You can upload your data using an ```Excel file (.xlsx)``` which should at least have 4 sheets:
* **trans_m:** all transactions made
* **trans_categ:** categories present in the transactions
* **liquid_list:** accounts where money is stored
* **liquid_m:** list with money avaiable in every account through every month

All columns names **MUST** be exactly equal as the examples below. You can use the 
[sample_data](https://github.com/villoro/expensor/blob/master/sample_data/data.xlsx)
file as a template

For all the  dates columns is better to use reversed order (**YYYY/MM/DD**).

### trans_m
This sheet should at least have the following columns:"""

INSTRUCTIONS_P2 = """It is important to notice that **incomes** have **positive**
 amount while **expenses** are **negative**.

### trans_categ
This sheet should be a list of all categories present in the transactions table. It needs
 those columns:
* **Name:** name of the category
* **Type:** _Expenses_ / _Incomes_
* **Color name:** name of the color
* **Color Index:** index of the color"""

INSTRUCTIONS_P3 = """The names and index used for colors can be found here
 [Android Colors](https://material.io/design/color/the-color-system.html#tools-for-picking-colors).

### liquid_list
This sheet should be a list of all accounts where you store liquid.
 It should have these three columns:
* **Name:** name of the account
* **Liquidity level:** this level states how easy it is to get that money (low levels mean easy)
* **Liquidity name:** name to be used for that level"""

INSTRUCTIONS_P4 = """### liquid_m
In this sheet the program is expecting a **Date** column and one column
 for each account in the ```liquid_list``` sheet."""

INSTRUCTIONS_ALL = [INSTRUCTIONS_P1, INSTRUCTIONS_P2, INSTRUCTIONS_P3, INSTRUCTIONS_P4]

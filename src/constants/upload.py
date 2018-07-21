"""
    upload data related constants
"""

INSTRUCTIONS_P1 = """# Format of data uploaded
You can upload your data using an **Excel file (.xlsx)** which should at least have 3 sheets:
* **liquid_list**
* **liquid_m**
* **trans_m**

All columns names **MUST** be exactly equal as the examples below. You can use the [sample_data](https://github.com/villoro/expensor/blob/master/sample_data/data.xlsx) file as a template

For all the  dates columns is better to use reversed order (**YYYY/MM/DD**).

## liquid_list
This sheet should be a list of all accounts where you store liquid. It should have these three columns:
* **Name:** name of the account
* **Liquidity level:** this level states how easy it is to get that money (low levels mean easy)
* **Liquidity name:** name to be used for that level"""

INSTRUCTIONS_P2 = """

## liquid_m
In this sheet the program is expecting a **Date** column and one column for each account in the **liquid_list** sheet."""


INSTRUCTIONS_P3 = """## trans_m
This sheet should at least have the following columns:"""

INSTRUCTIONS_P4 = """It is important to notice that **incomes** have **positive** amount while **expenses** are **negative**."""

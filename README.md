# Expenses Visualization App (ExpensOR)

This is a [dash](https://plot.ly/products/dash/) app that allows users to visualitze their expenses and/or incomes.

![Demo](images/demo.gif)

## Usage
Users can upload their on own data which should be an **Excel file (.xlsx)** which should at least have the following columns:

| Date       | Amount | Category |
|------------|--------|----------|
| 2017/01/01 | -500   | Rent     |
| 2017/02/01 | -500   | Rent     |
| 2017/03/01 | -500   | Rent     |
| 2017/01/01 | 1150   | Salary   |
| 2017/02/01 | 1250   | Salary   |

It is important to notice that **incomes** have **positive** amount while **expenses** are **negative**.

It is better if dates are in reversed order (**YYYY/MM/DD**). In the future user should be able to specify a custom date format.

## Install
1. Download the code 

    ```git clone https://github.com/villoro/expensor.git```

2. Install requirements

    ```pip install -r requirements.txt```
    
3. Run the app

    ```
    cd src
    python index.py
    ```
    
__* Note:__ The app is only tested in **python 3**. It might not work with python 2. 

## Authors
* [Arnau Villoro](villoro.com)

## License
The content of this repository is licensed under a [MIT](https://opensource.org/licenses/MIT).

## Nomenclature
Branches and commits use some prefixes to keep everything better organized.

### Branches
* **f/:** features
* **r/:** releases
* **h/:** hotfixs

### Commits
* **[NEW]** new features
* **[FIX]** fixes
* **[REF]** refactors
* **[PYL]** [pylint](https://www.pylint.org/) improvements
* **[TST]** tests
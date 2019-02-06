# <img src="assets/logo.png" alt="expensor" width="48px"/> Expenses Visualization App (expensor)
[![Build Status](https://travis-ci.com/villoro/expensor.svg?branch=master)](https://travis-ci.com/villoro/expensor)
[![codecov](https://codecov.io/gh/villoro/expensor/branch/master/graph/badge.svg)](https://codecov.io/gh/villoro/expensor)

This is a [dash](https://plot.ly/products/dash/) app that allows users to visualitze their expenses and/or incomes.

It is possible to see a live demo here: [expensor_heroku](https://expensorpy.herokuapp.com/)

![Demo](images/demo.gif)

## Usage
You can upload your data using an ```Excel file (.xlsx)``` which should at least have the following columns:
* **Date.** it is advised to use reversed order (**YYYY/MM/DD**).
* **Amount.** the values for **incomes** should be **positive** while **expenses** should be **negative**.
* **Category.**

| Date       | Amount | Category |
|------------|--------|----------|
| 2017/01/01 | -500   | Rent     |
| 2017/02/01 | -500   | Rent     |
| 2017/03/01 | -500   | Rent     |
| 2017/01/01 | 1150   | Salary   |
| 2017/02/01 | 1250   | Salary   |

You can use the [sample_data](https://github.com/villoro/expensor/blob/master/sample_data/data.xlsx) file as a template.

## Install
1. Download the code 

    ```git clone https://github.com/villoro/expensor.git```

2. Install requirements

    ```pip install -r requirements.txt```

3. Run the app

    ```
    python src/index.py
    ```

__* Note:__ The app is only tested in **python 3**. It might not work with python 2. 

## Authors
* [Arnau Villoro](https://villoro.com)

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
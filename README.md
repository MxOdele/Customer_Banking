# Customer_Banking

<div align='center'>
    <img src='https://images.pexels.com/photos/6694543/pexels-photo-6694543.jpeg' height='300' title='The desk of someone calculating finances (image courtesy of Pexels)' alt='An image of a desk littered with banking and financial papers, money in neatly organized stacks, a caluclator, and a laptop, all implying a scene of calculating financial information'/>

*Customer Banking System*[^1]

## READ ME
</div>

## Table of Contents

* [Overview](#Overview)
* [Usage](#Usage)

---

## Overview

### *The assignment*

For our Week 3 Challange, we were tasked with completing three (3) of the provided files (`cd_account.py`, `savings_account.py`, and `customer_banking.py`) to create a functional customer banking system that would allow users to enter infomration about their accounts and see the interest earned over a specified number of months. The steps we were charged with completing were:

1. Importing the `Account` class from the `Account.py` file into the `savings_account.py` file
2. Completing the `create_savings_account` function by;
    * Creating an instance of the `Account` class and passing the balance and interest variables
    * Calculating interested earned
        * Using **0** as the interest rate *for initialization **only***
    * Updating the savings account by adding the interest earned
    * Passing the updated balance with the `set_balance` method of the `Account` class
    * Passing the interest earned with the `set_interest` method of the `Account` class
    * Returning the updated balance and interest earned
3. Importing the `Account` class from the `Account.py` file into the `cd_account.py` file
4. Completing the `create_cd_account` function by;
    * Creating an instance of the `Account` class and passing the balance and interest variables
    * Calculating interested earned
        * Using **0** as the interest rate *for initialization **only***
    * Updating the savings account by adding the interest earned
    * Passing the updated balance with the `set_balance` method of the `Account` class
    * Passing the interest earned with the `set_interest` method of the `Account` class
    * Returning the updated balance and interest earned
5. Importing the `create_savings_account` and `create_cd_account` functions from the `savings_account.py` and `cd_account.py` files, respectively, into the `customer_banking.py` file
6. Completing the `main` function with the following;
    * Prompt the user for the savings balance, interest rate, and month for maturity
        * Data types enforced by wrapping the `input` with `float()` or `int()`, where needed
    * Calling the `create_savings_account` function and passing the variables from the user
    * Printing out the interest earned and updated savings balance with the interest earned for the given months
    * Prompt the user for the CD balance, interest rate, and month for maturity
        * Data types enforced by wrapping the `input` with `float()` or `int()`, where needed
    * Calling the `create_cd_account` function and passing the variables from the user
    * Printing out the interest earned and updated CD balance with the interest earned for the given months
    * Calling the main function

### *Written in*

Python v3.10.13

### *Accessing the customer banking system

To access the customer banking system, simply download all four (4) `*.py` files in this repository (`Account.py`, `savings_account.py`, `cd_account.py`, and `customer_banking.py`) into one directory, then load the `customer_banking.py` file through your terminal.

---

## Usage

### *Walkthrough*

1. Enter the initial balance of your **Savings Account** when prompted
    * May be an integer or float
2. Enter the interest rate for your **Savings Account** when prompted
    * May be an integer or float 
3. Enter the months for maturing your **Savings Account** when prompted
    * **MUST** be an integer
4. Enter the initial balance of your **CD Account** when prompted
    * May be an integer or float 
5. Enter the interest rate for your **CD Account** when prompted
    * May be an integer or float 
6. Enter the months for maturing your **CD Account** when prompted
    * **MUST** be an integer



[^1]: Image courtesy of free source image site, <a href='https://www.pexels.com/photo/banknotes-and-calculator-on-table-6694543/' title='Link to Pexels listing for image'>Pexels</a>
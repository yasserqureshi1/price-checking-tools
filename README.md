# Price-Checking-Tools
Multiple scripts that return statistical data on different marketplaces for mainly sneakers. 

## Installation
Install the required dependencies using the following command in Command Prompt (Windows) or Terminal (Mac or Linux):
```
pip install -r requirements.txt
```

The following packages will be installed:
```
requests
json
bs4
numpy
```

## Introduction
The purpose of this repo is to return statistical data on the prices for a particular item on different marketplaces. 
This can be used to determine the best site(s) to sell or purchase items.

This repo contains scripts for the following sites:
- StockX
- GOAT
- eBay
- Depop

## How to use

These scripts can be run via the command line.
The general structure is as follows

#### Windows
```
python [script name] [argument 1] [argument 2]
```

#### Linux/Mac
```
python3 [script name] [argument 1] [argument 2]
```

With most of the tools, you will only need to pass 1 argument, with the exception of `eBayBot.py` which takes 2.
An example of how to pass arguments is shown below:
```
python StockXBot.py 'yeezy 350 creams'
```

For `ebayBot.py`, the first argument is whether you want sold prices or current prices with the second argument being the item.
As such the first argument should be passed either as `current` or `sold`.
An example is shown below:
```
python eBayBot.py current 'yeezy 350 creams'
```
including the single quotations around the item is important to the accuracy of your results.

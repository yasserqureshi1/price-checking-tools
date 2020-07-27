# Price-Checking-Tools
Multiple scripts that return statistical data on different marketplaces for mainly sneakers. This project can be made into a Discord bot to provide price data on different site. More sites may be arranged in the future - if you would like another site added, please let me know.

## Installation
You will require the following packages that can be installed using your package installer.
```
requests
json
bs4
```

## Introduction
The purpose of this repo is to return statistical data on the prices for a particular item on different marketplaces. This can be used to determine which site(s) may be the best platform to sell on and also gives a good estimate on how well the item is selling.

This repo contains scripts for the following sites:
- StockX
- GOAT
- eBay
- Depop
- BUMP

## How to Use:

There are two ways to use the scripts:
### 1. Individually
You can usually view the current listings and/or the sold listings. To do this you input the name of the item as a string to the class and it should return a statistical summary.

### 2. Together through the main.py script
Input the name of the item you want to search as a string.

## Further Improvements

- Scraping more items. Depop and eBay both scrape around 200 items. Bump scrapes only 40.
- For Depop checker, remove random price listing values (users put up listings for random prices as they want to receive offers)
- For GOAT checker, fails on some items

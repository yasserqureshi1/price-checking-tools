import requests
import json
import sys


HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}
PARAMS = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.22.1',
          'x-algolia-api-key': '6bfb5abee4dcd8cea8f0ca1ca085c2b3',
          'x-algolia-application-id': 'XW7SBCT9V6'}
URL = 'https://xw7sbct9v6-dsn.algolia.net/1/indexes/products/query'


def scrape_site(item):
    try:
        data = {"params": "query={}&hitsPerPage=20&facets=*".format(item)}
        html = requests.post(url=URL, headers=HEADERS, params=PARAMS, json=data)
        return json.loads(html.text)
    except Exception as e:
        print(e)
        return 'Exception'


def current_listings(output):
    deadstock_sold = output['hits'][0]['deadstock_sold']
    highest_ask = output['facets_stats']['lowest_ask']['max']
    highest_bid = output['hits'][0]['highest_bid']
    last_sale = output['hits'][0]['last_sale']
    lowest_ask = output['hits'][0]['lowest_ask']
    name = output['hits'][0]['name']
    retail_price = output['hits'][0]['searchable_traits']['Retail Price']
    sales_last_72 = output['hits'][0]['sales_last_72']
    print_values(name, retail_price, deadstock_sold, highest_ask, highest_bid, last_sale, lowest_ask, sales_last_72)
    return name, retail_price, deadstock_sold, highest_ask, highest_bid, last_sale, lowest_ask, sales_last_72


def print_values(name, retail_price, deadstock_sold, last_sale, lowest_ask, highest_ask, highest_bid, sales_last_72):
    print(name)
    print('Retail Price: ', retail_price)
    print('DS Sold: ', deadstock_sold)
    print('Last Sale: ', last_sale)
    print('Lowest Ask: ', lowest_ask)
    print('Highest Ask: ', highest_ask)
    print('Highest Bid: ', highest_bid)
    print('Sales in the last 72hrs: ', sales_last_72)


if __name__ == '__main__':
    output = scrape_site(sys.argv[1])
    if output != 'Exception':
        current_listings(output)

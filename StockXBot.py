# Clean up and make into class

import requests
import json


class StockXPriceChecker:
    def __init__(self, item):
        self.item = item
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}
        self.params = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.22.1',
                       'x-algolia-api-key': '6bfb5abee4dcd8cea8f0ca1ca085c2b3',
                       'x-algolia-application-id': 'XW7SBCT9V6'}
        self.data = {"params": "query={}&hitsPerPage=20&facets=*".format(item)}
        self.output = None

    def scrape_site(self):
        response = requests.post(url='https://xw7sbct9v6-dsn.algolia.net/1/indexes/products/query',
                                 headers=self.headers,
                                 params=self.params, json=self.data)
        self.output = json.loads(response.text)

    def current_listing_stats(self):
        deadstock_sold = self.output['hits'][0]['deadstock_sold']
        highest_ask = self.output['facets_stats']['lowest_ask']['max']
        highest_bid = self.output['hits'][0]['highest_bid']
        image = self.output['hits'][0]['media']['imageUrl']
        last_sale = self.output['hits'][0]['last_sale']
        lowest_ask = self.output['hits'][0]['lowest_ask']
        name = self.output['hits'][0]['name']
        release_date = self.output['hits'][0]['release_date']
        retail_price = self.output['hits'][0]['searchable_traits']['Retail Price']
        sales_last_72 = self.output['hits'][0]['sales_last_72']
        url = 'https://stockx.com/' + self.output['hits'][0]['url']

        print(name)
        print('Release Date: ', release_date)
        print('Retail Price: ', retail_price)
        print('DS Sold: ', deadstock_sold)
        print('Last Sale: ', last_sale)
        print('Lowest Ask: ', lowest_ask)
        print('Highest Ask: ', highest_ask)
        print('Highest Bid: ', highest_bid)
        print('Sales in the last 72hrs: ', sales_last_72)


if __name__ == '__main__':
    test = StockXPriceChecker('jordan 1 high court purple')
    test.scrape_site()
    test.current_listing_stats()

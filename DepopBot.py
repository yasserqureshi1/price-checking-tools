# Current Issue: removing useless data - i.e. people listing items for random prices (£1, £12345, £9999 etc.)

import requests as rq
import json
import statistics


class DepopPriceChecker:
    def __init__(self, item, proxies=None):
        self.item = item
        if proxies == None:
            self.proxies = {}
        else:
            self.proxies = proxies
        self.current_listings = []
        self.max = 0
        self.min = 0
        self.avg = 0
        self.std = 0
        self.no_list = 0

    def scrape_site(self):
        try:
            html = rq.get('https://webapi.depop.com/api/v1/search/?what=' + self.item.replace(' ', '%20') + '&country=gb&limit=200', proxies=self.proxies).text
            output = json.loads(html)

            for i in output['products']:
                price = i['price']['price_amount']
                self.current_listings.append(float(price))

        except:
            print('error')

        return

    def checker(self, price, std, avg):
        if price > 2*std + avg:
            return 0
        elif price < avg - 2*std:
            return 0
        else:
            return 1

    def summary_of_prices(self, data):
        self.max = max(data)
        self.min = min(data)
        self.avg = sum(data)/len(data)
        self.std = statistics.stdev(data)
        self.no_list = len(data)

    def print_data(self):
        self.scrape_site()
        self.summary_of_prices(self.current_listings)
        for item in self.current_listings:
            if self.checker(item, self.std, self.avg) == 0:
                self.current_listings.remove(item)

        print('Max: ', self.max)
        print('Min: ', self.min)
        print('Average: ', self.avg)
        print('Standard Deviation: ', self.std)
        print('Number of listings: ', self.no_list)


if __name__ == '__main__':
    test = DepopPriceChecker('yeezy 350', proxies={})
    test.print_data()


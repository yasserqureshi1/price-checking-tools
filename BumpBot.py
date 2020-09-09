# Current Issue: Lazy loading / infinite scroll

import requests as rq
from bs4 import BeautifulSoup
import statistics


class BumpPriceChecker:
    def __init__(self, item, proxies=None):
        self.item = item
        self.current_listings = []
        if proxies == None:
            self.proxies = []
        else:
            self.proxies = proxies

    def get_current_prices(self):
        try:
            url = 'https://sobump.com/search?q='
            html = rq.get(url + self.item.replace(' ', '%20'), proxies=self.proxies, timeout=3, verify=False).text
            soup = BeautifulSoup(html, 'html.parser')

            for item in soup.find_all('div', attrs={'class': lambda e: e.startswith('_2nKHUq_PMQN8oVVOxfpkmd') if e else False}):
                price = item.find('div', {'class': '_1x9zBkhxPTMCCPbDAx9sB_'}).text
                self.current_listings.append(float(price.replace('€', '').replace('£', '')))

                # Name of each listing
                #print(item.find('div', {'class': '_2Krx4zaOVq0LlSknff-rnF'}).text)

        except:
            print('Error occurred')
        return

    def summary_of_prices(self, data):
        print('Max: ', max(data))
        print('Min: ', min(data))
        print('Average: ', sum(data)/len(data))
        print('Standard Deviation: ', statistics.stdev(data))
        print('Number of listings: ', len(data))


# if __name__ == '__main__':
#     proxies = {}
#     item = 'yeezy qntm'
#
#     test = BumpPriceChecker(item)
#     test.get_current_prices()
#     test.summary_of_prices(test.current_listings)

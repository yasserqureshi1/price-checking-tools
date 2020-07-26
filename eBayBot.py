import requests as rq
from bs4 import BeautifulSoup
import statistics


class EbayPriceChecker:
    def __init__(self, item, proxy=None):
        self.item = item
        self.current_listings = []
        self.sold_listings = []
        self.sold_listing_dates = []
        if proxy == None:
            self.proxies = {}
        else:
            self.proxies = proxy

    def get_current_prices(self):
        try:
            url = ['https://www.ebay.co.uk/sch/i.html?_nkw=', '&_ipg=200']

            html = rq.get(url[0] + self.item.replace(' ', '+') + url[1], proxies=self.proxies).text
            soup = BeautifulSoup(html, 'html.parser')

            for product in soup.find_all('div', {'class': 's-item__wrapper clearfix'}):
                price = product.find('span', {'class': 's-item__price'}).text
                try:
                    self.current_listings.append(float(price.replace('£', '')))
                except:
                    price = price.replace(' to', '').replace('£', '')
                    price = price.split()
                    prices = [float(item) for item in price]
                    self.current_listings.append(statistics.mean(prices))
                print(product.find('h3', {'class': 's-item__title'}).text)
                print(price)
                print(' ')
        except:
            print('Error occurred')
        return

    def get_sold_prices(self):
        try:
            url = ['https://www.ebay.co.uk/sch/i.html?_nkw=', '&_ipg=200&rt=nc&LH_Sold=1']

            html = rq.get(url[0] + self.item.replace(' ', '+') + url[1], proxies=self.proxies).text
            soup = BeautifulSoup(html, 'html.parser')

            for product in soup.find_all('div', {'class': 's-item__wrapper clearfix'}):
                price = product.find('span', {'class': 's-item__price'}).text
                try:
                    self.sold_listings.append(float(price.replace('£', '')))
                except:
                    price = price.replace(' to', '').replace('£', '')
                    price = price.split()
                    self.sold_listings.append(statistics.mean([float(item) for item in price]))
                # date = product.find('span', {'class': 's-item__ended-date s-item__endedDate'}).text
                # self.sold_listing_dates.append(date)
                print(product.find('h3', {'class': 's-item__title'}).text)
                print(price)
                # print(date)
                print(' ')
        except:
            print('Error occurred')
        return

    def summary_of_prices(self, data):
        print('Max: ', max(data))
        print('Min: ', min(data))
        print('Average: ', sum(data) / len(data))
        print('Standard Deviation: ', statistics.stdev(data))
        print('Number of listings: ', len(data))


if __name__ == '__main__':
    test = EbayPriceChecker('yeezy zyon')

    # Current Listings
    test.get_current_prices()
    test.summary_of_prices(test.current_listings)

    # Sold Listings
    test.get_sold_prices()
    test.summary_of_prices(test.sold_listings)

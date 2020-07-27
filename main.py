from DepopBot import DepopPriceChecker
from BumpBot import BumpPriceChecker
from eBayBot import EbayPriceChecker
from GOATBot import GOATPriceChecker
from StockXBot import StockXPriceChecker


class PriceChecker:
    def __init__(self, item, proxies=None):
        if proxies == None:
            self.proxy = {}
        else:
            self.proxy = proxies
        self.item = item

    def main(self):
        try:
            print(' -- DEPOP PRICES -- ')
            test = DepopPriceChecker(self.item, self.proxy)
            test.print_data()

        except:
            print('Unable to retrieve Depop prices')

        print(' ')

        try:
            print(' -- BUMP PRICES -- ')
            test = BumpPriceChecker(self.item, self.proxy)
            test.get_current_prices()
            test.summary_of_prices(test.current_listings)

        except:
            print('Unable to retrieve Bump prices')

        print(' ')

        try:
            print(' -- EBAY PRICES -- ')
            test = EbayPriceChecker(self.item, self.proxy)
            print(' + Current Listings')
            test.get_current_prices()
            test.summary_of_prices(test.current_listings)

            print(' + Sold Listings')
            test.get_sold_prices()
            test.summary_of_prices(test.sold_listings)
        except:
            print('Unable to retrieve eBay prices')

        print(' ')

        try:
            print(' -- GOAT PRICES -- ')
            test = GOATPriceChecker(self.item)
            test.scrape_site()
            test.current_listing_stats()
        except:
            print('Unable to retrieve GOAT prices')

        print(' ')

        try:
            print(' -- STOCKX PRICES -- ')
            test = StockXPriceChecker(self.item)
            test.scrape_site()
            test.current_listing_stats()
        except:
            print('Unable to retrieve StockX prices')


if __name__ == '__main__':
    text = PriceChecker('yeezy zyon')
    print(text.main())

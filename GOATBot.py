import requests
import json


class GOATPriceChecker:
    def __init__(self, item):
        self.item = item
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}
        self.params = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.25.1',
                       'x-algolia-api-key': 'ac96de6fef0e02bb95d433d8d5c7038a',
                       'x-algolia-application-id': '2FWOTDVM2O'}
        self.data = {"params": "query={}&facetFilters=(status%3Aactive%2C%20status%3Aactive_edit)%2C%20("
                               ")&page=0&hitsPerPage=20".format(item)}
        self.output = None

    def scrape_site(self):
        try:
            response = requests.post(url='https://2fwotdvm2o-dsn.algolia.net/1/indexes/ProductTemplateSearch/query',
                                     headers=self.headers, params=self.params, json=self.data, timeout=3)
            self.output = json.loads(response.text)
        except:
            print('Error Occurred')

    def current_listing_stats(self):
        image = self.output['hits'][0]['picture_url']
        name = self.output['hits'][0]['name']
        new_lowest_price_cents = int(self.output['hits'][0]['new_lowest_price_cents'] / 100)
        maximum_offer = int(self.output['hits'][0]['maximum_offer_cents'] / 100)
        minimum_offer = int(self.output['hits'][0]['minimum_offer_cents'] / 100)
        url = 'https://www.goat.com/sneakers/' + self.output['hits'][0]['slug']
        used_lowest_price_cents = int(self.output['hits'][0]['used_lowest_price_cents'] / 100)
        want_count = self.output['hits'][0]['want_count']
        want_count_three = self.output['hits'][0]['three_day_rolling_want_count']

        print(name)
        print('NEW Lowest Price: ', new_lowest_price_cents)
        print('USED Lowest Price: ', used_lowest_price_cents)
        print('Highest offer: ', maximum_offer)
        print('Minimum offer: ', minimum_offer)
        print('Want count: ', want_count)
        print('Three day rolling count: ', want_count_three)


if __name__ == '__main__':
    test = GOATPriceChecker("yeezy qntm")
    test.scrape_site()
    test.current_listing_stats()

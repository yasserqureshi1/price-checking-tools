import requests
import json
import sys


HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}
PARAMS = {'x-algolia-agent': 'Algolia for vanilla JavaScript 3.25.1',
          'x-algolia-api-key': 'ac96de6fef0e02bb95d433d8d5c7038a',
          'x-algolia-application-id': '2FWOTDVM2O'}
URL = 'https://2fwotdvm2o-dsn.algolia.net/1/indexes/ProductTemplateSearch/query'


def scrape_site(item):
    try:
        data = {"params": "query={}&facetFilters=(status%3Aactive%2C%20status%3Aactive_edit)%2C%20()&page=0&hitsPerPage=20".format(item)}
        html = requests.post(url=URL, headers=HEADERS, params=PARAMS, json=data)
        return json.loads(html.text)
    except Exception as e:
        print(e)
        return 'Exception'


def current_listings(output):
    name = output['hits'][0]['name']
    new_lowest_price_cents = int(output['hits'][0]['new_lowest_price_cents'] / 100)
    maximum_offer = int(output['hits'][0]['maximum_offer_cents'] / 100)
    minimum_offer = int(output['hits'][0]['minimum_offer_cents'] / 100)
    used_lowest_price_cents = int(output['hits'][0]['used_lowest_price_cents'] / 100)
    want_count = output['hits'][0]['want_count']
    want_count_three = output['hits'][0]['three_day_rolling_want_count']
    print_values(name, new_lowest_price_cents, maximum_offer, minimum_offer, used_lowest_price_cents, want_count, want_count_three)


def print_values(name, new_lowest_price_cents, maximum_offer, minimum_offer, used_lowest_price_cents, want_count, want_count_three):
    print(name)
    print('NEW Lowest Price: ', new_lowest_price_cents)
    print('USED Lowest Price: ', used_lowest_price_cents)
    print('Highest offer: ', maximum_offer)
    print('Minimum offer: ', minimum_offer)
    print('Want count: ', want_count)
    print('Three day rolling count: ', want_count_three)


if __name__ == '__main__':
    output = scrape_site(sys.argv[1])
    if output != 'Exception':
        current_listings(output)

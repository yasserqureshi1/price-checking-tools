import requests as rq
import json
import statistics
import numpy as np
import sys


def scrape_site(item):
    current_listings = []
    try:
        #change country_code to your countries two letter code (eg. gb for great britain)
        country_code = 'gb'
        url = f'https://webapi.depop.com/api/v2/search/products/?what={item.replace(" ", "+")}&itemsPerPage=40&country={country_code}&sort=relevance'
        html = rq.get(url=url)
        output = json.loads(html.text)
        for i in output['products']:
            price = i['price']['priceAmount']
            current_listings.append(float(price))
        return current_listings
    except Exception as e:
        print(e)
        return 'Exception'


def clean_data(data):
    _25th = np.percentile(np.array(data), 20)
    _75th = np.percentile(np.array(data), 80)
    data = [x for x in data if _75th > x > _25th]
    return data


def summary_of_prices(data):
    try:
        print('Max: ', max(data))
        print('Min: ', min(data))
        print('Average: ', (sum(data) / len(data)).__round__(2))
        print('Standard Deviation: ', statistics.stdev(data).__round__(2))
        print('Number of listings: ', len(data))
    except ValueError:
        print('Not enough listings to calculate statistics')


if __name__ == '__main__':
    output = scrape_site(sys.argv[1])
    if output != 'Exception' and output != []:
        summary_of_prices(clean_data(output))
    else:
        print('Please check first argument variable')

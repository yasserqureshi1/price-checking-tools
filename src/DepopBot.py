import requests as rq
import json
import statistics
import numpy as np
import sys


def scrape_site(item):
    current_listings = []
    try:
        url = f'https://webapi.depop.com/api/v1/search/?what={item.replace(" ", "%20")}&country=gb&limit=200'
        html = rq.get(url=url)
        output = json.loads(html.text)
        for i in output['products']:
            price = i['price']['price_amount']
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
    print('Max: ', max(data))
    print('Min: ', min(data))
    print('Average: ', sum(data) / len(data))
    print('Standard Deviation: ', statistics.stdev(data))
    print('Number of listings: ', len(data))


if __name__ == '__main__':
    output = scrape_site(sys.argv[1])
    if output != 'Exception' and output != []:
        summary_of_prices(clean_data(output))
    else:
        print('Please check first argument variable')

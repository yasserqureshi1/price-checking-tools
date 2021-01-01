import requests as rq
from bs4 import BeautifulSoup
import statistics
import sys


def get_current_prices(item):
    current_listings = []
    try:
        url = 'https://sobump.com/search?q=' + item.replace(' ', '%20')
        html = rq.get(url=url)
        soup = BeautifulSoup(html.text, 'html.parser')

        for item in soup.find_all('div',
                                  attrs={'class': lambda e: e.startswith('_2nKHUq_PMQN8oVVOxfpkmd') if e else False}):
            print(1)
            price = item.find('div', {'class': '_1x9zBkhxPTMCCPbDAx9sB_'}).text
            current_listings.append(float(price.replace('€', '').replace('£', '')))
        return current_listings
    except Exception as e:
        print(e)
        return 'Exception'


def summary_of_prices(data):
    print('Max: ', max(data))
    print('Min: ', min(data))
    print('Average: ', sum(data)/len(data))
    print('Standard Deviation: ', statistics.stdev(data))
    print('Number of listings: ', len(data))


if __name__ == '__main__':
    output = get_current_prices(sys.argv[1])
    if output != 'Exception' and output != []:
        summary_of_prices(output)
    else:
        print('Please check first argument variable')
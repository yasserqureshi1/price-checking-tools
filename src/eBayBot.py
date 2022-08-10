import requests as rq
from bs4 import BeautifulSoup
import statistics
import sys


def get_current_prices(item):
    current_listings = []
    try:
        url = f'https://www.ebay.co.uk/sch/i.html?_nkw={item.replace(" ", "+")}&_ipg=200'
        html = rq.get(url=url)
        soup = BeautifulSoup(html.text, 'html.parser')
        for product in soup.find_all('div', {'class': 's-item__wrapper clearfix'}):
            price = product.find('span', {'class': 's-item__price'}).text
            try:
                current_listings.append(float(price.replace('£', '')))
            except:
                #replaces dollar sign and pound sign
                price = price.replace(' to', '').replace('£', '').replace(',', '').replace('$', '')
                price = price.split()
                prices = [float(item) for item in price]
                current_listings.append(statistics.mean(prices))
        return current_listings
    except Exception as e:
        print(e)
        return 'Exception'


def get_sold_prices(item):
    sold_listings = []

    try:
        #to use USA ebay replace .co.uk with .com
        base_url = 'https://www.ebay.co.uk'
        url = f'{base_url}/sch/i.html?_nkw={item.replace(" ", "+")}&_ipg=200&rt=nc&LH_Sold=1'
        html = rq.get(url=url)
        soup = BeautifulSoup(html.text, 'html.parser')

        for product in soup.find_all('div', {'class': 's-item__wrapper clearfix'}):
            price = product.find('span', {'class': 's-item__price'}).text
            try:
                sold_listings.append(float(price.replace('£', '')))
            except:
                price = price.replace(' to', '').replace('£', '').replace(',', '').replace('$', '')
                price = price.split()
                sold_listings.append(statistics.mean([float(item) for item in price]))
        return sold_listings
    except Exception as e:
        print(e)
        return 'Exception'


def summary_of_prices(data):
    print('Max: ', max(data))
    print('Min: ', min(data))
    print('Average: ', (sum(data) / len(data)).__round__(2))
    print('Standard Deviation: ', statistics.stdev(data).__round__(2))
    print('Number of listings: ', len(data))


if __name__ == '__main__':
    if sys.argv[1] == 'current':
        output = get_current_prices(sys.argv[2])
    elif sys.argv[1] == 'sold':
        output = get_sold_prices(sys.argv[2])
    else:
        print('Please check first argument variable')
        exit()

    if output != 'Exception' and output != []:
        summary_of_prices(output)
    else:
        print('Please check second argument variable') 
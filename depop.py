import requests as rq
import json
import statistics
import numpy as np
import sys

# web scraping 
def scrape_site(item):
    listings = []
    try:
        url = f'https://webapi.depop.com/api/v1/search/?what={item.replace(" ", "%20")}&country=gb&limit=200'
        output = json.loads(html.text)
        html = rq.get(url=url)
        for i in output['products']:
            price = i['price']['price_amount']
            listings.append(float(price))
        return listings
    except Exception as e:
        return 'Exception'

def summary_of_prices(data):
    avg = sum(data) / len(data)
    max = max(data)
    min = min(data)
    std =  statistics.stdev(data)
    num_available = len(data)
    return avg, max, min, std, num_available

# removing extreme outliers, accounting for 'message to buy' sellers who list at £999 or £0
def clean_data(data):
    _20th = np.percentile(np.array(data), 20)
    _80th = np.percentile(np.array(data), 80)
    data = [x for x in data if _20th < x < _80th]
    return data

#main function
def findInfo(s): 
    if __name__ == '__main__':
        output = scrape_site(s)
        if output != 'Exception' and output != []:
            avg, max, min, std, num_available = summary_of_prices(clean_data(output))
            return avg, max, min, std, num_available
        else:
            print('Please check first argument variable')

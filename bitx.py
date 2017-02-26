import requests 
import json
import time 
import datetime
import threading

frequencyInSeconds = 10

class BitXApi():
    def __init__(self):
        self.base_url = "https://api.mybitx.com/api/1/"
    def get_ticker(self):
        url = self.base_url + "ticker?pair=XBTZAR"
        response = requests.get(url)
        return response


def print_exchangerate():
    threading.Timer(frequencyInSeconds, print_exchangerate).start()
    api = BitXApi()
    response = api.get_ticker()    
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        timestamp = datetime.datetime.fromtimestamp(response_dict['timestamp']/1000)
        ask = response_dict['ask']
        bid = response_dict['bid']
        avg = (float(ask) + float(bid))/2
        print("%s Bid: R%s  Ask: R%s Avg: R%s" % (timestamp, bid, ask, avg))

print_exchangerate()





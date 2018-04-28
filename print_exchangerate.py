""" Print the live bitcoin price (bid/ask) in ZAR on the Luno bitcoin exchange every 10 seconds """

from luno_api import LunoApi
import threading
import json
import time 
import datetime

frequencyInSeconds = 10
def print_exchangerate():
    """ Prints the luno exchange rate to the console every x seconds """
    threading.Timer(frequencyInSeconds, print_exchangerate).start()
    api = LunoApi()
    response = api.get_ticker()    
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        timestamp = datetime.datetime.fromtimestamp(response_dict['timestamp']/1000)
        ask = response_dict['ask']
        bid = response_dict['bid']
        avg = (float(ask) + float(bid))/2
        print("%s Bid: R%s  Ask: R%s Avg: R%s" % (timestamp, bid, ask, avg))

print_exchangerate()
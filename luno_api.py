import requests 

class LunoApi():
    def __init__(self):
        self.base_url = "https://api.mybitx.com/api/1/"
    def get_ticker(self):
        url = self.base_url + "ticker?pair=XBTZAR"
        response = requests.get(url)
        return response








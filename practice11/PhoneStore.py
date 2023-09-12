import json
import re
import ssl
import urllib.request as req
import requests as req


class Store:
    def __init__(self):
        pass

    def getDataFromUrl(self):
        #ssl.create_default_context = ssl.
        res = req.get("https://api.retailrocket.ru/api/2.0/recommendation/popular/525a6e890d422d408c35c909/?&stockId=777&categoryIds=141&categoryPaths=&session=6417409d0c5b53eafb0c5d00&pvid=127344900361245&isDebug=false&format=json")
        datalist = []
        for i in json.loads(res.text):
            name = i["Model"]
            price = i["Price"]
            datalist.append([name, price])
        return datalist

    def recordToFile(self):
        with open("secondHalfyear/prak11/phonestore", "a") as file:
            for i in self.getDataFromUrl():
                file.write(
f"""
{i[0]} | {i[1]}
------------------------------
""")
            file.close()

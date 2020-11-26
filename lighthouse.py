
# importing the requests library
import requests
import json
import sys
from urllib.parse import urlsplit

def lighthouse_seo(test_url):
    #sys.stdout = open('output.txt', 'wt', encoding="utf-8")
    # api-endpoint
    URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key=AIzaSyBkurRgGEs3fI-T4eLZ6xTAvX2VTbiGN7s"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {
        'url': test_url,
        'category': ["seo", "performance", "accessibility", "best-practices"],
        'strategy': "desktop"
    }
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS, stream=True)
    # extracting data in json format
    data = r.json()
    #print(pprint.pprint(data["lighthouseResult"]["audits"]))
    return data

def lighthouse_seo_mobile(test_url):
    #sys.stdout = open('output.txt', 'wt', encoding="utf-8")
    # api-endpoint
    URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key=AIzaSyBkurRgGEs3fI-T4eLZ6xTAvX2VTbiGN7s"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {
        'url': test_url,
        'category': ["seo", "performance", "accessibility", "best-practices"],
        'strategy': "mobile"
    }
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS, stream=True)
    # extracting data in json format
    data = r.json()
    #print(pprint.pprint(data["lighthouseResult"]["audits"]))
    return 
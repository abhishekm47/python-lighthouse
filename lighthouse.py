
# importing the requests library
import requests
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()

from urllib_parse_urlencode import set_query_parameter


API_KEY=os.getenv("API_KEY")
HTTP_request = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

def lighthouse_seo(test_url):
    #sys.stdout = open('output.txt', 'wt', encoding="utf-8")
    # api-endpoint
    URL = set_query_parameter(HTTP_request, "key", API_KEY)
    print(URL)  
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


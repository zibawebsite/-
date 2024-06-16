import requests
import xmltodict
import json

url = "https://sahmeto.com/crypto-sitemap.xml"
response = requests.get(url)
data_xml = response.content

data_dict = xmltodict.parse(data_xml)

data_json = json.dumps(data_dict, indent=4)

print(data_json)

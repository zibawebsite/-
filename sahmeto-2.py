import requests
import xmltodict
import json

url = "https://sahmeto.com/crypto-sitemap.xml"
response = requests.get(url)
data_xml = response.content
data_dict = xmltodict.parse(data_xml)
for url_entry in data_dict["urlset"]["url"]:
    if "loc" in url_entry:
        coin_name = url_entry["loc"].split("/")[-1]
        url_entry["name"] = coin_name
data_json = json.dumps(data_dict, indent=4)
print(data_json)

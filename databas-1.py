import pymongo
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
data_json = json.loads(json.dumps(data_dict))
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sahmeto"]
collection = db["coinmap"]
collection.insert_many(data_json["urlset"]["url"])
print("Data inserted successfully.")

import pymongo
import requests
import json

symbol = "AAPL"
url = f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json"
response = requests.get(url)
data = response.json()
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sahmeto"]
collection = db["messages"]
if "messages" in data:
    messages = data["messages"]
    for message in messages:
        if collection.count_documents({"id": message["id"]}) == 0:
            collection.insert_one(message)
print("Messages inserted successfully.")

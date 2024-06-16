import requests
import json

symbol = "AAPL"
url = f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json"
response = requests.get(url)
data = response.json(1)
if "messages" in data:
    messages = data["messages"]
    for message in messages:
        print(f"User: {message['user']['username']}")
        print(f"Message: {message['body']}")
        print("-" * 40)
else:
    print("No messages found")
with open("stocktwits_messages.json", "w") as f:
    json.dump(data, f, indent=4)

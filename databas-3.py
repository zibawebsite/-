import pymongo
import requests
import time
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sahmeto"]
collection = db["messages"]
symbol = 'AAPL'
base_url = f'https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json'
def get_max_message_id():
    """دریافت بزرگ‌ترین message_id از پایگاه داده"""
    max_message = collection.find_one(sort=[("id", pymongo.DESCENDING)])
    return max_message['id'] if max_message else 0
while True:
    max_id = get_max_message_id()
    url = f'{base_url}?since={max_id}'
    response = requests.get(url)
    data = response.json()
    if 'messages' not in data:
        print("No new messages or error occurred.")
        break
    messages = data['messages']
    new_messages = 0
    for message in messages:
        if collection.count_documents({'id': message['id']}) == 0:
            collection.insert_one(message)
            new_messages += 1
    if new_messages == 0:
        print("No new messages to insert. Exiting loop.")
        break
    print(f"Inserted {new_messages} new messages.")
    time.sleep(1)

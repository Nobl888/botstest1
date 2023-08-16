```python
import requests
import json

def make_request(url, method="GET", headers=None, data=None):
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=json.dumps(data))
    else:
        raise ValueError("Method must be either 'GET' or 'POST'")

    response.raise_for_status()

    return response.json()

def format_token_data(token_data):
    return {
        "name": token_data["name"],
        "symbol": token_data["symbol"],
        "address": token_data["address"],
        "volume": token_data["volume"],
    }

def log_message(message):
    print(message)
```
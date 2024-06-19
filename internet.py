import requests


response = requests.get('https://api.sr.se/api/v2/channels/DSAFGFWQ')

print(response.status_code)
print(response.text)


"""
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId":1, "title":"Buy milk", "completed":False}

response = requests.post(api_url, json=todo)

print(response)

if(response.status_code):
    print("Ok")
"""
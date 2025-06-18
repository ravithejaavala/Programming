import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "id": 1,
    "title": "Updated Title by Ravi",
    "body": "I am learning REST API using PUT!",
    "userId": 1
}

response = requests.put(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
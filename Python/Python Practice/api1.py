import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Data:", response.json()[1])  # Print the first post

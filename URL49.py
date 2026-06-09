import requests

long_url = input("Enter URL: ")

api_url = f"https://tinyurl.com/api-create.php?url={long_url}"

response = requests.get(api_url)

if response.status_code == 200:
    print("Short URL:", response.text)
else:
    print("Failed to shorten URL")
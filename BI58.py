import requests

# Power BI Access Token
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Workspace ID
GROUP_ID = "YOUR_WORKSPACE_ID"

url = f"https://api.powerbi.com/v1.0/myorg/groups/{GROUP_ID}/datasets"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    datasets = response.json()
    print("Datasets:")
    for dataset in datasets["value"]:
        print(dataset["name"])
else:
    print("Error:", response.status_code)
    print(response.text)
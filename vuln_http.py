import requests
url = input("Digite a URL: ")
response = requests.get(url)
for header, value in response.headers.items():
    print(f"{header}: {value}")

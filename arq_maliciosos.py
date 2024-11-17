import hashlib
import requests
api_key = "sua_api_key"
file_path = input("Caminho do arquivo: ")
with open(file_path, "rb") as f:
    hash = hashlib.sha256(f.read()).hexdigest()
response = requests.get(f"https://www.virustotal.com/api/v3/files/{hash}", headers={"x-apikey": api_key})
print(response.json())

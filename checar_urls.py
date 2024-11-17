import os
url = input("Digite a URL: ")
response = os.system(f"ping -c 1 {url}")
print(f"{url} está {'online' if response == 0 else 'offline'}.")

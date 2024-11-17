import hashlib
import os
path = input("Digite o diretório: ")
for root, _, files in os.walk(path):
    for file in files:
        with open(os.path.join(root, file), 'rb') as f:
            print(file, hashlib.md5(f.read()).hexdigest())

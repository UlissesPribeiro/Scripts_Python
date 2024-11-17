import os
import time
path = input("Digite o diretório para monitorar: ")
before = dict([(f, None) for f in os.listdir(path)])
while True:
    time.sleep(10)
    after = dict([(f, None) for f in os.listdir(path)])
    added = [f for f in after if f not in before]
    removed = [f for f in before if f not in after]
    if added: print(f"Adicionados: {added}")
    if removed: print(f"Removidos: {removed}")
    before = after

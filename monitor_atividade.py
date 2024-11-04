import os
import time

def monitor_directory(directory):
    previous_files = set(os.listdir(directory))
    print(f"Monitorando o diretório: {directory}")

    while True:
        time.sleep(5)  # Espera 5 segundos entre as verificações
        current_files = set(os.listdir(directory))

        added_files = current_files - previous_files
        removed_files = previous_files - current_files

        if added_files:
            print(f"Arquivos adicionados: {', '.join(added_files)}")
        if removed_files:
            print(f"Arquivos removidos: {', '.join(removed_files)}")

        previous_files = current_files

directory_to_monitor = input("Digite o caminho do diretório para monitorar: ")
monitor_directory(directory_to_monitor)

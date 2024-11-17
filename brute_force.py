passwords = ["1234", "senha", "admin", "password"]
correct = "senha"
for password in passwords:
    if password == correct:
        print(f"Senha encontrada: {password}")
        break

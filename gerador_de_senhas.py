import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Digite o comprimento da senha: "))
generated_password = generate_password(password_length)
print(f"Sua senha gerada é: {generated_password}")

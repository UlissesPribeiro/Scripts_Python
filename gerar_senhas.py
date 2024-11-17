import random
import string
password = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
print(f"Senha forte: {password}")

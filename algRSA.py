# Функция для нахождения обратного элемента в кольце по модулю
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Функция для генерации ключей RSA
def generate_rsa_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Обычно выбирается зафиксированным значением
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))

# Функция для шифрования сообщения
def encrypt(message, public_key):
    n, e = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

# Функция для дешифрования сообщения
def decrypt(encrypted, private_key):
    n, d = private_key
    decrypted = [pow(char, d, n) for char in encrypted]
    decrypted_message = ''.join([chr(char) for char in decrypted])
    return decrypted_message

# Пример использования

p, q, message = int(input('Введите первое простое большое число p: ')), int(input('Введите второе большое число q: ')), input('Введите сообщение: ')
public, private = generate_rsa_keys(p, q)
encrypted_message = encrypt(message, public)
print("Зашифрованное сообщение:", encrypted_message)
decrypted_message = decrypt(encrypted_message, private)
print("Расшифрованное сообщение:", decrypted_message)
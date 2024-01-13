import os
import pyaes

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    os.remove(file_path)

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    new_file_path = os.path.splitext(file_path)[0]
    with open(new_file_path, 'wb') as new_file:
        new_file.write(decrypt_data)

if __name__ == "__main__":
    file_name = "database.txt.ransomwaretroll"
    key = b"testeransomwares"
    decrypt_file(file_name, key)

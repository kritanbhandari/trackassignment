from cryptography.fernet import Fernet
import csv


# Code to encrypt data
def encrypter(key, value):
    fernet = Fernet(key)
    return fernet.encrypt(value.encode()).decode()

    # key = Fernet.generate_key()
    # frenet = Fernet(key)
    # encrypted_username = frenet.encrypt("username".encode())
    # encrypted_password = frenet.encrypt("password".encode())

    # data = [[key.decode(), encrypted_username.decode(), encrypted_password.decode()]]

def decrypter(key, value):
    fernet = Fernet(key)
    return fernet.decrypt(value.encode()).decode()

def write_data_to_file(data:list, csvfile):
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == '__main__':
    key = Fernet.generate_key()
    data = [key.decode(), encrypter(key, "username"), encrypter(key, "password")]
    print(decrypter(key, data[1]))




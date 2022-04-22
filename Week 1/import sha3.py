import sha3
from base64 import encode
from attr import has

print("Tugas 1 Blockchain : Keccak 256")
    raw_message = input("Mohon masukkan kata apa saja: ")
print("Pesan Awal: \n", raw_message)
    encrypted = raw_message.encode()
    obj_encrypted = sha3.keccak_256(encrypted)
print("Berikut pesan yang telah terenkripsi: \n", obj_encrypted.hexdigest())
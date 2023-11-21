import cryptography
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def encrypt_data(key,data):
	
	# Create IV (Initialization Vector)
	iv = os.urandom(16) # 16 bytes for AES block size 

	# Padding data for block size  
	padder = padding.PKCS7(algorithms.AES.block_size).padder()
	data = padder.update(data) + padder.finalize()

	#CipherContext
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())


	#Encryptor
	encryptor = cipher.encryptor()


	#Encrypting the data 
	ciphertext = encryptor.update(data) + encryptor.finalize()

	
	#Return IV and Ciphertext
	return iv + ciphertext



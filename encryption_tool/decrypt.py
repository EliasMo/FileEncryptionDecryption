import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def decrypt_data(key, ciphertext_with_iv):
	
	# Extract the IV from the ciphertext 
	iv = ciphertext_with_iv[:16] # 16 byte IV for AES 

	# Extract the actual ciphertext 
	ciphertext = ciphertext_with_iv[16:]

	# Create a CipherContext for AES
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

	# Create decryptor 
	decryptor = cipher.decryptor()

	# Decrypt the ciphertext 
	decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

	# Unpad the decrypted data 
	unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
	data = unpadder.update(decrypted_data) + unpadder.finalize()


	return data 


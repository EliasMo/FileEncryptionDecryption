import os
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from key_generator import generate_key 
from encrypt import verify_key_size

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


def decrypt_file(input_file_path , output_file_path, key):
	# read encrypted file 
	with open(input_file_path, 'rb') as file:
		encrypted_content = file.read()

	decrypted_content = decrypt_data(key, encrypted_content)

	with open(output_file_path,'wb') as output_file:
		output_file.write(decrypted_content)

def parse_args(): 
	parser = argparse.ArgumentParser(description = 'decrypt a file')
	
	parser.add_argument('--file', required= True, help='Path to the input file to be encrypted')
	parser.add_argument('--output', required= True, help ='Path to the output encrypted file')
	parser.add_argument('--key', help='Path to the recipient\s public key file')

	return parser.parse_args()


def main():
	args = parse_args()

	key = generate_key()

	verify_key_size(key)

	decrypt_file(args.file, args.output, key)





if __name__ == '__main__':
	main()



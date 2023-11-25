import os
import argparse 
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, serialization
from cryptography.hazmat.primitives.asymmetric import rsa 
from key_generator import generate_key 



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


def encrypt_file(input_file_path, output_file_path,key):
	
	# Read a file 
	with open(input_file_path, 'rb') as file:
		file_content = file.read()

	# Use the encrypt data function 
	encrypted_content = encrypt_data(key, file_content)


	with open(output_file_path, 'wb') as output_file:
		output_file.write(encrypted_content)



def verify_key_size(key):
	key_size_bytes = len(key)
	if key_size_bytes not in [16, 24 ,32]:
		raise ValueError(f"Invalid key size ({key_size_bytes} bytes) for AES")
	else : 
		print ("All good for AES")

def parse_args(): 
	parser = argparse.ArgumentParser(description = 'Encrypt a file using RSA encryption.')
	
	parser.add_argument('--file', required= True, help='Path to the input file to be encrypted')
	parser.add_argument('--output', required= True, help ='Path to the output encrypted file')
	parser.add_argument('--key', help='Path to the recipient\s public key file')

	return parser.parse_args()

def main():
	args = parse_args()

	
	key = generate_key()



	#Example verification for key size 
	verify_key_size(key)


	# Example: Encrypt a file 
	encrypt_file(args.file, args.output, key)




if __name__ == '__main__':
	main()





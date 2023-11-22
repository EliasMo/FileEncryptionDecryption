import os 
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms
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


def encrypt_file(input_file_path, output_file_path,key):
	
	# Read a file 
	with open(input_file_path, 'rb') as file:
		file_content = file,read()


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

	with open(output_file_path, 'wb') as output_file:
		output_file.write(iv + ciphertext)





def verify_key_size(key):
	key_size_bytes = len(key)
	if key_size_bytes not in [16, 24 ,32]:
		raise ValueError(f"Invalid key size ({key_size_bytes} bytes) for AES")
	else : 
		print ("All good for AES")


#print("cryptography Versions:", cryptography.__version)


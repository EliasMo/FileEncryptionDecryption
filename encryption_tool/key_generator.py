from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_key():
	# Generate key 
	key = key_derivation_function()
	return key

def key_derivation_function():
	# Use a KDF to derive secure key using SHA-256
	digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
	digest.update(b"Your secret salt or context information")
	key = digest.finalize()
	return key 

print(generate_key())



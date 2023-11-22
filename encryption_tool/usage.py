from encrypt import encrypt_data #, verify_key_size
from decrypt import decrypt_data

key_aes_128 = b'1234567890123456'
# Example 
encryption_key = key_aes_128
data_to_encrypt = b'This is the sensitive data'

# Encryption 
encrypted_data = encrypt_data(encryption_key, data_to_encrypt)
print("Encrypted Data:", encrypted_data)

# Decryption 
decrypted_data = decrypt_data(encryption_key, encrypted_data)
print("Decrypted Data:", decrypted_data.decode('utf-8'))


#verify_key_size(encryption_key)
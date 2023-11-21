from encrypt import encrypt_data
from decrypt import decrypt_data

# Example 
encryption_key = b'my_cool_key'
data_to_encrypt = b'This is the sensitive data'

# Encryption 
encrypted_data = encrypt_data(encryption_key, data_to_encrypt)
print("Encrypted Data: ", encrypt_data)

# Decryption 
decrypted_data = decrypt_data(encryption_key, encrypted_data)
print("Decrypted Data: ", decrypted_data.decode('utf-8'))
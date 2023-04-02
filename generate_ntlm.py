import hashlib

input_str = input("Enter the string to convert to NTLM hash: ")

hash_obj = hashlib.new('md4', input_str.encode('utf-16le'))
ntlm_hash = hash_obj.digest()

print(ntlm_hash.hex())

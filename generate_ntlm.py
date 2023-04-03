import hashlib
import sys

if len(sys.argv) > 1:
    input_str = sys.argv[1]
else:
    input_str = input("Enter the string to convert to NTLM hash: ")

hash_obj = hashlib.new('md4', input_str.encode('utf-16le'))
ntlm_hash = hash_obj.digest()

print(ntlm_hash.hex())

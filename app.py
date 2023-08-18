import hashlib

# Produce a SHA256 hash from a string.
x = "Hello Python"

# Encode the string as bytes.
encode_x = x.encode()

# Hash the string.
hash_x = hashlib.sha256(encode_x)

# Results.
print(f"\nSHA256 hash of '{x}':")

# Convert it to a hex string.
print(hash_x.hexdigest())

# List of hashes: https://docs.python.org/3/library/hashlib.html
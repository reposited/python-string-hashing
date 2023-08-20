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

# ----------------------------------------------------------------
print("<------------------------>")
print("")
print("< User Input For String Hashing >")
print("")
# ----------------------------------------------------------------

# Adding user input for own user hashing.
userinput = str(input("Display a message you would like to hash: "))

# Print user message.
print(f"\nThe input message is: '{userinput}'") 
# Note: \n is a type of escape character that will create a new line when used.

# Produce a SHA256 hash from a string.
msg = userinput

# Encode the string as bytes.
encode_msg = msg.encode()

# Hash the string.
hash_msg = hashlib.sha256(encode_msg)

# Results.
print(f"\nSHA256 hash of '{msg}':") 

# Convert it to a hex string.
print(hash_msg.hexdigest())

# ----------------------------------------------------------------

# To-do: 
# - Convert msg hash to string.
# - Add filtering for adding more hashes.

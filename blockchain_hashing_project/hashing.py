import hashlib

# Step 1: Hashing function
def generate_hash(data):
    sha = hashlib.sha256(data.encode())
    return sha.hexdigest()

# Step 2: Original data
data = "Blockchain Transaction: Alice pays Bob 5 BTC"

# Step 3: Generate hash
hash_value = generate_hash(data)

# Step 4: Output
print("Original Data:")
print(data)

print("\nGenerated Hash:")
print(hash_value)

import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        return hashlib.sha256(block_data.encode()).hexdigest()


# -------- BLOCK CREATION --------

# Genesis Block (First Block)
genesis_block = Block(0, "Genesis Block", "0")

# Second Block
block1 = Block(1, "Alice pays Bob 5 BTC", genesis_block.hash)

# Print block details
print("Genesis Block:")
print(vars(genesis_block))

print("\nBlock 1:")
print(vars(block1))

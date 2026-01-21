import hashlib
import time

# -------- BLOCK CLASS --------
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        return hashlib.sha256(content.encode()).hexdigest()


# -------- BLOCKCHAIN CLASS --------
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=self.get_latest_block().hash
        )
        self.chain.append(new_block)

    # 🔐 Tampering Detection Function
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check 1: Current hash correct hai ya nahi
            if current.hash != current.calculate_hash():
                print("Block data tampered at index:", current.index)
                return False

            # Check 2: Previous hash match ho raha ya nahi
            if current.previous_hash != previous.hash:
                print("Chain broken between blocks", previous.index, "and", current.index)
                return False

        print("Blockchain is valid")
        return True

    def display_chain(self):
        for block in self.chain:
            print("\n-------------------------")
            print(f"Block Index: {block.index}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")


# -------- RUN PROGRAM --------
my_chain = Blockchain()

my_chain.add_block("Alice pays Bob 5 BTC")
my_chain.add_block("Bob pays Charlie 2 BTC")
my_chain.add_block("Charlie pays Dave 1 BTC")

print("\n🔹 Blockchain Before Tampering:")
my_chain.display_chain()
my_chain.is_chain_valid()

# -------- TAMPERING --------
print("\n⚠️ Tampering Block 1 Data...")
my_chain.chain[1].data = "Alice pays Bob 50 BTC"

print("\n🔹 Blockchain After Tampering:")
my_chain.display_chain()
my_chain.is_chain_valid()

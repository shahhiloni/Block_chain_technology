import hashlib
import time

# -------- BLOCK CLASS WITH MINING --------
class Block:
    def __init__(self, index, data, previous_hash, difficulty):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def calculate_hash(self):
        content = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(content.encode()).hexdigest()

    # ⛏️ Mining (Proof of Work)
    def mine_block(self):
        print(f"⛏️ Mining block {self.index}...")
        while True:
            hash_value = self.calculate_hash()
            if hash_value.startswith("0" * self.difficulty):
                print(f"✅ Block {self.index} mined with nonce: {self.nonce}")
                return hash_value
            self.nonce += 1


# -------- BLOCKCHAIN CLASS --------
class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", self.difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=self.get_latest_block().hash,
            difficulty=self.difficulty
        )
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print("\n-------------------------")
            print(f"Block Index: {block.index}")
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")


# -------- RUN PROGRAM --------
my_chain = Blockchain(difficulty=4)

my_chain.add_block("Alice pays Bob 5 BTC")
my_chain.add_block("Bob pays Charlie 2 BTC")

my_chain.display_chain()

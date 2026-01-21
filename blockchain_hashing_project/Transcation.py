import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        return hashlib.sha256(content.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [Block(0, ["Genesis Transaction"], "0")]

    def add_block(self, transactions):
        last_block = self.chain[-1]
        block = Block(len(self.chain), transactions, last_block.hash)
        self.chain.append(block)

    def show_chain(self):
        for block in self.chain:
            print("\nBlock:", block.index)
            print("Transactions:", block.transactions)
            print("Hash:", block.hash)


# -------- RUN --------
bc = Blockchain()

bc.add_block([
    "Alice → Bob : 5 BTC",
    "Bob → Charlie : 2 BTC"
])

bc.add_block([
    "Charlie → Dave : 1 BTC",
    "Dave → Eva : 0.5 BTC"
])

bc.show_chain()

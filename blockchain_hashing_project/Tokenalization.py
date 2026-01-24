import uuid
import datetime

# -------------------------------
# Blockchain Ledger (Simple)
# -------------------------------
blockchain_ledger = []

def add_block(transaction):
    block = {
        "block_id": str(uuid.uuid4()),
        "timestamp": str(datetime.datetime.now()),
        "transaction": transaction
    }
    blockchain_ledger.append(block)

# -------------------------------
# Token Class
# -------------------------------
    
class Token:
    def __init__(self, asset_name, total_supply):
        self.asset_name = asset_name
        self.total_supply = total_supply
        self.balances = {}

    def mint(self, owner):
        self.balances[owner] = self.total_supply
        add_block(f"{self.total_supply} tokens minted for {owner}")

    def transfer(self, sender, receiver, amount):
        if self.balances.get(sender, 0) >= amount:
            self.balances[sender] -= amount
            self.balances[receiver] = self.balances.get(receiver, 0) + amount
            add_block(f"{amount} tokens transferred from {sender} to {receiver}")
        else:
            print("❌ Insufficient balance")

    def show_balances(self):
        print("\n🔹 Token Balances:")
        for user, balance in self.balances.items():
            print(f"{user}: {balance} tokens")

# -------------------------------
# Main Program
# -------------------------------
            
gold_token = Token("Gold", 100)

# Mint tokens
gold_token.mint("Owner")

# Transfer tokens
gold_token.transfer("Owner", "Alice", 30)
gold_token.transfer("Owner", "Bob", 20)

# Show balances
gold_token.show_balances()

# Show blockchain ledger
print("\n🔹 Blockchain Ledger:")
for block in blockchain_ledger:
    print(block)


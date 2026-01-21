class SmartContract:
    def __init__(self):
        self.accounts = {
            "Alice": 10,
            "Bob": 5
        }

    def transfer(self, sender, receiver, amount):
        print(f"\nExecuting Smart Contract: {sender} → {receiver} : {amount} BTC")

        if self.accounts.get(sender, 0) >= amount:
            self.accounts[sender] -= amount
            self.accounts[receiver] = self.accounts.get(receiver, 0) + amount
            print("✅ Transaction Successful")
        else:
            print("❌ Transaction Failed: Insufficient Balance")

        print("Updated Accounts:", self.accounts)


# -------- RUN --------
contract = SmartContract()

contract.transfer("Alice", "Bob", 3)
contract.transfer("Bob", "Alice", 10)

---------------------------------------------- Part - 1 -------------------------------------------

1. What is BlockChain Technology?
- Blockchain Technology is a decentralized, distributed digital ledger system that records transactions across a network of computers in a secure, transparent, and tamper-proof way.

Block: A container that stores a group of transactions
Chain: A sequence of blocks linked together in chronological order
Decentralized: No single person, company, or government owns the data; instead, it’s shared across many computers.
Immutable: Once information is added, it cannot be altered or deleted, which ensures trust and security.

2. Who Build or create Block Chain Technology?
- Blockchain technology was created by an individual (or group) using the pseudonym Satoshi Nakamoto in 2008.
- In October 2008, Satoshi Nakamoto published a whitepaper titled “Bitcoin: A Peer-to-Peer Electronic Cash System”.
- In January 2009, Nakamoto released the first open-source software and launched Bitcoin, which was the first practical implementation of blockchain.

Note: After Bitcoin’s success, developers and researchers expanded blockchain use cases beyond cryptocurrency (like in finance, supply chain, healthcare, etc.).

3. why Satoshi Nakamoto built blockchain instead of using the traditional banking system?
- 1. Problem with Traditional Banking System
    - Banks act as middlemen for money transfers.
    - This causes:
        1. High fees (especially for international transactions).
        2. Delays (settlements take hours/days).
        3. Trust issues (you need to trust banks to handle your money correctly).
        4. Single point of failure (if the bank fails, users lose access).

- 2. Satoshi’s Goal
    - Create a Peer-to-Peer Electronic Cash System (Bitcoin) that:
        1. Allows people to send money directly without banks.
        2. Is decentralized (no single authority controls it).
        3. Uses cryptography to ensure security and trust instead of banks.
    
- 3. Blockchain Solution
    - Blockchain is like a public ledger that everyone can see but no one can secretly change.
    - Every transaction is verified by a network of computers (nodes) instead of a bank.
    - Once added to the blockchain, data cannot be altered or deleted → this ensures trust without middlemen.

Note: Blockchain relies on mathematics + cryptography + consensus → trust is built into the system

------------------------------------------- Part - 2 ----------------------------------------

1. What is Centralized System? 
- A centralized system is one where all data, power, or decision-making is controlled by a single central authority (like a server, company, or government).

****** Example: Let’s say you want to transfer ₹5000 from your account to your friend’s account:
1. You → request transfer from your bank.
2. Bank → checks your balance, approves, and updates its database.
3. Friend → receives money in their account.

Here the Bank is the central authority that controls everything.

******  Diagram of Centralized System ******

                [CENTRAL AUTHORITY ]
                  (Bank Server)
                         |
     -----------------------------------------
     |             |             |           |
 [User A]      [User B]      [User C]     [User D]

****** Disadvantages: 
1. Users must trust the central authority.
2. If the central point fails → the whole system is affected.
3. Example: Banks, Facebook, Google, Traditional Databases, Food Delievery Apps, etc. 

2. What is De-Centralized System?
- A Decentralized System is a network where control, decision-making, and data storage are not managed by a single central authority.Instead, multiple independent nodes (computers/servers/participants) share power and coordinate among themselves.

****** Advantages 
1. No central authority → Everyone has equal control.
2. Transparency → Every node can verify the data.
3. Security → If one node is hacked, the system still works.
4. Fault tolerance → Failure of one node doesn’t stop the whole system.

3. Explain how blocks are connected in a blockchain.
    1. Block Structure: What information a block contains.
        1. Block Header (metadata: timestamp, previous block hash, nonce)
        2. Transactions/Data
        3. Hash of the Block

****** Block Structure Diagram 


----------------------------------------- Part -3 --------------------------------------------
1. Components Of BlockChain 
-   1. Node: one kind of user who are Part of the Block chain network 
        1. Full Node: A Node who Have blue print or copy of all nodes, It stores a copy of the blockchain ledger (full or partial).
          - Broadcasting : It verifies and shares transactions and blocks.
          - It communicates with other nodes to keep the network decentralized.
          - Enforces blockchain rules (consensus, protocol rules)
          Note: Full Node require more memory and large data size.
          - Validated transition message

        2. Partial Node: no need to require more memory and large data size.
        (A node who has small number of memory size its automatically converted into partial node)
         
         Limitations of Partial Node: 
         1. can't do Broadcasting
         2. can't initialized Block
         3. can't validated transition message

    2. Ledger: A Ledger in blockchain is a digital record-keeping system that stores all transactions across the network in a secure, transparent, and immutable way.
    - In blockchain → Ledger = Distributed Digital Book shared across all nodes.

    3. Wallet: A Blockchain Wallet is a digital tool that allows users to store, send, and receive cryptocurrencies securely.
    - It does not store actual coins.
    - Instead, it stores your private keys (like a password) and public keys (like your account number).
    - Transactions are recorded on the blockchain ledger, and the wallet helps you access and manage them.

    1. Public Key = Bank Account Number (you can share).
    2. Private Key = ATM PIN/Password (keep secret).

****** Types of Wallets in Blockchain
- Wallets are mainly divided into Hot Wallets (online) and Cold Wallets (offline).
1. Hot Wallets (Online) : 
- Connected to the internet.
- Easy to use but slightly less secure (vulnerable to hacks).
    1. Web Wallets : Accessed via browser (e.g., MetaMask, Blockchain.com).
    - Convenient but depends on third-party security.

    2. Mobile Wallets : Apps on smartphones (e.g., Trust Wallet, Coinbase Wallet).
    - Very handy for quick payments.

    3. Desktop Wallets : Installed on PC/Laptop (e.g., Electrum, Exodus).
    - More secure than web wallets but still online.

2. Cold Wallets (Offline): 
- Not connected to the internet.
- Very secure against hacking.
- Best for long-term storage of large funds.

Types: 
1. Hardware Wallets: 
- Physical devices like USB sticks.
- Store private keys offline.
- Example: Ledger Nano X, Trezor.

2. Paper Wallets: 
- Keys printed on paper (QR codes).
- Fully offline but risky (paper can be lost/damaged).

****** Diagram (Wallet Types) 

           Blockchain Wallets
           ┌───────────┐
           │   Hot      │
           │ (Online)   │
           └───────────┘
             /   |    \
     Web   Mobile  Desktop

           ┌───────────┐
           │   Cold     │
           │ (Offline)  │
           └───────────┘
             /       \
      Hardware     Paper

    4. Nonce: Nonce stands for “Number Only Used Once”.
    - It is a random number (integer) that miners change repeatedly until they find a valid block hash.
    - Used in Proof of Work (PoW) blockchains (like Bitcoin).
    - Ensures that the hash of a block meets the required difficulty target (e.g., starting with certain number of zeros).
    - Nonce is part of the block header.

****** Role of Nonce in Mining
1. A block contains:
    - Previous block hash
    - Transactions
    - Timestamp

2. Miners try different nonce values → hash the block.
3. If the hash < target difficulty → block is accepted.
4. If not → change nonce and try again.
    5. Hash: 
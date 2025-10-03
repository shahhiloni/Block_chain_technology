-------------------------------------- Merkle Tree ------------------------------------------

----------------------------------------- Part - 1 ----------------------------------------------

1. What is Merkle Tree?
- A Merkle Tree (or Hash Tree) is a data structure used in blockchain to efficiently and securely verify transactions.
- It organizes transactions in a block into a tree of hashes.
- The root hash (Merkle Root) represents all transactions in that block.
- If even one transaction changes, the Merkle Root will also change → making tampering easy to detect.

2. Structure of a Merkle Tree
- Each transaction is hashed (using SHA-256, etc.).
- Pairs of transaction hashes are combined and hashed again.
- This process continues until only one hash remains → called the Merkle Root. 

****** Note: Hashing is the process of taking any input (transaction data, block info, etc.) and converting it into a fixed-length unique string (hash) using a mathematical function (like SHA-256).
- Input can be large or small → Output (hash) is always the same size.
- The output is called a hash value or digest.
- Blockchain uses hashing to secure data, link blocks, and maintain immutability.
- hashing Provides Data Integrity, Block Identification, Linking Blocks Together, Efficiency, etc. 

****** Note: SHA - 256 : SHA-256 stands for Secure Hash Algorithm – 256 bit.
- It is a cryptographic hash function that takes any input (text, number, file, transaction data, etc.) and produces a fixed 256-bit (64-character hexadecimal) output.

****** Example : 
** Format: Transaction Data → Hash Function → Hash Value

** Input: "Blockchain"
SHA-256 Output: 
625da44e4eaf58d61cf048d168aa6f5e492dea166d8bb54ec06c60df272f6fd1


****** Why is SHA-256 Used in Blockchain?
- Blockchain (like Bitcoin) uses SHA-256 for:
1. Data Integrity : Each transaction is hashed using SHA-256.
- If anyone tries to change the transaction → hash changes immediately → tampering is detected.

2. Block Hashing : Every block header (includes transactions, timestamp, nonce, previous block hash) is hashed with SHA-256.
- The result = block hash → unique fingerprint of that block.

3. Linking Blocks Together : Each block stores the hash of the previous block.
- This chaining (using SHA-256) ensures immutability → changing one block invalidates all following blocks.

4. Proof of Work (Mining): Miners change the nonce and hash the block header using SHA-256.
- They search for a hash that meets the difficulty target (e.g., starts with certain zeros).
- This makes mining secure and resource-intensive.

5. Security: SHA-256 is one-way → you cannot reverse a hash to get the original data.
- It is resistant to: 
1. Collision attacks (two inputs producing same hash).
2. Pre-image attacks (finding input from output).

****** Diagram 

Transaction Data + Nonce + Previous Hash
             ↓ SHA-256
       Unique Block Hash (256-bit)




----------------------------------------- Double Spending ---------------------------------------
1. Trying to spend the same digital currency twice (like sending the same Bitcoin to two different people).

## Why It’s a Problem
- Digital money is just data, and data can be copied.
- Without a safeguard, one coin could be used multiple times, causing fraud.

## How Blockchain Prevents It
1. Public Ledger (Blockchain):
- Every transaction is recorded on a transparent ledger.
- Once confirmed, it cannot be changed.

2. onsensus Mechanism (PoW / PoS):
- Miners/validators check if coins are already spent.
- Only valid transactions are added to the blockchain.

3. Cryptographic Signatures:
- Each transaction is signed by the owner’s private key.
- Prevents forgery.

Example: 
1. You own 1 BTC.
2. You try to send 1 BTC to Alice and the same 1 BTC to Bob.
3. Blockchain will validate one transaction and reject the duplicate → so double spending is stopped.

-------------------------------------------- UTXO ------------------------------------------

1. What is UTXO?
- UTXO stands for Unspent Transaction Output.
- It is the fundamental way cryptocurrencies like Bitcoin keep track of balances.
- Ex: 1: 
*** Think of UTXO like digital cash notes (₹100, ₹500, ₹2000) in your wallet.
1. When you spend, you give some notes (inputs).
2. You may get back some change (outputs).
3. The notes you haven’t spent yet are your UTXOs.

2. How it works?
- Every transaction in Bitcoin creates outputs.
Example: If A sends 1 BTC to B → this creates an output of 1 BTC for B.

- These outputs can be spent later in another transaction.
Until they are spent, they are called UTXO.

- Once spent, the UTXO disappears (it can’t be used again).

*** Example: 
1. Imagine you have these UTXOs in your Bitcoin wallet:
    1. 0.3 BTC
    2. 0.7 BTC
    3. 1 BTC

👉 Your total balance = 2 BTC.
step: 1: Now, you want to send 1.2 BTC to someone.
step: 2: The system will combine: 0.7 BTC + 0.7 BTC = 1.4 BTC (inputs).
step: 3: 1.2 BTC goes to the receiver.
step: 4: 0.2 BTC comes back to you as change (a new UTXO).

3. Key Properties of UTXO:
- Atomic → Cannot be divided, you must spend the whole output. (Like cash notes).
- Immutable → Once spent, it can’t be reused.
- Transparent → Easy to verify ownership and balance.
- Stateless system → No central balance sheet; balances are calculated from UTXOs.

4. Importance of UTXO in Blockchain:
- Prevents Double Spending – A UTXO can only be used once.
- Scalability – Easy to parallelize transactions since UTXOs are independent.
- Security – Simplifies verification of funds.
- Privacy – UTXOs can be split/merged, making tracking harder.


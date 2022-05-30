# Consensus

Consensus is the mechanism by which nodes agree on both

- historical blockchain
- new additions to the historical blockchain

> Consensus is the process by which all nodes agree on the same ledger.

The difficulty of consensus is to **trust** the result of a transaction or block, without trusting the parties involved.

DeFi is at the **early stage** of providing consensus. There are a lot of mechanism. Two of them are popular.

- PoW: Bitcoin, ETH 1.0
- PoS: ETH 2.0

## Proof-of-Work (PoW)

PoW is a way to solve consensus problem. It's very straightforward.

- The mining node begins to solve an very difficult **hashing problem**, with the **transactions being a part of the input**. (It guesses the key of the hashing)

- Once the correct answer is found, the result will broadcast to the rest of the network. (The miners will be rewarded if they find the answer)

PoW is **robust**. But it **wastes a lot of resources** to solve the hashing problem.

## Proof-of-Stake (PoS)

Instead of all the people solve the hashing problem together, **PoS delegates the work to the people who has stakes**.

For example, if you have 10% of stakes, you handle the 10% of transaction validation work.

If the validator proves a wrong transaction, he will pay for the loss by reducing his stakes.

It's more efficient than PoW, but it **leads to centralization**, which makes the rich richer (The people who holds more stakes has more chance to handle the validation, so they have more chance to have the reward).

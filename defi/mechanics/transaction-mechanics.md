# Transaction Mechanics

Transaction is **sending data from an address to another**.

In EHT, there are 2 types of account:

- Externally owned account (EOA)
- contract account (using smart contract)

## How does transaction work?

When sending data to a **contract account**, the data are used to **execute** codes in that contract.

The transaction starts by **interacting with a single contract**, then a contract can interact with **a large number of dApps(ETH smart contract)**.

## Atomicity

If one contract failed to execute, **all the previous contracts will be reverted**.

## Gas

Transaction has the gas fee. It depends on the complexity of the transaction.

If the transaction is failed, the gas fee cost in the middle won't be refund to the user.

## Mempool

The transactions are posted to a memory pool, or mempool, before they are added into a block.

## Miner extractible value (MEV)

MEV is a **measure of the profit** that the miner could make by **including, excluding, re-ordering transactions**.

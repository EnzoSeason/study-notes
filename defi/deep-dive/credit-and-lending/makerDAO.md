# MakerDAO

MakerDAO creates **crypto-collateralized stablecoin**, DAI. It runs without outside centralized institutions, such as vaulting, auditing.

They have 2 tokens:

- DAI: stablecoin
- MKR: governance token

## Mechanics of DAI

1. A user deposits **ETH or ERC-20** token to a **Vault**.

   Vault is a smart contract that **escrows collateral** and keep tracks of the **USD-denominated value** of it.

2. The user can **mint DAI** depended on his assets. This creates a "debt" in DAI that must be paid back by the Vault holder.

3. The user can use DAI for whatever he wants, like exchanging for cash, buying more ETH, etc.

Because ETH is more volatile DAI, we need **over-collateral**.

What's more, we don't mint DAI to the max. We have a **buffer** to avoid being liquidated if the value of ETH drops.

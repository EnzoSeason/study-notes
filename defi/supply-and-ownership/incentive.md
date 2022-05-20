# Incentive

## Types of incentive

- staked incentives: apply to a balance of tokens custodied in a smart contract.
- direct incentives: apply to user in the system who do not have a custodied balance.

## Slashing

Slashing is the **removal** of a portion of a user's staked balance, thereby **creating a negative staked incentives**. Keeper will check if there is a negative action.

**Slashing condition** is a mechanism that triggers a slashing.

An example of a slashing situation is when a user’s staked balance is reduced because of an undercollateralization event.

## Keeper

Keeper is incentived to perform an action in a DeFi protocol or other dApp. He receives fee.

Keepers are externally owned addresses. They are not part of the algorithm of the smart contract. They watch for events like undercollateralization and close out positions that violate the term of the contract. They are rewarded.

Downside is the gas price. It can be too high to encourage keeper to work.

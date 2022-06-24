# Balancer

It's a descentralized exchange, similar to [Uniswap](./uniswap.md).

However, it can hold **more than 2 assets** in a liquidity pool.

- Instead of having a constant _k_, it has a **bounding surface** _V_.
- Instead of making `k = x * y`, `V = `$\prod_{t = 0}^{n} B_{t}^{W^{t}}$.

  - n: The number of the types of the tokens
  - B: The balance of the token _t_
  - W: The normalized weight of the token _t_

## Rehypothecation

Rehypothecation is **pledging collateral** for debt.

That means you can use borrowed assets as collateral, and demande more loan.

As the result, the amount asset in the market is more than that is issued.

### Money multiplier

In CeFi, the gouverment decides that the resever ratio is **10%**. Image you deposit $100 in a bank _A_.

1. The bank _A_ sets aside $10, and lends $90.
2. A user borrows $90, and deposits it into the bank _B_.
3. The bank _B_ sets aside $9, and lends $81.

In total, the deposit is $100, but the loan is $171.

### DeFi multiplier

Multiplier is similar to that in CeFi. The only difference is that no gouverment descides the resever ratio. Different protocols have different collateral ratio. For example:

1. User deposits $1500 and get 1000 DAI. (The collateral rate is 150%)

2. He deposits 1000 DAI and 1000 USDC in Uniswap.

3. Uniswap gives him $2000 worth of LP and he collateralizes it to borrow 1960 DAI. (The collateral rate is 102%)

As the result, the total deposit is $1500 + $1000 (in DAI) = **$2500**, while the total loan is $1000 (in DAI) + $2000 (in LP) = **$3000**. More importantly, the collateral rate is lower in second round (102% vs 150%).

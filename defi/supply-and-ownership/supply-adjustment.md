# Supply adjustment

## Burn (reduce supply)

Burning means **removing tokens from circulation**.

There are two ways to do:

- Manually send them to an **unowned ETH address**.
- **More efficient**: create a **contract** that is incapable of spending them.

It's possible that we burn the tokens by accident. **Checksum** is one method to prevent it.

Why do we burn?

- redemption (e.g., sel the Equity token and get ETH)
- drive the token price upward
- penalize bad acting

## Minting (increase supply)

Minting means **increase tokens from circulation**.

Minting helps people raise fund easier. We don't need to pass banking system anymore.

Why do we mint?

- acquiring corresponding ownership share
- drive the token price downward
- reward user behavior

Minting can act as an **incentive mechanism**.

## Bonding curves

A bonding curve is the **price relationship** between the **token supply** and corresponding **asset** used to purchase the tokens.

### Linear bonding curve

Suppose that we have a token, TKN. The simplest bonding curve can be:

```code
TKN = 1
```

It means 1 TKN equals 1 ETH.

Next, consider a simple linear bonding curve:

```code
y = mx + b
```

If `m = 1` and `b = 0`, that means the first TKN equals 1 ETH, the second equals 2 ETH, etc..

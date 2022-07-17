# Uniswap

Uniswap is an **Automated Market Maker** on Ethereum.

The core of Uniswap is **constant product rule**.

```
k = x * y
```

- x: The balance of asset A
- y: The balance of asset B
- k: The constant value

For example, we have 4 DAI and 4 USDC in a contract. If we want to take 2 USDC from it, we need to deposit 4 DAI so that the constant value _k_ stays 16. In this case, the splippage is **2 DAI : 1 USDC**.

As we can see, the rate is high. However, if the **liqudity is deep**, e.g. 1000 DAI and 1000 USDC, the slippage of taking out 2 USDC is going to be **1.04 DAI : 1 USDC**. In conclusion, the **liqudity is important in AAM**.

## Impermanent loss

Liquidity providers in Uniswap earn passive income, however, the **exchange rate** of the underlying assets will have **changed**s. This raises the possibility of impermanent loss.

Impermanent loss is the **oppotunity loss**. It's possible that the providers earn more if they don't put the assets in Uniswap pool.

## Router contracts

If the asset A and B are not tradable, and A/C, B/C are. We still can trade A/B. Router contracts help to **find the best path to trade assets**.

## Drawback

### Front running

It's a **drawback** of AAM and Proof of Work. The miner can see all the pending transactions, and choose which one to run first.

### Arbitrage

Arbitrage occurs when an investor can make a profit from **simultaneously buying and selling a commodity in two different markets**. For example, gold may be traded on both New York and Tokyo stock exchanges.

Arbitrageurs profit at the expense of liquidity providers.

## Flash swap

Flash swap sends the tokens before the user pays for them.

It's different from **flash loan**, whose repayment needs the same asset. Flash swap doesn't. Therefore, it's interesting for **arbitrageurs**.

For example, we borrow in USDC and pay back in DAI.

![flash-swap](./images/flash-swap.png)

## Solution

![uniswap-solution](./images/uniswap-solution.png)
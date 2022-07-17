# Layer 2

Layer 2 refers to the solution built **on top of a blockchain**. The goal is **moving small transactions off-chain**. It pass the transactions to the blockchain only in certains states, such as initializing, terminating.

Therefore, it provides **much lower fees**. However, it's more centralized.

## Mechanics

Layer 2 has a **multi-signature address**. It's like a vault that can only be opened when both parties agree. It's a **payment channel**.

When we initialize this channel, both parties deposit coins into this address. It's on-chain.

After that, the transaction between both of them, it's off-chain.

Either of the parties wants to withdraw the coin, it's on-chain.

## Importance

- Any party in the **multi-signature address** can release its fund. One party can't hold on to the other.

- Network can find the **fastest and cheapest** path to transact from A to B.

## Rollup

Similar to Layer 2, Rollup aggregates the small transactions into a big one and put it on-chain.

# SHA-256 Hash Function Demo

A simple Python demonstration of how cryptographic hash functions are used in sealed-bid auctions.

Created for the Finance 5140 Blockchain Auction presentation.

## Overview

This demo uses SHA-256 to illustrate:

1. **Deterministic hashing:** The same input produces the same hash.
2. **Input sensitivity:** A small change in the input produces a different hash.
3. **Bid commitment:** A bidder can commit to a bid without revealing its value.
4. **Reveal and verification:** The original bid and secret can be revealed and checked against the commitment.
5. **Tamper detection:** Changing the bid causes verification to fail.

## Requirements

- Python 3
- No external libraries required

## Running the Demo

```bash
python3 hash_function.py
```

Press Enter to proceed through each part of the demonstration.

## How It Relates to Blind Auctions

In a sealed-bid auction, bidders submit cryptographic commitments instead of revealing their bid amounts.

This example computes a commitment using SHA-256:

`commitment = SHA256(bid + nonce)`

The nonce is a randomly generated secret used to help keep the bid private.

After bidding closes, the bidder reveals the original bid and nonce. The commitment is recomputed to verify that the revealed bid matches the original commitment.

## Note

This is an educational demonstration. It does not reproduce the exact commitment format used by the Hyperledger Fabric auction application.
# Hash Function and Blind Auction Demo
# Finance 5140 - Sealed-Bid Auction
#
# This demo shows how SHA-256 can be used
# to create and verify a bid commitment.
#
# To run the code, type 
#
# python3 hash_function.py
#
# in terminal.

import hashlib
import secrets

# Convert a string into a SHA-256 hash.
def hash_value(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def pause():
    input("\nPress Enter to continue...")


# --------------------------------------------------
# Part 1: Same input produces the same hash
# --------------------------------------------------

print("=== Part 1: Same Input, Same Hash ===")

bid = "650"

hash1 = hash_value(bid)
hash2 = hash_value(bid)

print("Bid:", bid)
print("First hash: ", hash1)
print("Second hash:", hash2)
print("Are they equal?", hash1 == hash2)

pause()


# --------------------------------------------------
# Part 2: Small changes produce different hashes
# --------------------------------------------------

print("\n=== Part 2: Small Change, Different Hash ===")

bid1 = "650"
bid2 = "651"

hash1 = hash_value(bid1)
hash2 = hash_value(bid2)

print("Bid 1:", bid1)
print("Hash 1:", hash1)

print()

print("Bid 2:", bid2)
print("Hash 2:", hash2)

print()

print("Are the hashes equal?", hash1 == hash2)

pause()


# --------------------------------------------------
# Part 3: Create a sealed bid (Commit)
# --------------------------------------------------

print("\n=== Part 3: Commit a Secret Bid ===")

# Bidder chooses a bid amount.
secret_bid = 650

# Generate a random secret value.
# The secret makes guessing the bid harder.
nonce = secrets.token_hex(16)

# Combine the bid and secret.
bid_data = f"{secret_bid}:{nonce}"

# Create the commitment.
commitment = hash_value(bid_data)

print("Bidder creates a sealed bid.")
print("The bid amount is kept private.")

print("\nPublished commitment:")
print(commitment)

print("\nThe blockchain stores this commitment.")
print("Other participants cannot directly see the bid.")

pause()


# --------------------------------------------------
# Part 4: Reveal and verify the bid
# --------------------------------------------------

print("\n=== Part 4: Reveal and Verify ===")

print("The auction is now closed.")
print("The bidder reveals the bid and secret.")

revealed_bid = 650

# Recalculate the hash using the revealed data.
revealed_data = f"{revealed_bid}:{nonce}"
revealed_hash = hash_value(revealed_data)

print("\nRevealed bid:", revealed_bid)
print("Revealed nonce:", nonce)

print("\nOriginal commitment:")
print(commitment)

print("\nRecalculated hash:")
print(revealed_hash)

if revealed_hash == commitment:
    print("\nVerification successful!")
    print("The bid matches the original commitment.")
else:
    print("\nVerification failed!")
    print("The bid does not match the commitment.")

pause()


# --------------------------------------------------
# Part 5: Try changing the bid
# --------------------------------------------------

print("\n=== Part 5: Can We Change the Bid? ===")

# The bidder tries to change the bid from 650 to 651.
changed_bid = 651

changed_data = f"{changed_bid}:{nonce}"
changed_hash = hash_value(changed_data)

print("Original bid:", secret_bid)
print("Changed bid: ", changed_bid)

print("\nOriginal commitment:")
print(commitment)

print("\nHash of changed bid:")
print(changed_hash)

if changed_hash == commitment:
    print("\nVerification successful!")
else:
    print("\nVerification failed!")
    print("The bidder cannot change the bid after committing.")

print("\n=== Demo Complete ===")

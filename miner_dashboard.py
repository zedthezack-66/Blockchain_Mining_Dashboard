import hashlib
import time

# Define the mining function
def mine(block_number, transactions, previous_hash, difficulty):
    nonce = 0
    prefix = '0' * difficulty  # Required number of leading zeros
    print(f"\n⛏️ Mining Block {block_number} with difficulty {difficulty}...")

    start_time = time.time()
    
    while True:
        text = f"{block_number}{transactions}{previous_hash}{nonce}".encode()
        hash_result = hashlib.sha256(text).hexdigest()

        if hash_result.startswith(prefix):
            end_time = time.time()
            print(f"✅ Block {block_number} Mined! Nonce: {nonce}")
            print(f"🔗 Hash: {hash_result}")
            print(f"⏳ Time Taken: {end_time - start_time:.2f} seconds")
            return nonce, hash_result  # Return the valid nonce and hash

        nonce += 1  # Increment nonce and try again

# Initialize blockchain parameters
difficulty = 4  # Adjust difficulty level
block_number = 100

previous_hash = "00000000000000000000000000000000"  # Genesis block hash

# Continuous mining loop
while True:
    transactions = f"User{block_number}->User{block_number+1}->10"  # Fake transactions
    nonce, block_hash = mine(block_number, transactions, previous_hash, difficulty)

    # Update values for the next block
    previous_hash = block_hash  # Chain the blocks
    block_number += 1

    # Ask user if they want to continue mining
    choice = input("\nDo you want to continue mining? (y/n): ").strip().lower()
    if choice != 'y':
        print("\n⛔ Mining stopped by user.")
        break

print("\n👋 Exiting mining process. Goodbye!")


yield
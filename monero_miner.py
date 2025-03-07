import hashlib
import time

# Function to log mining session
def log_mining_details(log_file, block_number, nonce, hash_result, time_taken):
    with open(log_file, 'a') as f:
        f.write(f"Block {block_number} Mined!\n")
        f.write(f"Nonce: {nonce}\n")
        f.write(f"Hash: {hash_result}\n")
        f.write(f"Time Taken: {time_taken:.2f} seconds\n")
        f.write('-' * 40 + '\n')

# Mining function that tries to find a nonce that produces the correct hash
def mine(block_number, transactions, previous_hash, difficulty, log_file):
    nonce = 0
    prefix = '0' * difficulty  # Leading zeros required for the proof of work
    print(f"⛏️ Mining Block {block_number}... Difficulty: {difficulty}")

    start_time = time.time()

    while True:
        text = f"{block_number}{transactions}{previous_hash}{nonce}".encode()
        hash_result = hashlib.sha256(text).hexdigest()

        if hash_result.startswith(prefix):
            end_time = time.time()
            print(f"✅ Block {block_number} Mined! Nonce: {nonce}")
            print(f"🔗 Hash: {hash_result}")
            print(f"⏳ Time Taken: {end_time - start_time:.2f} seconds")
            
            # Log mining session details
            log_mining_details(log_file, block_number, nonce, hash_result, end_time - start_time)
            
            return nonce, hash_result

        nonce += 1  # Increment nonce and try again

# Initial blockchain setup
difficulty = 4  # Adjust difficulty for testing (number of leading zeros)
block_number = 1
previous_hash = "00000000000000000000000000000000"  # Genesis block hash
log_file = 'mining_log.txt'  # Log file to store mining session data

# Continuously mine blocks
while True:
    transactions = f"User{block_number} -> User{block_number+1} -> 10"  # Fake transaction data
    nonce, block_hash = mine(block_number, transactions, previous_hash, difficulty, log_file)

    # Update values for the next block
    previous_hash = block_hash  # Chain blocks together
    block_number += 1

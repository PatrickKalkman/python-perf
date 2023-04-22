import hashlib
import time

def chain_sha1_hash(input_str, iterations):
    current_hash = input_str
    for _ in range(iterations):
        current_hash = hashlib.sha1(current_hash.encode()).hexdigest()
    return current_hash

if __name__ == "__main__":
    input_str = "Turbocharge Your Python Code"

    start_time = time.time()
    result = chain_sha1_hash(input_str, 3_000_000)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")

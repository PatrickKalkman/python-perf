# test_hashing.py
import time
from measuring.time_function import chain_sha1_hash


def test_chain_sha1_hash_performance():
    input_str = "Turbocharge Your Python Code"
    iterations = 3_000_000

    start_time = time.time()
    _ = chain_sha1_hash(input_str, iterations)
    end_time = time.time()

    elapsed_time = end_time - start_time
    assert elapsed_time < 5, f"Time taken: {elapsed_time:.2f} seconds"

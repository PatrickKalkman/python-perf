import hashlib
import timeit


def chain_sha1_hash(input_str, iterations=100_000):
    current_hash = input_str
    for _ in range(iterations):
        current_hash = hashlib.sha1(current_hash.encode()).hexdigest()
    return current_hash


if __name__ == "__main__":
    input_str = "Turbocharge Your Python Code"

    elapsed_time = timeit.timeit(
        'chain_sha1_hash(input_str)',
        setup='from __main__ import chain_sha1_hash, input_str',
        number=10
    )

    result = chain_sha1_hash(input_str)

    print(f"Result: {result}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

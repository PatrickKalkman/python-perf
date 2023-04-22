import hashlib


@profile
def chain_sha1_hash(input_str, iterations):
    current_hash = input_str
    for _ in range(iterations):
        current_hash = hashlib.sha1(current_hash.encode()).hexdigest()
    return current_hash


if __name__ == "__main__":
    input_str = "Turbocharge Your Python Code"
    result = chain_sha1_hash(input_str, 100_000)

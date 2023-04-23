import random
import string

# Generate a large dataset
data = {"".join(random.choices(string.ascii_lowercase, k=10)):
        random.randint(1, 100) for _ in range(100000)}


@profile
def lbyl_style(key, data):
    if key in data:
        return data[key]
    return None


@profile
def eafp_style(key, data):
    try:
        return data[key]
    except KeyError:
        return None


def main(hit_ratio):
    # Generate a list of random keys, some of which may not be in the dataset
    num_keys_to_check = 10000
    num_present_keys = int(num_keys_to_check * hit_ratio)
    num_missing_keys = num_keys_to_check - num_present_keys

    present_keys = random.sample(list(data.keys()), num_present_keys)
    missing_keys = ["".join(random.choices(string.ascii_lowercase, k=10))
                    for _ in range(num_missing_keys)]

    keys_to_check = present_keys + missing_keys
    random.shuffle(keys_to_check)

    for key in keys_to_check:
        lbyl_style(key, data)
        eafp_style(key, data)


if __name__ == "__main__":
    main(hit_ratio=0.5)

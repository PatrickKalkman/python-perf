import random

# This is a no-op if line_profiler is not installed
if "profile" not in globals():

    def profile(func):
        return func


@profile
def search_items(items_to_search, collection):
    count = 0
    for item in items_to_search:
        if item in collection:
            count += 1
    return count


@profile
def main():
    size = 1000000
    big_list = list(range(size))
    big_set = set(big_list)
    big_tuple = tuple(big_list)

    items_to_find = [random.randint(0, size) for _ in range(1000)]

    count_list = search_items(items_to_find, big_list)
    count_set = search_items(items_to_find, big_set)
    count_tuple = search_items(items_to_find, big_tuple)

    print(f"Found {count_list} items in list")
    print(f"Found {count_set} items in set")
    print(f"Found {count_tuple} items in tuple")


if __name__ == "__main__":
    main()

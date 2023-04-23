import random

# This is a no-op if line_profiler is not installed
if 'profile' not in globals():
    def profile(func):
        return func


def random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]


@profile
def list_comprehension(numbers):
    return [x ** 2 for x in numbers]


@profile
def generator_expression(numbers):
    return (x ** 2 for x in numbers)


def main():
    numbers = random_numbers(1000000)
    _ = list_comprehension(numbers)
    _ = generator_expression(numbers)


if __name__ == "__main__":
    main()

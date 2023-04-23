from collections import namedtuple
from dataclasses import dataclass

# This is a no-op if line_profiler is not installed
if 'profile' not in globals():
    def profile(func):
        return func


@profile
def create_datastructures():
    size = 100000

    # Dictionary
    d = {i: (2 * i, i ** 2) for i in range(size)}

    # Named Tuple
    Order = namedtuple('Order', 'order_id double_val square_val')
    namedtuples = [Order(i, 2 * i, i ** 2) for i in range(size)]

    # Data Class
    @dataclass
    class OrderDataClass:
        order_id: int
        double_val: int
        square_val: int

    dataclasses = [OrderDataClass(i, 2 * i, i ** 2) for i in range(size)]

    return d, namedtuples, dataclasses


def main():
    create_datastructures()


if __name__ == "__main__":
    main()

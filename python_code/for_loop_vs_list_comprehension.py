import random
from typing import List

def for_loop(orders: List[int]) -> List[int]:
    result = []
    for amount in orders:
        if amount > 50:
            result.append(amount * 2)
    return result

def list_comprehension(orders: List[int]) -> List[int]:
    return [amount * 2 for amount in orders if amount > 50]

@profile
def main():
    orders = [random.randint(0, 100) for _ in range(100000)]
    for_loop_result = for_loop(orders)
    list_comprehension_result = list_comprehension(orders)

if __name__ == "__main__":
    main()

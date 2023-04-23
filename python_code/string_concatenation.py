import random
import string

def random_string(length):
    return "".join(random.choices(string.ascii_lowercase, k=length))

def plus_operator(strings):
    result = ""
    for s in strings:
        result += s
    return result

def join_method(strings):
    return "".join(strings)

@profile
def main():
    strings = [random_string(10) for _ in range(10000)]

    plus_operator(strings)
    join_method(strings)

if __name__ == "__main__":
    main()

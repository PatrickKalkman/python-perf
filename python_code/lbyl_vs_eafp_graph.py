import random
import string
import timeit
import matplotlib.pyplot as plt  # type: ignore

plt.style.use("ggplot")

data = {"".join(random.choices(string.ascii_lowercase, k=10)):
        random.randint(1, 100) for _ in range(100000)}


def lbyl_style(key, data):
    if key in data:
        return data[key]
    return None


def eafp_style(key, data):
    try:
        return data[key]
    except KeyError:
        return None


def measure_performance(hit_ratio):
    num_keys_to_check = 10000
    num_present_keys = int(num_keys_to_check * hit_ratio)
    num_missing_keys = num_keys_to_check - num_present_keys

    present_keys = random.sample(list(data.keys()), num_present_keys)
    missing_keys = ["".join(random.choices(string.ascii_lowercase, k=10))
                    for _ in range(num_missing_keys)]

    keys_to_check = present_keys + missing_keys
    random.shuffle(keys_to_check)

    lbyl_time = timeit.timeit(lambda: [lbyl_style(key, data)
                                       for key in keys_to_check], number=1)
    eafp_time = timeit.timeit(lambda: [eafp_style(key, data)
                                       for key in keys_to_check], number=1)

    return lbyl_time, eafp_time


def main():
    # Vary hit_ratio from 0 to 1 in steps of 0.05
    hit_ratios = [i / 20 for i in range(21)]
    lbyl_times = []
    eafp_times = []

    for hit_ratio in hit_ratios:
        lbyl_time, eafp_time = measure_performance(hit_ratio)
        lbyl_times.append(lbyl_time)
        eafp_times.append(eafp_time)

    # Plot the results
    fig, ax = plt.subplots()
    ax.plot(hit_ratios, lbyl_times, label="LBYL", linewidth=2, marker='o')
    ax.plot(hit_ratios, eafp_times, label="EAFP", linewidth=2, marker='x')
    ax.set_xlabel("Hit Ratio", fontsize=12)
    ax.set_ylabel("Execution Time (s)", fontsize=12)
    ax.legend(fontsize=12)
    ax.set_title("Performance Comparison: LBYL vs EAFP", fontsize=14)

    # Customize tick labels
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Add grid
    ax.grid(True)

    plt.show()


if __name__ == "__main__":
    main()

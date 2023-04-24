import numpy as np
import random
from line_profiler import LineProfiler  # type: ignore


def double_list(initial_list):
    return [x * 2 for x in initial_list]


def double_array(initial_array):
    return initial_array * 2


size = 10_000_000
initial_list = [random.randint(0, 100) for _ in range(size)]
initial_array = np.random.randint(0, 100, size)

lp = LineProfiler()
lp.add_function(double_list)
lp.add_function(double_array)

lp.runctx("double_list(initial_list)", globals(), locals())
lp.runctx("double_array(initial_array)", globals(), locals())

lp.print_stats()

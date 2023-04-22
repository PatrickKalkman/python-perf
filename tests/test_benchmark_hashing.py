from measuring.time_function import chain_sha1_hash


def test_benchmark_chain_sha1_hash(benchmark):
    benchmark(chain_sha1_hash, "Turbocharge Your Python Code", 100_000)

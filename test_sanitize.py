import time
from sanitize import test_set_cap, sanitize, sanitize_sparse
from ddmin_alt import ddmin_alt
from ddmin_hybrid import ddmin_hybrid
from ddmin_random import ddmin_random
from ddmin import ddmin

def test_sanitize(test):
    ddmin_test = ddmin_time = 0
    ddmin_random_test = ddmin_random_time = 0
    ddmin_hybrid_test = ddmin_hybrid_time = 0
    ddmin_alt_test = ddmin_alt_time = 0
    test_size = 0

    for x in test:
        start_time = time.perf_counter()
        list = ddmin(sanitize, x)
        ddmin_time += (time.perf_counter() - start_time) * 1e9  # Convert to nanoseconds
        ddmin_test += list[2]

        start_time = time.perf_counter()
        list = ddmin_random(sanitize, x)
        ddmin_random_time += (time.perf_counter() - start_time) * 1e9
        ddmin_random_test += list[2]

        start_time = time.perf_counter()
        list = ddmin_hybrid(sanitize, x)
        ddmin_hybrid_time += (time.perf_counter() - start_time) * 1e9
        ddmin_hybrid_test += list[2]

        start_time = time.perf_counter()
        list = ddmin_alt(sanitize, x)
        ddmin_alt_time += (time.perf_counter() - start_time) * 1e9
        ddmin_alt_test += list[2]

        test_size += len(x)

    num_tests = len(test)
    print("test_set")
    print("Avg # of tests ddmin: ", ddmin_test / num_tests)
    print("Avg # of tests ddmin_random: ", ddmin_random_test / num_tests)
    print("Avg # of tests ddmin_hybrid: ", ddmin_hybrid_test / num_tests)
    print("Avg # of tests ddmin_alt: ", ddmin_alt_test / num_tests)
    print("Avg elements in test: ", test_size / num_tests)

    print("\nRuntime Analysis (in nanoseconds)")
    print(f"Avg runtime ddmin: {ddmin_time / num_tests:.2f} ns")
    print(f"Avg runtime ddmin_random: {ddmin_random_time / num_tests:.2f} ns")
    print(f"Avg runtime ddmin_hybrid: {ddmin_hybrid_time / num_tests:.2f} ns")
    print(f"Avg runtime ddmin_alt: {ddmin_alt_time / num_tests:.2f} ns")

test = test_set_cap()
test1 = test[0]
test2 = test[1]

test_sanitize(test1)
test_sanitize(test2)


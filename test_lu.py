#We are using the ddmin implementation from Andreas Zeller's Debugging Book library, we will be making edits but the majority
#of the function will be the same. 
# pip install debuggingbook

from typing import Sequence, Any, Callable, Optional, Type, Tuple, Dict, Union, Set, FrozenSet, List 
from types import FrameType, TracebackType 

def ddmin(test: Callable, inp: Sequence[Any], *test_args: Any) -> Sequence:
    """
    Reduce `inp` to a 1-minimal failing subset, using the outcome
    of `test(inp, *test_args)`, which should be `PASS`, `FAIL`, or `UNRESOLVED`.
    """

    PASS = 'PASS'
    FAIL = 'FAIL'
    UNRESOLVED = 'UNRESOLVED'

    assert test(inp, *test_args) != PASS

    n = 2  # Initial granularity
    list = [] #Records all tested sets
    tests = 0 #Records the # of tests run
    while len(inp) >= 2:
        start: int = 0  # Where to start the next subset
        subset_length: int = int(len(inp) / n)
        some_complement_is_failing: bool = False

        while start < len(inp):
            tests = tests + 1
            # Cut out inp[start:(start + subset_length)]
            complement: Sequence[Any] = \
                inp[:start] + inp[start + subset_length:]
            
            list.append(complement) #Only add things that we test into the list, everything else doesn't matter 

            if test(complement, *test_args) == FAIL:
                # Continue with reduced input
                inp = complement
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break

            # Continue with next subset
            start += subset_length

        if not some_complement_is_failing:
            # Increase granularity
            if n == len(inp):
                break
            n = min(n * 2, len(inp))

    return inp, list, tests

def ddmin_random(test: Callable, inp: Sequence[Any], *test_args: Any) -> Sequence:
    """
    Reduce `inp` to a 1-minimal failing subset, using the outcome
    of `test(inp, *test_args)`, which should be `PASS`, `FAIL`, or `UNRESOLVED`.
    """
    import random, sys

    PASS = 'PASS'
    FAIL = 'FAIL'
    UNRESOLVED = 'UNRESOLVED'

    assert test(inp, *test_args) != PASS

    n = 2  # Initial granularity
    list = [] #Records all tested sets
    tests = 0 #Records the # of tests run

    rand = random.randint(2, len(inp))
    n = rand

    while len(inp) >= 2:
        tests = tests + 1
        start: int = 0  # Where to start the next subset
        subset_length: int = int(len(inp) / n)
        some_complement_is_failing: bool = False

        while start < len(inp):
            # Cut out inp[start:(start + subset_length)]
            complement: Sequence[Any] = \
                inp[:start] + inp[start + subset_length:]
            
            list.append(complement) #Only add things that we test into the list, everything else doesn't matter 

            if test(complement, *test_args) == FAIL:
                # Continue with reduced input
                inp = complement
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break

            # Continue with next subset
            start += subset_length

        if not some_complement_is_failing:
            # Increase granularity
            if n == len(inp):
                break
            n = min(n * 2, len(inp))

    return inp, list, tests

from sanitize import test_set_cap, sanitize

test = test_set_cap()
list = []
for x in test:
    print("\ninput: ", x)
    list = ddmin(sanitize, x)
    print("ddmin")
    print("minimum: ", list[0])
    print("tests: ", list[2])
    print(list[1])

    list = ddmin_random(sanitize, x)
    print("\nrand")
    print("minimum: ", list[0])
    print("tests: ", list[2])
    print(list[1])
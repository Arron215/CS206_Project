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

    list = [] #Records all tested sets
    list.append(inp)
    assert test(inp, *test_args) != PASS

    tests = 0 #Records the # of tests run
    rand = random.randint(2, len(inp)) 
    n = 2

    while len(inp) >= 2:
        tests = tests + 1
        start: int = random.randint(1, len(inp)-1)  # Where to start the next subset
        subset_length: int = int(len(inp) / n)
        some_complement_is_failing: bool = False

        while start < len(inp):
            # Cut out inp[start:(start + subset_length)]
            if ((start+subset_length) > len(inp)):
                remaining = (start+subset_length)
                complement: Sequence[Any] = \
                    inp[start:] + inp[0:remaining]
            else:
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

def ddmin_hybrid(test: Callable, inp: Sequence[Any], *test_args: Any) -> Sequence:
    """
    Reduce `inp` to a 1-minimal failing subset, using the outcome
    of `test(inp, *test_args)`, which should be `PASS`, `FAIL`, or `UNRESOLVED`.
    """
    import random, sys

    PASS = 'PASS'
    FAIL = 'FAIL'
    UNRESOLVED = 'UNRESOLVED'

    list = [] #Records all tested sets
    list.append(inp)
    revert = len(inp)/2
    assert test(inp, *test_args) != PASS

    tests = 0 #Records the # of tests run
    rand = random.randint(2, len(inp)) 
    n = 2

    while len(inp) >= 2:
        tests = tests + 1
        if (len(inp) >= revert):
            start: int = random.randint(1, len(inp)-1)  # Where to start the next subset
        else: 
            start: int = 0
        subset_length: int = int(len(inp) / n)
        some_complement_is_failing: bool = False

        while start < len(inp):
            # Cut out inp[start:(start + subset_length)]
            if ((start+subset_length) > len(inp)):
                remaining = (start+subset_length)
                complement: Sequence[Any] = \
                    inp[start:] + inp[0:remaining]
            else:
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

#Iteratively, we pick a random point and attempt to split the input until we find two parts—one buggy and one not.
# We continue this process until further splitting is not possible.  
# At that point, we switch back to the original ddmin.  
def ddmin_alt(test: Callable, inp: Sequence[Any], *test_args: Any) -> Sequence:
    import random

    PASS = 'PASS'
    FAIL = 'FAIL'

    tested = []  # Records tested subsets
    assert test(inp, *test_args) == FAIL  # Input must start as FAIL

    trial = 0 # counter for tried random points 
    while True:
        if len(inp) < 2:
            break  # No further splitting possible

        start = random.randint(1, len(inp) - 1)  # Random split point

        # Split the input into two parts
        part1 = inp[:start]
        part2 = inp[start:]

        # Avoid redundant tests
        if part1 in tested and part2 in tested:
            if trial == len(inp):
                break  # All possible points are tried, no further splitting is possible
            continue

        trial += 1
        tested.append(part1)
        tested.append(part2)

        # Test both parts
        test_p1 = test(part1, *test_args)
        test_p2 = test(part2, *test_args)

        if test_p1 == FAIL and test_p2 != FAIL:
            inp = part1  # Continue with the failing part
            trial = 0  # Reset the trial counter
        elif test_p2 == FAIL and test_p1 != FAIL:
            inp = part2  # Continue with the failing part
            trial = 0  # Reset the trial counter
        else:
            # Neither is isolated or both fail, try another split point
            continue

    return ddmin(test, inp, *test_args) # fall back to original delta debugging algorithm at the end.


from sanitize import test_set_cap, sanitize

test = test_set_cap()
test1 = test[0]
test2 = test[1]
list = []
ddmin_test = 0
test_size = 0
ddmin_random_test = 0
ddmin_hybrid_test = 0
ddmin_alt_test = 0


for x in test1:
    #print("\ninput: ", x)
    list = ddmin(sanitize, x)
    #print("ddmin")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_test = ddmin_test + list[2]
    #print(list[1])

    list = ddmin_random(sanitize, x)
    #print("\nrand")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_random_test = ddmin_random_test + list[2]
    #for i in list[1]:
    #    print(i, len(i))

    list = ddmin_hybrid(sanitize, x)
    #print("\nhybrid")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_hybrid_test = ddmin_hybrid_test + list[2]
    #print(list[1])

    #print("\ninput: ", x)
    list = ddmin_alt(sanitize, x)
    #print("ddmin")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_alt_test = ddmin_alt_test + list[2]
    #print(list[1])

    test_size = test_size + len(x)

ddmin_test = ddmin_test/len(test1)
ddmin_random_test = ddmin_random_test/len(test1)
ddmin_hybrid_test = ddmin_hybrid_test/len(test1)
ddmin_alt_test = ddmin_alt_test/len(test1)
test_size = test_size/len(test1)

print("test_set")
print("Avg # of tests ddmin: ", ddmin_test)
print("Avg # of tests ddmin_random: ", ddmin_random_test)
print("Avg # of tests ddmin_hybrid: ", ddmin_hybrid_test)
print("Avg # of tests ddmin_alt: ", ddmin_alt_test)
print("Avg elements in test: ", test_size)

for x in test2:
    #print("\ninput: ", x)
    list = ddmin(sanitize, x)
    #print("ddmin")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_test = ddmin_test + list[2]
    #print(list[1])

    list = ddmin_random(sanitize, x)
    #print("\nrand")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_random_test = ddmin_random_test + list[2]
    #for i in list[1]:
    #    print(i, len(i))

    list = ddmin_hybrid(sanitize, x)
    #print("\nhybrid")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_hybrid_test = ddmin_hybrid_test + list[2]
    #print(list[1])

    #print("\ninput: ", x)
    list = ddmin_alt(sanitize, x)
    #print("ddmin")
    #print("minimum: ", list[0])
    #print("tests: ", list[2])
    ddmin_alt_test = ddmin_alt_test + list[2]
    #print(list[1])

    test_size = test_size + len(x)

ddmin_test = ddmin_test/len(test2)
ddmin_random_test = ddmin_random_test/len(test2)
ddmin_hybrid_test = ddmin_hybrid_test/len(test2)
ddmin_alt_test = ddmin_alt_test/len(test2)
test_size = test_size/len(test2)

print("test_set_sparse")
print("Avg # of tests ddmin: ", ddmin_test)
print("Avg # of tests ddmin_random: ", ddmin_random_test)
print("Avg # of tests ddmin_hybrid: ", ddmin_hybrid_test)
print("Avg # of tests ddmin_alt: ", ddmin_alt_test)
print("Avg elements in test: ", test_size)

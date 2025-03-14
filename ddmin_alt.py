from typing import Sequence, Any, Callable, Optional, Type, Tuple, Dict, Union, Set, FrozenSet, List 
from types import FrameType, TracebackType 

#Iteratively, we pick a random point and attempt to split the input until we find two parts—one buggy and one not.
# We continue this process until further splitting is not possible.  
# At that point, we switch back to the original ddmin.  
def ddmin_alt(test: Callable, inp: Sequence[Any], *test_args: Any) -> Sequence:
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
    max_tests = len(inp)
    revert = 0
    tested = []
    assert test(inp, *test_args) != PASS

    tests = 0 #Records the # of tests run
    n = 2

    while len(inp) >= 2:
        tests = tests + 1
        if not revert:
            start: int = random.randint(1, len(inp)-1)  # Where to start the next subset
        else: 
            start: int = 0
        subset_length: int = int(len(inp) / n)
        some_complement_is_failing: bool = False

        while start < len(inp):
            # Cut out inp[start:(start + subset_length)]
            complement: Sequence[Any] = \
                inp[:start + subset_length]            
            list.append(complement) #Only add things that we test into the list, everything else doesn't matter

            if not revert:
                tests += 1
                remaining = len(inp)
                c2: Sequence[Any] = \
                    inp[start + subset_length:] 
                if (complement in tested) | (c2 in tested):
                    break
                list.append(c2)
                test_cmp = test(complement, *test_args)
                test_inp = test(c2 ,*test_args) 
                tested.append(complement)
                tested.append(c2)

                if (test_cmp != test_inp):
                    if(test_cmp == FAIL):
                        inp = complement
                        break
                    else: 
                        inp = c2
                        break
                else:
                    if (tests == max_tests): #Done with all possible tests, no hit
                        revert = 1
                    break

            if (revert):
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



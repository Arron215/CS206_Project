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
                inp[:start] + inp[start + subset_length:]
            list.append(complement) #Only add things that we test into the list, everything else doesn't matter

            if not revert:
                c2: Sequence[Any] = \
                    inp[:start] + inp[start + subset_length:]
                if (complement in tested) | (c2 in tested):
                    break
                test_cmp = test(complement, *test_args)
                test_inp = test(c2 ,*test_args) 
                tested.append(complement)
                tested.append(c2)

                if (test_cmp != test_inp):
                    revert = 1
                    if(test_cmp == FAIL):
                        inp = test_cmp
                        break
                    else: 
                        inp = test_inp
                        break
                else:
                    if (tests == len(inp)): #Done with all possibel tests, no hit
                        revert = 1
                        break
                    else:
                        break

            else:
                if (revert):
                    if test(complement, *test_args) == FAIL:
                        # Continue with reduced input
                        inp = complement
                        n = max(n - 1, 2)
                        some_complement_is_failing = True
                        break
            

            # Continue with next subset
            start += subset_length

        if revert:
            if not some_complement_is_failing:
                # Increase granularity
                if n == len(inp):
                    break
                n = min(n * 2, len(inp))
        
    return inp, list, tests

from sanitize import test_set_cap, sanitize

test = test_set_cap()
#test = ['a\\b']
list = []
ddmin_test = 0
test_size = 0
ddmin_random_test = 0
ddmin_hybrid_test = 0

for x in test:
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

    test_size = test_size + len(x)

ddmin_test = ddmin_test/len(test)
ddmin_random_test = ddmin_random_test/len(test)
ddmin_hybrid_test = ddmin_hybrid_test/len(test)
test_size = test_size/len(test)

print("Avg # of tests ddmin: ", ddmin_test)
print("Avg # of tests ddmin_random: ", ddmin_random_test)
print("Avg # of tests ddmin_hybrid: ", ddmin_hybrid_test)
print("Avg elements in test: ", test_size)
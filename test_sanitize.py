from sanitize import test_set_cap, sanitize, sanitize_sparse
from ddmin_alt import ddmin_alt
from ddmin_hybrid import ddmin_hybrid
from ddmin_random import ddmin_random
from ddmin import ddmin

def test_sanitize(test):
    ddmin_test = 0
    test_size = 0
    ddmin_random_test = 0
    ddmin_hybrid_test = 0
    ddmin_alt_test = 0
    
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

        list = ddmin_alt(sanitize, x)
        #print("\nhybrid")
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

    return ddmin_test, ddmin_random_test, ddmin_hybrid_test, ddmin_alt_test, test_size

test = test_set_cap()
test1 = test[0]
test2 = test[1]

ddmin_test, ddmin_random_test, ddmin_hybrid_test, ddmin_alt_test, test_size = test_sanitize(test1)
ddmin_test, ddmin_random_test, ddmin_hybrid_test, ddmin_alt_test, test_size = test_sanitize(test2)

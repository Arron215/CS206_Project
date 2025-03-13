def test()
    from sanitize import test_set_cap, sanitize

    test = test_set_cap()
    test1 = test[0]
    test2 = test[1]
    list = []
    ddmin_test = 0
    test_size = 0
    ddmin_random_test = 0
    ddmin_hybrid_test = 0

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

        test_size = test_size + len(x)
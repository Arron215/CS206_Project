def divide_largest_by_smallest(arr):
    largest = max(arr)
    smallest = min(arr)

    # Intentionally commented out to introduce bug
    # if smallest == 0:
    #     return 0

    return largest / smallest

def test_set_cap():
    import random

    test_set = []
    test_set_sparse = []

    while len(test_set) < 1000:
        # Generate a random array of integers
        entry = [random.randint(1, 100) for _ in range(random.randint(2, 100))]
        
        # Add zero to the array to make sure it will fail
        entry.append(0)
        random.shuffle(entry)
        
        test_set.append(entry)

    while len(test_set_sparse) < 1000:
        # Generate sparse arrays where some have zero and others don't
        entry = [random.randint(1, 100) for _ in range(random.randint(2, 100))]
        
        # Add zero in a sparse manner
        if random.random() < 0.1:
            entry.append(0)  # Occasionally add zero to make sure it will fail
        
        random.shuffle(entry)
        test_set_sparse.append(entry)
    
    random.shuffle(test_set)

    return test_set, test_set_sparse

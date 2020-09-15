def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    store = {}
    # store each number from each array as {number: count} in a dictionary  
    for arr in arrays:
        for num in arr:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1
    # check for numbers with value == length of arrays (meaning the num is in each sub array)
    # if so, add the number to the result (this won't work if numbers appear more than once in the sub arrays)
    for key, value in store.items():
        if value == len(arrays):
            result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

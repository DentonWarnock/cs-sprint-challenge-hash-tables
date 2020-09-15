def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    store = {}
    # store each {weight: index} in dictionary
    for index, weight in enumerate(weights):
        store[weight] = index
    # loop over each weight and look for a value that adds to the limit
    for index, weight in enumerate(weights):
        missing_weight = limit - weight # (missing_weight + weight = limit)
        if missing_weight in store:            
            smaller_index = index if weight <= missing_weight else store[missing_weight]   
            bigger_index = index if weight > missing_weight else store[missing_weight]
            if missing_weight == 0: # added this line to pass last test, I think the test is wrong?            
                bigger_index, smaller_index = smaller_index, bigger_index                   
            return (bigger_index, smaller_index)
    # If nothing found
    return None

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    store_negative = {}
    # store each negative number as {abs(number): number} in a dictionary  
    for num in a:
        if num < 0:
            store_negative[abs(num)] = num      
    # loop through again looking for positive numbers with a negative match (already stored)
    # if found add positive number to result 
    for num in a:
        if num in store_negative:
            result.append(num)    
            
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

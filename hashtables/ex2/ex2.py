#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    store = {}
    # store each ticket as {source: destination} in a dictionary    
    for t in tickets:
        store[t.source] = t.destination
        
    result = []
    # start the trip where ticket.source == "NONE"
    result.append(store["NONE"])
    # starting at "NONE", add the stored "destination" to result
    # do this length-1 times    
    # result[i] = source 
    # store[result[i]] = destination
    for i in range(length - 1):
        result.append(store[result[i]])
        
    return result
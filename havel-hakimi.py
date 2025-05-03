def havel_hakimi(deg_seq):
    """
    Determines if a given degree sequence is graphic using the Havel-Hakimi algorithm.
 
    Parameters:
    deg_seq (list of int): A list of nonnegative integers representing the degrees.
 
    Returns:
    bool: True if the sequence is graphic, False otherwise.
    """
    # Step 1: Sort the sequence in descending order for convenience.
    seq = sorted(deg_seq, reverse=True)
 
    while True:
        # Step 2: Remove all zeros (any vertex with degree 0 doesn't affect the process).
        seq = [d for d in seq if d > 0]
 
        # If the sequence is empty after removing zeros, it means all degrees are satisfied -> graphic
        if not seq:
            return True
 
        # Sort again in descending order to ensure we always pick the largest remaining degree first
        seq.sort(reverse=True)
 
        # Step 3: Take the first (largest) element, call it D
        D = seq[0]
        # Remove that element from the sequence
        seq = seq[1:]
 
        # If D is larger than the length of the remaining list, we can't subtract from enough vertices
        # -> not graphic
        if D > len(seq):
            return False
 
        # Step 4: Subtract 1 from the next D elements
        for i in range(D):
            seq[i] -= 1
            # If any element goes below 0, it means there's an impossible requirement -> not graphic
            if seq[i] < 0:
                return False
 
def example_usage():
    """
    Demonstrates how to use the havel_hakimi function.
    """
    # Example degree sequence
    example_list = [3,3,2,2,2,1]
 
    # Print "Graphic?" if the sequence is graphic, otherwise "Not Graphic"
    print("Graphic?" if havel_hakimi(example_list) else "Not Graphic")

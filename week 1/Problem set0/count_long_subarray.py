def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 1   # number of longest increasing subarrays in A[:i]
    length = 1  # length of longest increasing subarrays in A[:i]
    current = 1  # length of longest increasing subarrays now
    for i in range(1,len(A)):
        if A[i-1] < A[i]:
            current += 1
        else:
            current = 1
        if length == current:
            count += 1
        elif current > length:
            count = 1
            length = current
    return count

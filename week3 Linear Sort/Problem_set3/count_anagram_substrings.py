ORD_A = ord('a')
def lower_ord(c):
    return ord(c) - ORD_A

def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    F = [0] * 26 # the array of frequency table
    D = {}
    m,n,k = len(T),len(S),len(S[0])
    # compute the frequency tale of T
    for i in range(m):
        F[lower_ord(T[i])] += 1
        if i > k - 1:
            F[lower_ord(T[i - k])] -= 1  # next k freq
        if i >= k - 1:  # sort into dict
            key = tuple(F)
            if key in D: D[key] += 1
            else: D[key] = 1
    # countA
    A = [0] * n
    for j in range(n):
        F = [0] * 26
        for c in S[j]:
            F[lower_ord(c)] += 1
        key = tuple(F)
        if key in D: A[j] = D[key]
    return tuple(A)

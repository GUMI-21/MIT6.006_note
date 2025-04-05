# LCS
def longest_common_subsequence(A: str, B: str) -> str:
    n, m = len(A), len(B)
    # dp[i][j] represent A[i:] and B[j:], +1 correspond to Basecase
    dp = [[0] * (m+1) for _ in range(n+1)]
    # bottom up n-1....0 in topological order
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    # recover LCS string: the original problem
    i = j = 0
    lcs = []
    while i < n and j < m:
        if A[i] == B[j]:
            lcs.append(A[i])
            i += 1
            j += 1
        elif dp[i+1][j] > dp[i][j+1]:
            i+=1
        else:
            j+=1
    return ''.join(lcs)

def longest_increasing_subsequence(A: str) -> str:
    """
    Finds the longest increasing subsequence (LIS) of a string A.
    Args:
        A: The input string.
    Returns:
        The LIS as a string.
    """
    n = len(A)
    # dp[i] stores the length of the LIS starting at index i
    dp = [0] * (n + 1)
    # dp process (topological order: i = |A|-1, ..., 0)
    for i in range(n - 1, -1, -1):
        dp[i] = 1 + max(
            (dp[j] for j in range(i + 1, n) if A[i] < A[j]),
            default=0  # If no such j exists, the LIS starting at i is just A[i] itself
        )
    # Recover LIS string from DP
    return recover_lis_concise(A,dp)

def recover_lis_concise(A, dp):
    n = len(A)
    lis_length = max(dp)
    index = dp.index(lis_length)
    lis = [A[index]]
    length = lis_length - 1
    for i in range(index + 1, n):
        if dp[i] == length and A[i] > lis[-1]:  # Key: dp[i] == length
            lis.append(A[i])
            length -= 1
            if length == 0:
                break
    return "".join(lis)
# Test cases

if __name__ == '__main__':
    # Test cases
    print(longest_increasing_subsequence("CARBOHYDRATE"))  # Expected: ABORT
def fibonacci(n):
    if n <= 1:
        return n
    dp = [None for _ in range(n)]
    # base case
    dp[0] = 1
    dp[1] = 1
    # DP
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

if __name__ == '__main__':
    print(fibonacci(10))
+ 斐波那契数列
f(n) = f(n-1) + f(n-2)
=> dp[n] = dp[n-1] + dp[n-2]
+ 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数
dp[i]： 爬到第i层楼梯，有dp[i]种方法
dp[i] = dp[i - 1] + dp[i - 2]
到i 有两种办法 i-1 -> i, i-2 -> i => dp[i - 1] + dp[i - 2] 这两种方法的和就是dp[i] 方法的总数
base case: dp[1] = 1, dp[2] = 2
+ LCS  longest common sequence
![[Pasted image 20250527104923.png]]

## Recall
SRTBOT paradigm for recursive alg. design & with memoization DP algorithm desion.
-Subproblem definition
+ for sequence S try prefixes S[:i], suffixes S[i:] Substring S[i:j]
+ for nonnegative integer K, try integers in [0,k]
+ add Subproblems & constraints to "remember state"
-Relate subproblem solutions recursively
+ identify guestion about subproblem solution that if you knew answer, reduces to "smaller" subproblems
+ locally brute-force all answers to question
+ can think of correctly guessing answer, then loop
-Topological order on subprobs => DAG
-Base case of relation
-original problem
-Time analysis
$$\sum_{x\in X} \text{work}(x), \text{ or if } \text{work}(x) = O(W) \text{ for all } x \in X, \text{ then } |X| \cdot O(W)$$
*   work(x) measures **nonrecursive** work in relation; treat recursions as taking O(1) time
## Rod cutting:
given rod of lenght L & value V(l) of rod of length l for all $l \in \{1,2,...L\}$
what's max-value partition of length-l rod?
-example: L=7, 
l:     1 2   3   4   5   6   7
v(l): 1 10 13 18 20 31 32
-> 6+1 -> 31+1=32
 or 3 + 2 + 2 = 13 + 10 + 10 = 33  the best
 + SRTBOT
-Subproblems:
x(l) = max value partition of length l for l = 0,1,....,L
-Relate:
X(l) = max {v(p) + X(l-p) | for p in 1 <= p <= l}
-Topo. order:
increasing l, for l = 0, 1, ....., L
-Base case: x(0) = 0
-Original: x(L)
-Time: $\theta(L)\ subprobs. * O(L) time = O(L^2) time$
Is $\theta(L^2)$ polynomial time?  Yes
**(Strongly) polynomial time = polynomial in input size (measured in words)**
## Subset Sum
given multiset A=$\{a_0,a_1,a_2,....,a_\{n-1\}\}$ of n integers & target sum T, does any subset S <= A sum to T ?
-example: A = {2, 5, 7, 8, 9}  T = 21, 25
for 21 => YES, S={5,7,8}
for 25 => NO
-decision problem:  YES/NO answer
+  SRTBOT for (SS)
-Subproblems:
X(i, t) = does any subset S in A[i:] sum to t, for i = 0,1,...,n,  t = 0,1,...,T
-Relate
X(i, t) = OR(any) {x(i+1, t), <- a_i not in S, 
x(i+1, t-a_i) if a_i <= t}
-Topological order: decreasing i
-Base case: x(n,t) = { if t=0, yes; otherwise no.}
-Original problem: X(0,T)
-Time: theta(nT)
![[QQ_1744023051125.png]]
->
Is $\theta(nT)$ is polynomial time? NO: not polynomial input size of n+1
->Beacuse input is size n+1
-know T <= 2^w , w >= lgn, but w could be >> lgn, e.g. w=n, T<=2^n
means nT could be exponential in n+1
->this is a *pseudo-polynomial*
#### Pseudopolynomial
polynomial input size & input integers (T)
=>polynomial if input intergers <= polynomial input size
others
-counting sort, DAA, Fibonacci, Rdix sort   pseudopoly

![[QQ_1744096761521.png]]
## Main features of DP
+ Subpreoblems
-prefixes/suffixes:  Bowling game,LCS, LIS, Floyd-warshall, subset sum
-substrings: ACG, Paren
-multiple sequences: LCS
-integers:  Rod Cutting, Subset sum, Fibonacci
	-pseudopolynomial
-vertices
+ Subproblem constraints / expansion
-nonexpansive constraint: LIS
-2x: ACG, P
-$\theta(1)x$: Piano
-$\theta(n)x: Bellman-Ford$
![[QQ_1744030163659.png]]
## Supplement
+ Subproblem Expension
在动态规划的子问题中，在尝试解决一个特定的子问题时，我们发现为了得到最优解，需要更多的信息或者状态，这通常意味着子问题需要进一步的进行分解，或者考虑额外的约束条件。
Introduce these missing information or constraint.!

+ Guess and Brute Force
In subproblem, we Brute Force All possiable situation.

![[QQ_1744096902843.png]]
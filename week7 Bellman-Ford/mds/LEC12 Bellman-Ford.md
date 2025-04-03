3.30 https://github.com/GUMI-21/MIT6.006_note
## Previously
+ weighted graphs
shortest-path weight, negative-weight cycles
+ BFS positive weighted graphs
+ DAG Relaxtion
algorithm to solve SSSP on a weighted DAG in O(|V | + |E|) time
+ SSSP for graph with negative weights
-Compute $\delta(s,v)$ for all $v \in V$ ($-\infty$if v reachable via negative-weight cycle)
-if a negative-weight cycle reachable from s, return one

**for this lecture, we restrict our discussion to directed graphs**
![[QQ_1743305329814.png]]
## Warmup Exercise
+ Ex1: Given undirected graph G, return whether G contains a negative weight cycle
every edge with negative edge can be a cycle.
+ Ex2: If have Alg A solves SSSP in O(|V|(|V|+|E|))
Show how to solve SSSP in O(|V|·|E|)
*Use BFS or DFS find all the things reachable from S, and throw ohters away, then I have a graph which V is asymptotically no bigger than E, means O(|V|(|V|+|E|) = O(|V||E|)*
## Simple Shortest Paths
If graph does not contain negative-weight cycles, shortest paths are simple!
+ Claim 1: If δ(s, v) is finite, there exists a shortest path from s to v is *simple*
*PROOF*: By contradiction
Assume there is a cycle in the path from s to v, two case: 1.the cycle weight is negative, contradiction, -> -infinite. 2.the cycle weight is 0 or negative, I can just erase the cycle to get the shortest path.
![[QQ_1743318585366.png]]
+ simple paths cannot repeat vertices, finite shortest paths contain at most |V | − 1 edges
So the Shortest path is simple, and *|E| <= |V| - 1*
#### Negative Cycle Witness
* then a Idea
What if I limit the number of edges when find the shortest weighted path?
this is called *k-Edges Distance $\delta _k(s,v)$: shortest s-v path using <= k edges*
+ *A Statement*
If $\delta_{|V|}(s,v) < \delta_{|V|-1}(s,v)$, then $\delta(s,v) = -\infty$
---If I can find a vertex that has this property, **this vertex is called a witness**.---
+ *Claim 2* if $\delta(s,v)=-\infty$,then v is reachable from a witness.
Proof: By contradiction
Alenative: Prove every negative weighted cycle contains witness
Think there is a Cycle with negative weighted, select a vetex v and his predeccessor v'. Then $\delta_{|v|}(s,v) <= \delta_{|v|-1}(s,v') + w(v',v)$
then take this equation to all cycle vertices, sum of w(v',v) is the weight of cycle which is negative, then erase the w equation give $\delta_{|v|}(s,v) < \delta_{|v|-1}(s,v')$, which means if there isn't witness in cycle there will be a constrcution of the defination of witness. proved.
## Bellman-Ford
**see the R12 note whit the original Bellman-Ford, it's easier to understand!**
#### A modified Bellman-Ford
+ Idea! Use graph duplication: make multiple copies (or levels) of the graph
this is a very common technique.
=> Make |v| + 1 levels, $V_k$ in level k represents reaching vertex v using at most k edges.
If we connect edges from one level to only higher levels, then the graph is DAG!
![[QQ_1743323644021.png]]
+ ALG
-Construct G' |V|(|V| + 1) vertices, |V||V| + |V||E| = |V|(|V| + |E|) edges
-Run DAG Relaxation from $S_0$ compute $\delta(s_0,v_k)$ fro k = {0,...,|V|}
-For each vertex V: set d(S,V) = $\delta(S_0,V_{|V|-1})$
+ Claim: $\delta(S_0,V_k) = \delta(S,V)$
-For each witness u in V, $\delta(s_o,u_{|v|}) < \delta(s_0,u_{|v|-1})$
-for each v reachable from u, set d(s,v) = -infinty
+ EXAMPLE from Note
![[QQ_1743331247637.png]]
#### Correctness
+ Claim3: δ(s0, vk) = δk(s, v) for all v ∈ V and k ∈ {0, . . . , |V |}

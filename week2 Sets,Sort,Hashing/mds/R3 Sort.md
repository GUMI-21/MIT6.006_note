3.22 https://github.com/GUMI-21/MIT6.006_note
## Sorted Array
we can simply binary search to find keys and support Order operations!
![[QQ_1742642916512.png]]
## Sorting
+ Selection sort maintains and grows a subset the largest i items in sorted order. 
+ Insertion sort maintains and grows a subset of the first i input items in sorted order.
#### Selection sort
Having already sorted the largest items into sub-array A[i+1:], the algorithm repeatedly scans the array for the largest item not yet sorted and swaps it with item A[i].
runtime: O(n^2)
`see code in r3.py`

#### Insertion Sort
Having already sorted sub-array A[:i], the algorithm repeatedly swaps item A[i] with the item to its left until the left item is no larger than A[i].
	`see code in r3.py`
#### In-place and Stability
+ in-place
using at most a constant amount of additional space. 
+ stable
Insertion sort is stable. 
meaning that items having the same value will appear in the sort in the same order as they appeared in the input array.
#### Merge Sort
o T(n) = Θ(n log n).
In particular, log n grows slower than any polynomial n^ε for ε > 0
`see code in r3.py`
## Recurrences
+ Substitution: Guess a solution and substitute to show the recurrence holds.
+ Recursion Tree: Draw a tree representing the recurrence and sum computation at nodes. This is a very general method, and is the one we’ve used in lecture so far.
+ Master Theorem: A general formula to solve a large class of recurrences. It is useful, but can also be hard to remember.
#### Master Theorem
![[QQ_1742647729744.png]]
![[QQ_1742647733950.png]]
# Exercies

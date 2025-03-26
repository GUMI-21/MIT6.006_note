3.22 https://github.com/GUMI-21/MIT6.006_note
## Sequence Interface
Sequences maintain a collection of items in an extrinsic order, where each item stored has a rank in the sequence, including a first item and a last item.
Sequences are generalizations of stacks and queues, which support a subset of sequence operations.
![[QQ_1742635104870.png]]
## Set Interface
By contrast, Sets maintain a collection of items based on an intrinsic property involving what the items are, usually based on a unique key, x.key, associated with each item x. Sets are generalizations of dictionaries and other intrinsic query databases.
![[QQ_1742635297130.png]]
## Implementations
![[QQ_1742635388121.png]]
## Array Sequence
place fixed
## Linked List Sequence
`code see r2_linked_list.py`
also called pointer-based or linked.
their constituent items can be stored anywhere in memory.
## Dynamic Array Sequnce
One straight-forward way to support faster insertion would be to over-allocate additional space when you request space for the array.
+ How python does   : it doesn’t
*amortized constant time*
A typical implementation of a dynamic array will allocate double the amount of space needed to store the current array, sometimes referred to as table doubling. H
Python Lists allocate additional space according to the following formula (from the Python source code written in C): 1 new_allocated = (newsize >> 3) + (newsize < 9 ? 3 : 6);

When attempting to append past the end of the allocation, the contents of the array are transferred to an allocation that is twice as large. When removing down to one fourth of the allocation, the contents of the array are transferred to an allocation that is half as large.

how amortized constant append and pop could be implemented. 
# Exercise
1.Suppose the next pointer of the last node of a linked list points to an earlier node in the list, creating a cycle. Given a pointer to the head of the list (without knowing its size), describe a linear-time algorithm to find the number of nodes in the cycle. Can you do this while using only constant additional space outside of the original linked list?

answer: use tow pointers pointing at the head of the linked list.Use Fast-slow pointers.
slow pointer: move to next
fast pointer: inital at head.next and move to next.next
when slow equal fast means fast point has made a full loop around cycle, then fixed slow pointer, make fast pointer take one step until slow pointer again to count nodes in cycle.

2.Given a data structure implementing the Sequence interface, show how to use it to implement the Set interface. (Your implementation does not need to be efficient.)

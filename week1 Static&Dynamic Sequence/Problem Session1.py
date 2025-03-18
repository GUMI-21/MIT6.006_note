# problem1-2
# a
def swap_ends(D):
	first = D.delete_first()
	last = D.delete_last()
	D.insert_first(last)
	D.insert_last(first)
# b 1.
def shift_left(D, k):
    # check
    if (k<1) or (k > len(D) - 1):
        return
    for i in range (0,k):
        D.insert_last(D.delete_first())
# b 2
def shift_left(D, k):
    # check
    if (k<1) or (k > len(D) - 1):
        return
    x = D.delete_first()
    D.insert_last(x)
    shift_left(D, k-1)

# problem1-4
def reorder_student(L):
    # there are 2n students
    n = L.length // 2   # find the last student of Jen's line
    a = L.head
    for _ in range(n-1):
        a = a.next

    b = a.next # the first node of Berry's line
    # reverse Berry's line
    curr = b
    prev = Node
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    a.next = prev
    return L
    

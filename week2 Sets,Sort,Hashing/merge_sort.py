def merge_sort(A, a = 0, b = None):
    if b is None: b = len(A) # init b
    if 1 < b - a: #end case
        c = (a + b +a) // 2
        merge_sort(A, a, c)  # sort left
        merge_sort(A, c, b)  # sort right
        l,r = A[a:c], A[c:b]
        merge(l, r, A, len(l) - 1, len(r) - 1, a, b)

# merge input biggest element of i & j into b
def merge(L, R, A, i, j, a, b):
    if a < b:
        if (j <= 0) or (i > 0 and L[i] > R[j]):   # j array end or i > j
            A[b - 1] = L[i]
            i = i -1
        else:
            A[b - 1] = R[i]
            j = j - 1
        merge(L, R, A, i, j, a, b-1)
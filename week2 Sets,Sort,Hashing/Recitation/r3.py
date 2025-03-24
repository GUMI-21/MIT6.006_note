class selection_sort:
    def __init__(self):
        pass
    # 1 by iterate
    def selection_sort(self,A):
        for i in range(len(A) - 1, 0, -1):
            m = i                      # O(1) initial index of max
            for j in range(i):         # search max in A[:i]
                if A[m] < A[j]:
                    m = j
            A[m], A[i] = A[i], A[m]    # swap
    # 2 by recurese
    def prefix_max(self, A, i):
        if i > 0:
            j = self.prefix_max(A, i - 1) # find the biggest iten in 0 to i-1 is J
        if A[i] < A[j]:
            return j
        return i

    def selection_sort_recurse(self, A, i=None):
        if i is None: i = len(A) - 1
        if i > 0:
            j = self.prefix_max(A, i)
            A[i],A[j] = A[j],A[i]
            self.selection_sort_recurse(A, i - 1)
        return A

class insertion_sort:
    def __init__(self):
        pass
    def insertion_sort(self,A):
        for i in range(len(A)):   # loop O(n)
            j = i
            while j > 0 and A[j] < A[j-1]:
                A[j-1], A[j] = A[j], A[j-1]  #swap
                j = j -1

    def find_position(self,A,i):
        tmp = A[i]
        while i > 0 and tmp < A[i - 1]:
            i -= 1
        return i


    def insertion_sort_recurse(self, A, i=None):
        if i is None: i = 1
        if i <= len(A)-1:
            j = self.find_position(A,i)
            # shift the array
            key = A[i]
            k = i
            while k > j:
                A[k] = A[k-1]
                k -= 1
            A[j] = key
            self.insertion_sort_recurse(A, i + 1)
        return A

def merge_sort(A,a=0,b=None):
    if b is None:
        b=len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A,a,c)
        merge_sort(A,c,b)
        L, R = A[a:c], A[c:b]
        i, j = 0,0
        while a < b:
            if (j >= len(R)) or (i<len(L) and L[i] < R[j]):
                A[a] = L[i]
                i = i + 1
            else:
                A[a] = R[j]
                j = j + 1
            a = a + 1

if __name__ == '__main__':
    A = [1,4,2,5,7,8,2,3,5]
    a = insertion_sort()
    print(a.insertion_sort_recurse(A))
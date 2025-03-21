# p3-1 b
def find_nocollisions_hashing(A):
    i = 0
    while True:
        i = i + 1
        if i > 100:  # max number limit
            return 0
        b = []
        for j in range(len(A)):
            res = ((10*A[j] + 4) % i) % 7
            if res in b:
                break
            b.append(res)
            if j == len(A) - 1:
                return i

if __name__ == '__main__':
    A = [47, 61, 36, 52, 56, 33, 92]
    a = find_nocollisions_hashing(A)
    print(a)


# problem1-2 a
def reverse(D, i, k):
    if k < 2:
        return
    for j in range(k/2):
        x1 = D.delete_at(i-1+j)
        x2 = D.delete_at(i+k-1-j)
        D.insert_at(i-1+j,x2)
        D.insert_at(i+k-1-j,x1)
# answer: use recursive
def reverse(D, i, k):
    if k < 2:
        return # base case
    x2 = D.delete_at(i+k-1)
    x1 = D.delete_at(i)
    D.insert_at(i, x2)
    D.insert_at(i + k - 1, x1)
    reverse(D, i+1, k - 2)
# problem1-2 b
def move(D, i, k, j):
    if k < 1:   # base case
        return
    x1 = D.delete_at(i)
    D.insert_at(j-1,x1)
    move(D, i+1, k-1, j+1)
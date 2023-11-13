# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    maxsize = 1
    currentsize = 1
    currentpos = 0
    res = 0
    i, j = 0, 1
    while j < len(A):
        if A[i] < A[j]:
            currentsize += 1
            i += 1
            j += 1
        else:
            if currentsize > maxsize:
                maxsize = currentsize
                res = currentpos
            i = j
            j += 1
            currentpos = i
            currentsize = 1
    if currentsize > maxsize:
        maxsize = currentsize
        res = currentpos
    return res

A = [1,2,3]
#A = [2, 2, 2, 2, 1, 2, -1, 2, 1, 3]
print(solution(A))
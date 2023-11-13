# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    Nlen = 0
    i = 0
    while A[i] != -1:
        Nlen += 1
        i = A[i]
    Nlen += 1
    return Nlen

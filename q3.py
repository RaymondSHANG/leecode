# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
    # write your code in Python 3.6
    Nlen = len(T)
    i, j = 0, Nlen-1
    currentlen = 0
    maxleft = T[i]
    newmax = maxleft
    #minright = T[j]
    for i in range(1,Nlen):
        if T[i] > newmax:
            newmax = T[i]
        if T[i] <= maxleft:
            currentlen = i
            maxleft = newmax
    return currentlen+1
A= [-5,-3,-5,-2,-3,-4,-1,-1,0,-1,2,0,2]
print(A[solution(A)-1])
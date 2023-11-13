'''
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
'''
class Solution:
    def minSwaps(self, grid: list) -> int:
        lastOnes = []
        for onerow in grid:
            i = 0
            for j,k in enumerate(onerow):
                if k != 0:
                    i = j
            lastOnes.append(i)
        print(lastOnes)
        '''
        screen lastOnes from left, comparing to 0:len-1
        for each one, check
        '''
        n = 0
        i = 0
        k = 0
        while i < len(lastOnes):
            #print(f"the {i}th round: {lastOnes}")
            if lastOnes[i] == -1:
            	i += 1
            	continue
            while lastOnes[i] > k:
                #Need to swap until 
                mark_change = 0
                #print(lastOnes)
                for j in range(i+1,len(lastOnes)):
                    if lastOnes[j] == -1:
                        continue
                    n += 1
                    #print(lastOnes)
                    if lastOnes[j] <= k:
                        #Found One
                        mark_change = 1
                        lastOnes[j] = -1
                        k += 1
                        break
                if mark_change == 0:
                    return -1
            i += 1
            k += 1
        return n

'''
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
Input: [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], output:2
Input: [[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]]) == 4
#[0, 3, 3, 1, 2, 5] == 4
[[1,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,1,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[1,1,0,1,0,0,0,0]] == 3
'''
a = Solution()
#print(a.minSwaps(grid=[[0,0,1],[1,1,0],[1,0,0]]) == 3)
#print(a.minSwaps(grid=[[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]) == -1)
#print(a.minSwaps(grid=[[1,0,0],[1,1,0],[1,1,1]]) == 0)
#[[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
#[[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
#print(a.minSwaps(grid=[[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]) == 2)
#[[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]] == 4
#print(a.minSwaps(grid=[[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]) == 2)
#print(a.minSwaps(grid=[[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]]) == 4)
print(a.minSwaps(grid=[[1,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,1,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[1,1,0,1,0,0,0,0]]) == 3)



        
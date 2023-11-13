'''
You are given an array of network towers towers and an integer radius, where towers[i] = [xi, yi, qi] denotes the ith network tower with location (xi, yi) and quality factor qi. All the coordinates are integral coordinates on the X-Y plane, and the distance between two coordinates is the Euclidean distance.

The integer radius denotes the maximum distance in which the tower is reachable. The tower is reachable if the distance is less than or equal to radius. Outside that distance, the signal becomes garbled, and the tower is not reachable.

The signal quality of the ith tower at a coordinate (x, y) is calculated with the formula ⌊qi / (1 + d)⌋, where d is the distance between the tower and the coordinate. The network quality at a coordinate is the sum of the signal qualities from all the reachable towers.

Return the integral coordinate where the network quality is maximum. If there are multiple coordinates with the same network quality, return the lexicographically minimum coordinate.

1 <= towers.length <= 50
towers[i].length == 3
0 <= xi, yi, qi <= 50
1 <= radius <= 50
Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
Output: [1,2]
'''
import math
class Solution:
    def bestCoordinate(self, towers: list, radius: int) -> list:
        #Use list to store the coordinates
        '''
        because x,y <=50, the maximum coord should be within this scope
        use a 2-D array to store the data
        '''
        #sig_dict = [[0]*51]*51   Not correct 2-d array
        sig_dict = [[0]*51 for _ in range(50)]
        maxsig = 0
        result = [0,0]
        for a,b,q in towers:
            print(f"({a},{b},{q}):")
            xmin = a - radius
            xmax = a + radius
            ymin = b - radius
            ymax = b + radius
            for x in range(xmin,xmax+1):
                if x < 0 or x > 50:
                    continue
                for y in range(ymin,ymax+1):
                    if y < 0 or y > 50:
                        continue
                    dist = math.sqrt((x-a)**2 + (y-b)**2)
                    #print("distance",dist)
                    if  dist <= radius:
                        #update current signal
                        value = int(q//(1+dist))                       
                        if value > 0:
                            sig_dict[x][y] += value
                            #print(f"update\t({x},{y}):{sig_dict[x][y]}")
                            if sig_dict[x][y] > maxsig:
                                maxsig = sig_dict[x][y]
                                result = [x,y]
                                print(f"update maxiSig\t({x},{y}):{sig_dict[x][y]}")
                            elif sig_dict[x][y] == maxsig:
                                if x < result[0] or (x == result[0] and y < result[1]):
                                    result = [x,y]
                                    print(f"update maxiSig\t({x},{y}):{sig_dict[x][y]}")
        
        return result
#Test
a = Solution()
#[[0,1,2],[2,1,2],[1,0,2],[1,2,2]]
#1
print(a.bestCoordinate(towers = [[0,1,2],[2,1,2],[1,0,2],[1,2,2]], radius = 1))

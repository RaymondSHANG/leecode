from typing import List


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)
        r_pos = [i for i in range(N) if senate[i] == 'R']
        d_pos = [i for i in range(N) if senate[i] == 'D']
        while r_pos and d_pos:
            r_temp = r_pos.pop(0)
            d_temp = d_pos.pop(0)
            if r_temp < d_temp:
                r_pos.append(N+r_temp)
            else:
                d_pos.append(N+d_temp)
        return 'Radiant' if r_pos else 'Dire'

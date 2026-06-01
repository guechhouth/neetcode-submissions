"""
temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

- naive two loop scans --> O(n^2)


"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            if i == len(temperatures) -1:
                res.append(0)
                break
            for j in range(i+1, len(temperatures)):
                if (j == len(temperatures) -1) and temperatures[j] <= temperatures[i]:
                    res.append(0)
                elif temperatures[j] <= temperatures[i]:
                    count += 1
                elif temperatures[j] > temperatures[i]:
                    count += 1
                    res.append(count)
                    break
        return res
        
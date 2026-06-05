"""
Input: target = 10, position = [1,4], speed = [3,2]

Output: 1

when do they catch up?
car 1 start at 1 with speed 3
t = 0 at 1
t = 1 at 4
t = 2 at 7
t = 3 at 10
car 2 starts at 4 with speed 2
t = 0 at 4
t = 1 at 6
t = 2 at 8
t = 3 at 10

d = v*t

# if car at pos less but take less time to reach then it can be counted as fleet with another car
a car onl join fleet with a car ahead of it
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, s in pair:
            # time
            t = (target - pos)/s
            # only push for new fleet: car take longer
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)

        
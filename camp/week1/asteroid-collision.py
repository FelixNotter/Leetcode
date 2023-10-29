class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for r in range(len(asteroids)):
            skip = False
            while stack and (stack[-1] > 0 and asteroids[r] < 0):
                if abs(stack[-1]) == abs(asteroids[r]):
                    stack.pop()
                    skip = True
                    break
                if abs(stack[-1]) < abs(asteroids[r]):
                    stack.pop()
                else:
                    skip = True
                    break
            if skip:
                continue

            stack.append(asteroids[r])
        return stack


        
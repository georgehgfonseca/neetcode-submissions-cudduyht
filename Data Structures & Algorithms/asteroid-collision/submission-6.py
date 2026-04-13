class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # asteriods          = [2, 4, -4, -1]
        # i                  =         |
        # stack              = [2, 4]
        stack = []
        for i in range(len(asteroids)):
            if not stack or asteroids[i] > 0:
                stack.append(asteroids[i])
                continue
            sameDirection = (stack[-1] > 0 and asteroids[i] > 0) or (stack[-1] < 0 and asteroids[i] < 0)
            if sameDirection:
                stack.append(asteroids[i])
            elif asteroids[i] < 0:
                while -asteroids[i] > stack[-1] and stack[-1] > 0:
                    stack.pop()
                    if not stack:
                        break
                if not stack:
                    stack.append(asteroids[i])
                elif stack[-1] == -asteroids[i]:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
        return stack


        
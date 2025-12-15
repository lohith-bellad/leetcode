class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def stack_add(stack: List[int], cur: int):
            if len(stack) == 0:
                stack.append(cur)
                return

            last = stack[-1]
            if last * cur > 0:
                stack.append(cur)
            else:
                if last > 0:
                    if abs(last) < abs(cur):
                        stack.pop()
                        stack_add(stack, cur)
                    elif abs(last) == abs(cur):
                        stack.pop()
                else:
                    stack.append(cur)

        stack.append(asteroids[0])

        for i in range(1, len(asteroids)):
            stack_add(stack, asteroids[i])

        return stack

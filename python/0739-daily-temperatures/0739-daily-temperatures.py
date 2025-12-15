class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for i in range(len(temperatures))]

        stack.append((temperatures[-1], len(temperatures) - 1))
        ind = len(temperatures) - 2

        while ind >= 0:
            temp = temperatures[ind]

            while stack and temp >= stack[-1][0]:
                stack.pop()

            if len(stack) > 0:
                output[ind] = stack[-1][1] - ind
            stack.append((temp, ind))

            ind -= 1

        return output

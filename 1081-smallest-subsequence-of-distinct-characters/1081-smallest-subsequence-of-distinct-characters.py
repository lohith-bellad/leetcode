class Solution:
    def smallestSubsequence(self, s: str) -> str:
        table = {}
        present = set()
        stack = []

        for i in range(len(s)):
            table[s[i]] = i

        for i in range(len(s)):
            if s[i] in present:
                continue
            while stack and stack[-1] > s[i] and table[stack[-1]] > i:
                present.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            present.add(s[i])
        
        return "".join(stack)
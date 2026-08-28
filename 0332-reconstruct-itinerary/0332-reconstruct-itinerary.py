class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mapping = defaultdict(list)

        for src, dst in tickets:
            mapping[src].append(dst)
        
        for key in mapping.keys():
            mapping[key].sort(reverse=True)

        output = []
        stack = ["JFK"]

        while stack:
            while mapping[stack[-1]]:
                stack.append(mapping[stack[-1]].pop())
            output.append(stack.pop())

        return output[::-1]

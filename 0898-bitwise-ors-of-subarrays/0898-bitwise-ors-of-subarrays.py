class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        output = set()
        prev = set()

        for i in range(len(arr)):
            output.add(arr[i])
            cur = {arr[i]}
            for each in prev:
                val = arr[i] | each
                cur.add(val)
                output.add(val)
            prev = cur
        
        return len(output)
            
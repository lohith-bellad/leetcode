class Solution:
    def reorganizeString(self, s: str) -> str:
        hash_map = {}
        arr = []
        output = []
        total = 0

        for c in s:
            if c not in hash_map:
                hash_map[c] = 0
            hash_map[c] += 1

        for k,v in hash_map.items():
            arr.append((-v, k))
           
        heapq.heapify(arr)
        last_char = ""
        temp_q = []
        
        while len(arr) > 1:
            p, q = heapq.heappop(arr)
            if q == last_char:
                temp_q.append((p, q))
                p, q = heapq.heappop(arr)
            output += q
            p = -p
            if p > 1:
                heapq.heappush(arr, (-(p-1), q))
            while len(temp_q) > 0:
                heapq.heappush(arr, temp_q.pop())

            last_char = q
        
        p, q = heapq.heappop(arr)
        p = -p
        if p > 1:
            return ""
        else:
            output += q

        return "".join(output)


            
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        inorder = {n: 0 for n in nums}

        for seq in sequences:
            for i in range(len(seq) - 1):
                if seq[i] not in nums or seq[i + 1] not in nums:
                    return False
                mapping[seq[i]].append(seq[i + 1])
                inorder[seq[i + 1]] += 1
        
        queue = deque()

        for k, v in inorder.items():
            if v == 0:
                queue.append(k)
        path = []

        while queue:
            if len(queue) > 1:
                return False

            cur_num = queue.popleft()
            path.append(cur_num)
            for neighbor in mapping[cur_num]:
                inorder[neighbor] -= 1
                if inorder[neighbor] == 0:
                    queue.append(neighbor)
        
        return path == nums

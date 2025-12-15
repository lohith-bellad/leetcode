class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_hash = defaultdict(list)
        count = 0

        for i in range(len(nums)):
            if nums[i] not in index_hash:
                index_hash[nums[i]].append(i)
            else:
                indices = index_hash[nums[i]]
                for index in indices:
                    if (index * i) % k == 0:
                        count += 1
                index_hash[nums[i]].append(i)

        return count

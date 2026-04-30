class SparseVector:
    """
    def __init__(self, nums: []):
        self.vals = []

        for i, val in enumerate(nums):
            if val != 0:
                self.vals.append((i, val))

    def dotProduct(self, sv: 'SparseVector') -> int:
        res = 0

        p1 = 0
        p2 = 0

        while p1 < len(self.nums) and p2 < len(sv.nums):
            if self.nums[p1][0] == sv.nums[p2][0]:
                res += self.nums[p1][1] * sv.nums[p2][1]
                p1 += 1
                p2 += 1
            elif self.nums[p1][0] < sv.nums[p2][0]:
                p1 += 1
            else:
                p2 += 1

        return res

        def get_val(ind: int, v: []):
            start = 0
            end = len(v) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if v[mid][0] == ind:
                    return v[mid][1]
                if v[mid][0] < ind:
                    start = mid + 1
                else:
                    end = mid - 1

            return -1
        
        if len(self.vals) < len(sv.vals):
            prim = self.vals
            sec = sv.vals
        else:
            prim = sv.vals
            sec = self.vals
    
        output = 0
        for i in range(len(prim)):
            cur_ind, cur_val = prim[i]
            matching_val = get_val(cur_ind, sec)
            if matching_val >= 0:
                output += cur_val * matching_val
        
        return output
    """
    def __init__(self, nums: List[int]):
        self.ind_map = {}

        for ind, val in enumerate(nums):
            if val != 0:
                self.ind_map[ind] = val
        
        return

    def dotProduct(self, vec: "SparseVector") -> int:
        def find_ind(arr, val):
            start = 0
            end = len(arr) - 1

            while start <= end:
                mid = start + (end - start) // 2

                if arr[mid] == val:
                    return True
                
                if arr[mid] > val:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return False
        
        indices_1 = sorted(self.ind_map.keys()) #short
        indices_2 = sorted(vec.ind_map.keys()) #long

        if len(indices_1) > len(indices_2):
            indices_1, indices_2 = indices_2, indices_1
        
        result = 0
        for ind in indices_1:
            if find_ind(indices_2, ind):
                result += self.ind_map[ind] * vec.ind_map[ind]
        
        return result
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
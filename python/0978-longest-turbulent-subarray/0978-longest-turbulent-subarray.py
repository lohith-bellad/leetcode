class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        idx = 0
        count = 1
        exp_sign = None
        max_count = 1
        while idx < len(arr) - 1:
            if exp_sign == None:
                if arr[idx] > arr[idx + 1]:
                    exp_sign = "<"
                elif arr[idx] < arr[idx + 1]:
                    exp_sign = ">"
                else:
                    idx += 1
                    continue
                count += 1
                idx += 1
                max_count = max(max_count, count)
            else:
                if (exp_sign == ">" and arr[idx] <= arr[idx + 1]) or (
                    exp_sign == "<" and arr[idx] >= arr[idx + 1]
                ):
                    count = 1
                    exp_sign = None
                else:
                    if exp_sign == ">":
                        exp_sign = "<"
                    else:
                        exp_sign = ">"
                    count += 1
                    max_count = max(max_count, count)
                    idx += 1

        return max_count

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = []
        if num < 10:
            return num

        for c in str(num):
            num_list.append(int(c))

        idx = 0
        while idx < (len(num_list) - 1):
            digit = num_list[idx]
            if digit < max(num_list[idx + 1 :]):
                swap = max(num_list[idx + 1 :])
                for i in range(len(num_list) - 1, idx, -1):
                    if num_list[i] == swap:
                        num_list[idx], num_list[i] = num_list[i], num_list[idx]
                        break
                break
            else:
                idx += 1

        res = 0
        for num in num_list:
            res = (res * 10) + num

        return res

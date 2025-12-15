class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        num_list = []
        if num < 10:
            return num

        for c in str(num):
            num_list.append(int(c))

        idx = 0
        while idx < (len(num_list) - 1):
            digit = num_list[idx]
            swap = max(num_list[idx + 1:])
            if digit < swap:
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
        """
        if num == 0:
            return num

        num_list = list(str(num))
        num_list = [int(c) for c in num_list]
        pivot = 0

        while pivot < len(num_list) - 1 and num_list[pivot] >= max(
            num_list[pivot + 1 :]
        ):
            pivot += 1

        print(pivot)
        if pivot < len(num_list) - 1:
            max_num = max(num_list[pivot + 1 :])

            swap_ind = 0
            for i in range(len(num_list)):
                if num_list[i] == max_num:
                    swap_ind = i

            num_list[pivot], num_list[swap_ind] = num_list[swap_ind], num_list[pivot]

        output = 0
        for n in num_list:
            output = (output * 10) + n

        return output

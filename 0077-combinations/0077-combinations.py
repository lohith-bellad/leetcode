class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def traverse(n: int, ind: int, k: int, cur_combs: [], output: []):
            if len(cur_combs) == k:
                output.append(cur_combs.copy())
                return

            if ind > n:
                return
            
            cur_combs.append(ind)
            traverse(n, ind + 1, k, cur_combs, output)
            cur_combs.pop()

            traverse(n, ind + 1, k, cur_combs, output)
            return

        output = []

        traverse(n, 1, k, [], output)
        return output
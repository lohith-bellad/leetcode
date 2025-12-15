class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def traverse(
            candidates: List[int], target: int, ind: int, combs: [], output: []
        ):
            if sum(combs) == target:
                output.append(combs.copy())
                return

            if ind > len(candidates) - 1:
                return

            if sum(combs) > target:
                return

            combs.append(candidates[ind])
            traverse(candidates, target, ind + 1, combs, output)
            combs.pop()

            while ind + 1 < len(candidates) and candidates[ind] == candidates[ind + 1]:
                ind += 1
            traverse(candidates, target, ind + 1, combs, output)
            return

        output = []

        candidates.sort()
        traverse(candidates, target, 0, [], output)
        return output

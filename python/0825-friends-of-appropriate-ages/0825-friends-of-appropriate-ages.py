class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_cnt = [0 for i in range(121)]
        requests = 0

        for age in ages:
            age_cnt[age] += 1

        for i, g1_cnt in enumerate(age_cnt):
            for j, g2_cnt in enumerate(age_cnt):
                if (j <= (0.5 * i) + 7) or (j > i) or (j > 100 and i < 100):
                    continue
                if i == j:
                    requests -= g1_cnt

                requests += g1_cnt * g2_cnt

        return requests

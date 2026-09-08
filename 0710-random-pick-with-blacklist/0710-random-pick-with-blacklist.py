class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self. n = n
        self.mapping = {}
        blacklist = set(blacklist)
        self.b = len(blacklist)

        temp = []

        for b_num in blacklist:
            if b_num < n - self.b:
                temp.append(b_num)

        for i in range(n - self.b, n):
            if i not in blacklist:
                b_num = temp.pop()
                self.mapping[b_num] = i

    def pick(self) -> int:
        rand_pick = randrange(self.n - self.b)
        if rand_pick in self.mapping:
            return self.mapping[rand_pick]

        return rand_pick    


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
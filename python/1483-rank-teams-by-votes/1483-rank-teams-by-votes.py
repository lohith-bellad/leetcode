class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        hash_map = {}

        for vote in votes:
            for i, c in enumerate(vote):
                if c not in hash_map:
                    hash_map[c] = [0 for i in range(len(vote))]
                hash_map[c][i] += 1
        
        vote_alpha = sorted(hash_map.keys())
        winner = sorted(vote_alpha, key=lambda x: hash_map[x], reverse=True)
        
        return "".join(winner)
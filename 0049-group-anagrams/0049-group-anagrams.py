class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        output = []

        for word in strs:
            key = "".join(sorted(word))
            
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(word)
        
        for val in hash_map.values():
            output.append(val)

        return output
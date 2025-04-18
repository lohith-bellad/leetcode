class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        inp = sorted(strs, key = lambda x: len(x))

        output = inp[0]

        for i in range(1, len(inp)):
            ind = 0
            while ind < len(output) and inp[i][ind] == output[ind]:
                ind += 1
            output = output[:ind]
        
        return output
        """
        longest = strs[0]

        for i in range(1, len(strs)):
            cur_word = strs[i]
            max_ind = min(len(longest), len(cur_word))

            ind = 0
            while ind < max_ind and longest[ind] == cur_word[ind]:
                ind += 1
        
            longest = longest[:ind]
    
        return longest
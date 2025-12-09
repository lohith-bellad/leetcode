"""
187. Repeated DNA Sequences
Medium

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G',
and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long
sequences (substrings) that occur more than once in a DNA molecule. You may return
the answer in any order.


Example 1:
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]


Constraints:
    * 1 <= s.length <= 10^5
    * s[i] is either 'A', 'C', 'G', or 'T'.

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def seq_to_key(seq: str):
            mapping = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}
            output = 0
            mask = 18

            for s in seq:
                output = output | (mapping[s] << mask)
                mask -= 2

            return output

        def key_to_seq(key: int):
            rev_mapping = {0: "A", 1: "C", 2: "G", 3: "T"}
            res = ""

            while len(res) < 10:
                res += rev_mapping[key & 3]
                key = key >> 2

            return res[::-1]

        dna_table = {}
        if len(s) < 10:
            return []

        left = 0
        right = 9

        while right < len(s):
            seq = s[left : right + 1]
            key = seq_to_key(seq)
            dna_table[key] = dna_table.get(key, 0) + 1
            left += 1
            right += 1

        output = []

        for key, val in dna_table.items():
            if val > 1:
                output.append(key_to_seq(key))

        return output

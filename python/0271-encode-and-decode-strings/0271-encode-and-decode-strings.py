class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""
        for word in strs:
            count = len(word)
            l = str(count)
            if len(l) == 2:
                l = "0" + l
            elif len(l) == 1:
                l = "00" + l

            encoded += l + word

        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []

        idx = 0
        while idx < len(s):
            count = int(s[idx : idx + 3])
            decoded.append(s[idx + 3 : idx + count + 3])
            idx += count + 3

        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

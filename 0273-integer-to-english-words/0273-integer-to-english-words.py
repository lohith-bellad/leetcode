class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]

        def getChunkWords(num):
            res = []
            if num >= 100:
                res.append(ones[num // 100])
                res.append("Hundred")
                num = num % 100
            if num >= 20:
                res.append(tens[num // 10])
                num = num % 10
            if num > 0:
                res.append(ones[num])
            
            return " ".join(res)

        chunks = {0: "", 1: "Thousand", 2: "Million", 3: "Billion"}

        chunk_idx = 0
        output = []

        while num > 0:
            chunk = num % 1000

            if chunk > 0:
                word = getChunkWords(chunk)
                if chunk_idx > 0:
                    word += " " + chunks[chunk_idx]
                output.append(word)

            num = num // 1000
            chunk_idx += 1
        
        return " ".join(reversed(output))

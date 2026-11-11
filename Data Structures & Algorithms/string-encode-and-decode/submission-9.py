class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(chr(len(word)))
            parts.append(word)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            length = ord(s[i])
            start = i + 1
            end = start + length
            decoded.append(s[start:end])
            i = end

        return decoded
class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += (chr(len(s)) + s)
        return encode

    

    def decode(self, s: str) -> List[str]:
        
        decode,i = [], 0

        while i < len(s):
            length = ord(s[i])
            j = i+1
            decode.append(s[j:j+length])
            i += length + 1

        
        return decode


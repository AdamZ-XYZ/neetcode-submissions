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
            #print(length, s)
            decode.append(s[i+1:i+1+length])
            #print("decode: " + str(decode))
            i += length + 1

        
        return decode


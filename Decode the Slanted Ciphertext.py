class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        encoded_length = len(encodedText)
        cols = encoded_length//rows
        s = ''
        for i in range(cols):
            j = i
            while j<encoded_length:
                s+=encodedText[j]
                j += cols + 1
        return s.rstrip()
  

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(self.compare(word, s) for word in words)
    
    def compare(self, s1: str, s2: str) -> int:
        i, j = 0, 0
        
        while i < len(s1):
            if j >= len(s2) or s1[i] != s2[j]:
                return 0
            
            l1, l2 = 0, 0
            c = s1[i]

            while i < len(s1) and s1[i] == c:
                l1 += 1
                i += 1
            
            while j < len(s2) and s2[j] == c:
                l2 += 1
                j += 1
            
            if l1 > l2 or (l2 < 3 and l2 != l1):
                return 0
        
        if j != len(s2):
            return 0
        
        return 1 

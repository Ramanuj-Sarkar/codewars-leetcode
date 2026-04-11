class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
                # Step 1: Build one repeating sentence string with spaces
        s = " ".join(sentence) + " "
        
        # Length of the full repeated pattern
        n = len(s)
        
        # Step 2: pos = total number of characters placed on the screen
        pos = 0
        
        # Step 3: Process each row
        for _ in range(rows):
            # Try to place cols characters in this row
            pos += cols
            
            # Step 4: If we land on a space, move to the next character
            if s[pos % n] == " ":
                pos += 1
            else:
                # Step 5: If we are in the middle of a word,
                # move backward until we reach the start of that word
                while pos > 0 and s[(pos - 1) % n] != " ":
                    pos -= 1
        
        # Step 6: Number of full sentence fits
        return pos // n
        

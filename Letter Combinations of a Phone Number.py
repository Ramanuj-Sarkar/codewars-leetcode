# Find the possible combinations of letters
# corresponding to the digits of a phone number
# with a specific phone number setup where 2-9 have letters
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # strings that are too small / strings that are the correct length
        pre_answer, answer = [], []
        
        # letters which correspond to numbers
        correspondences = {'2': 'abc',
                          '3': 'def',
                          '4': 'ghi',
                          '5': 'jkl',
                          '6': 'mno',
                          '7': 'pqrs',
                          '8': 'tuv',
                          '9': 'wxyz'}
        
        # base case
        if len(digits) == 1:
            return [x for x in correspondences[digits]]
        
        # other cases
        for num, digit in enumerate(digits):
            # beginning
            if num == 0:
                pre_answer += [x for x in correspondences[digit]]
            else:
                for x in [x for x in pre_answer]:
                    for y in correspondences[digit]:
                        # only add if they're long enough
                        if len(x + y) == len(digits):
                            answer.append(x + y)
                        else:  # add to pre_answer if they're too short
                            pre_answer.append(x + y)
        
        return answer


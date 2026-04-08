# You get an integer in
# You get a Roman number out
class Solution:
    def intToRoman(self, num: int) -> str:
        # all base roman values
        values = {1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX', 
        5: 'V',
        4: 'IV',
        1: 'I'}

        answer = ''

        # this is guaranteed to be sorted
        # instead of stored in some possibly unsorted way
        sorted_values = sorted(values, key=lambda x: -x)

        for base_roman_value in sorted_values:
            if num >= base_roman_value:
                quotient = num // base_roman_value
                num -= base_roman_value * quotient
                answer += values[base_roman_value] * quotient
            
            # not necessary, but useful
            if num == 0:
                break

        return answer
        

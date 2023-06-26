class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)-1
        tmp = 0
        num = 0
        if digits[length] == 9:
            while(digits[length-num] == 9 and num<=length):
                digits[length-num] = 0
                num = num + 1
            if digits[0] == 0:
                digits[0] = 1
                digits.append(0)
            else:
                digits[length-num]=digits[length-num] + 1
        else:
            digits[length] = digits[length] + 1
        return digits

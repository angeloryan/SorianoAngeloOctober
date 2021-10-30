class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total = 0
        if num < 10:
            return num
        while num > 9:
            total = (num // 10) + (num % 10)
            num = total
        return total

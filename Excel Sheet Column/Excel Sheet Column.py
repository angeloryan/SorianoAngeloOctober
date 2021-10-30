class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        # Number = index of letter + 1 
        
        colNum = 0
        letPlace = 0
        
        for i in range(len(columnTitle), 0, -1):
            letterNum = letters.index(columnTitle[i-1:i]) + 1
            #print(letterNum)
            colNum +=  26**(letPlace) * letterNum
            
            letPlace += 1
            
        return colNum

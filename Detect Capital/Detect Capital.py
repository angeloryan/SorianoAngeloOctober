class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        wordQualifies = False 
        letterIter = 1
        
        expectLower = False
        expectUpper = False
        
        if len(word) == 1:
            print(len(word))
            return True
        
        
        if word[0].isupper():
            if word[1].islower():
                # first letter cap only        
                expectLower = True 
            elif word[1].isupper():
                # all caps 
                expectUpper = True 
        else:
            if word[1].islower():
                # all lower case 
                expectLower = True 
    
    
        while wordQualifies == False:
            print(letterIter)
            if expectLower == True and word[letterIter].isupper() == True: 
                expectLower = False
                #print("here1")
                return False
            elif expectUpper == True and word[letterIter].islower() == True: 
                #print("here2")
                expectUpper = False
                return False 
                            
            if letterIter >= len(word)-1:
                #print("here3")
                wordQualifies = True
                
            letterIter += 1     
                 
            
        if word[0].isupper() == True and expectLower == True: 
            return True 
        elif word[0].isupper() == True and expectUpper == True:
            return True
        elif word[0].islower() == True and expectLower == True:
            return True 
                
        return False 
                
                
                
                
            
          

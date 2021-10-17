class Solution(object):
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        finalList = []
        
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        
        rowList = [firstRow, secondRow, thirdRow]
        
        
        for i in range(len(words)):
            
            wordQualifies = True
            letterCount = 1
            currentRow = -1
            
            if firstRow.__contains__(words[i][0].lower()):
                currentRow = 0
            elif secondRow.__contains__(words[i][0].lower()):
                currentRow = 1
            elif thirdRow.__contains__(words[i][0].lower()):
                currentRow = 2
            #print(currentRow)
            
            while(wordQualifies == True and letterCount < len(words[i])):
                #print(letterCount)
                
                if rowList[currentRow].__contains__(words[i][letterCount].lower()) == False:
                    wordQualifies = False
                    #print("word does not qualify")
                else:
                    letterCount+=1
                    

            if wordQualifies == True:
                finalList.append(words[i])
                
        return finalList 

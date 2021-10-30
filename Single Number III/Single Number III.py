class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numIter = 0

        while len(nums) > 2:    
            freqCount = nums.count(nums[numIter])
            
            if freqCount > 1:
                removeVal = nums[numIter]
                while nums.__contains__(removeVal):
                    nums.remove(removeVal)
                    
            elif freqCount == 1:
                numIter +=1

        return nums 

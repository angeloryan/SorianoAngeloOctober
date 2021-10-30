class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if nums.__contains__(target): # contains 
            return nums.index(target)
        elif target > nums[len(nums)-1]: # back
            return len(nums)
        elif target < nums[0]: # front 
            return 0
        
        if not nums.__contains__(target):
            nums.append(target)
            nums.sort()
            return nums.index(target)
        
        return -1 

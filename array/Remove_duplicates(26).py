class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i=0
        while (i<(length-1)):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])       
                length=len(nums)
            else:
                i=i+1
        return length

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)-1
        res = 0
        i = 0
        while(res == 0):
            if nums[length]<target:
                res = length+1
                break
            elif nums[i] == target:
                res = i
                break
            elif nums[i]>target:
                res = i
                break    
            i = i + 1        
        return res

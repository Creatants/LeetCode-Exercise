#In a foolish way
import numpy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = 0
        tmp2 = 0
        arr=[]
        while tmp==0:
            length = len(nums)
            for i in range(0,length):
                i2 = target-nums[i]
                for j in  range(i+1,length):
                    if i2==nums[j]:
                        arr.append(i)
                        arr.append(j)
                        tmp=1
                        tmp2=1
                        break
                if tmp2 ==1:
                    break
        return arr

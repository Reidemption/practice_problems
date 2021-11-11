#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i= 0
        j=i+1
        while nums[i] + nums[j] != target:
            if j == (len(nums)-1):
                i += 1
                j = i
            j += 1
        return [i,j]
        
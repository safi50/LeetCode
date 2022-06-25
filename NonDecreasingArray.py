'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Example 3: 
Input: [3,4,2,3]
etc...
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3 or nums == sorted(nums): return True # if len of array is 0,1,2 -> it is always true
        nums2 = nums[:]  #make sure to use [:] when copying list, else nums2 = nums is a referenced list and change in one will change both.
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums2[i+1] = nums[i] #if nums[i] > nums[2] -> list can be made increasing if either nums[i] = nums[i+1] or nums[i+1] = nums[i]
                nums[i] = nums[i+1]
                return True if nums == sorted(nums) or nums2 == sorted(nums2) else False
    
        

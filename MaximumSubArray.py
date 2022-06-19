'''
QUESTION STATEMENT:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

#OPTIMUM APPROACH IS USING KADANE ALGORITHM
    def maxSubArray(self, nums: List[int]) -> int:

        localmax, globalmax = 0, nums[0]  
        for i in nums:         #iterate over array
             # Kadane Algorithm -> localmax = maximum of ( curr_index of array) and (previous localmax)
             # Localmax[i] = max(arr[i] , arr[i] + localmax[i-1])
            localmax = max(i , i + localmax) 
            if localmax > globalmax: # check to find the greatest sum of any subarray
                globalmax = localmax
        return globalmax            # return greatest sum of subarray

            
            

        

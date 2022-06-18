"""
QUESTION STATEMENT: 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
      						  # BRUTE FORCE SOLUTION  O(N^2)
        """
        for num1 in range(0 , (len(nums))-1):
            for num2 in range(1, len(nums)):
                    if num1 != num2 and nums[num1]+nums[num2] == target: 
                        list = [num1,num2]
		"""
						
    
      						  # OPTIMUM SOLUTION ( HASHMAP ) O(N)

        explored = {}		#empty dict 
        for key, value in enumerate(nums):			#traverses the list but enumerate also keeps track of index in key
			remaining = target - value				# find the difference between target and the value of current index
            if remaining in explored:				# compare the remaining value in explored dict 
                return [explored[remaining], key]	#return the values whose sum is target
            explored[value] = key					# IMPORTANT -> map (value -> key) , not (key -> value)
        

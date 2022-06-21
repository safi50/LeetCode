'''
Question: 
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

'''

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: # 2 list input parameters and 1 output list parameter
	nums3 = []
	for value in nums1: 
			if value in nums2:
				nums3.append(value)
				nums2.remove(value) #remove matched value , so that more than one values don't match to the same value. 
	return nums3

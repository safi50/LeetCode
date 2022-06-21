

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: # 2 list input parameters and 1 output list parameter
	nums3 = []
	for value in nums1: 
			if value in nums2:
				nums3.append(value)
				nums2.remove(value) #remove matched value , so that more than one values don't match to the same value. 
	return nums3



    def containsDuplicate(self, nums: List[int]) -> bool:
        
                #INTERMEDIATE SOLUTION
#         dict = {}
#         for key, value in enumerate(nums):
#             if value in dict.values():
#                 return True
#             dict[value] = key
#         return False
                
        
        # OPTIMUM SOLUTION 
		# set() functions creates a list of distinct numbers. Example: x = [1,2,3,1] --> set(x) = [1,2,3] --> excludes dublicates
        return len(nums) != len(set(nums)) #if len of original array and set of distinct elements is not equal, dublicate exists so return true else false
        

    

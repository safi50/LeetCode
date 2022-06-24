'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2
'''

#Fastest Solution --- HASHMAP 
def firstUniqChar(self, s: str) -> int:
	count = collections.Counter(s).  #builds a hashmap using the Counter function in collections library. e.g. {a: 4, b: 6 ...}
	
	for key, val in enumerate(s):	
		if count[val] == 1:		#checks the no. of occurances of current element in hashmap -> if one then its the first unique element, so return
			return key 
	return -1




#Medium Speed Solution: 
#         for i in s:
#             if i not in s[s.index(i)+1:]: #checks if the current element is present in rest of the list, if yes then returns index
#                 return s.index(i)
#         return -1


#Slowest Solution: 
#   def firstUniqChar(self, s: str) -> int:
#   	for char in s:
#   		indices = [i for i, x in enumerate(s) if x == char]
#     		if len(indices) == 1:
#         		return indices[0]
# 		return -1

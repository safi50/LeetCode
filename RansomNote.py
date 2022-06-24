'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
 #Solution 1: Best Speed
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	return all(ransomNote.count(x) <= magazine.count(x) for x in set(ransomNote)) #count occurances of chars in both str from unique chars of ransomNote



#Solution 2:  Good Speed
# def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	# return collections.Counter(ransomNote) & collections.Counter(magazine) == collections.Counter(ransomNote). #compare Hashmaps and bitwise operation



#solution 3: Medium Speed 
# def canConstruct(self, ransomNote: str, magazine: str) -> bool:
	# return True if collections.Counter(ransomNote) <= collections.Counter(magazine) else False #compare Hashmaps 


'''
QUESTION STATEMENT:
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1: 
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
'''
# For sorted arrays , Binary Search is the best algorithm and should be implemented. However, this solution is not that of binary search.

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        if row[-1] == target: # since array is sorted , we check if the last element of an individual array is greater than the target value, 
            return True       
        elif row[-1] > target: # if last element of row exists in target, then the target is probably in that row , so we ignore the rest of rows.
            if target in row: 
                return True
            return False

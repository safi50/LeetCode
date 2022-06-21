'''
Question: 
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix

Example:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
'''

'''
Approach: 
2D array is basically an array of arrays. So, we traverse the input array and fill individual inner rows first, and then append those rows 
to the resultant array. 
Res = [ [row1], [row2] , .... ] 
'''
# array = sum(array , []) --> converts a 2D array to a 1D array


def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:    
	row, res = [], []
	col = 0
	if len(mat)*len(mat[0]) != r*c:   		# rows * cols of both arrays should be equal to reshape it. this line check that
		return mat
	for i in mat: 							# traversing the 2D array 
		for j in i:
			row.append(j)
			col+= 1
			if col == c:					#if col = c , then go to next line and append the current row array in the res array. [ [row], [row] ... ]
				res.append(row)
				col = 0 
				row = []					# empty row array for the next iteration.
	return res


                


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


                

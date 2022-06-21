'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers:

Example:
NumRows = 6
							1
						1		1									1+1 = 2
					1		2		1								1+2 = 3 
				1	    	3       	3		1									1+3 = 4, 3+3 = 6 ....
			1		4		6		4		1
		1		5		10		10		5		1

'''


'''
Approach: 

 Any row can be constructed using the offset sum of the previous row. Example:
 1. from the current row , add zero to end of it and add zero to start of it. store these arrays in temp arrays.
 2. add the temp arrays's corresponding elements to get the next row of the pascal's triangle and so on... 
    1 3 3 1 0          1 4 6 4 1 0
 +  0 1 3 3 1		 + 0 1 4 6 4 1 
 =  1 4 6 4 1		 = 1 5 10 10 5 1
'''

	#Good and Easy Solution but takes more memory 
def generate(self, numRows: int) -> List[List[int]]:
	prev= [1]
	a = []
	b = []
	c = []
	res = [prev]
	for i in range(1, numRows):
		a = prev + [0]
		b = [0] + prev
		for j in range(len(a)):
			c.append(a[j] + b[j])
		prev = c 
		c = []
		res.append(prev)
	return res

        #SHORTER AND COMPLEX SOLUTION
def generate(self, numRows: int) -> List[List[int]]:
	res = [[1]]
	for i in range(1, numRows):
	# lambda is a function that takes arguments( can be as many as needed)  and 1 expression using those arguments.  --> lambda arguments : expression
	# map takes a function and iterables to perform that functions on. it maps the corresponding indexes of the iterables and performs the func on them
		#res += list(map(func , inp1 , inp2) --> breakdown of below line. -> we convert map to list in order to concatenate it to res, else error
		res += [list(map((lambda x, y: x+y), res[-1]+ [0], [0] + res[-1]))] #res[-1] grabs the last element of the res array
	return res

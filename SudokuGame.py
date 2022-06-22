'''
QUESTION STATEMENT:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''


''' SOLUTION APPROACH
Check for problems in Individual Rows, Columns, and Boxes.
If any row , column, or box contains a dublicate number then we return false , else true.

For Dublicates in Rows:
Iterate over each element of individual arrays (rows) in the board, and check for dublicates.

For Dublicates in Columns:
Iterate over corresponding elements of each individual array.
For Example:
Suppose board = [ array1, array2, .... array9]
so, array1[0] , array2[0] ...... array9[0] form the first column of the board.
Similarly, using a for loop for the number of elements in an array (row), we can extract individual columns
and check for dublicates using dictionaries as above.

For Dublicates in Boxes:

Checking for dublicates is a bit more complex than checking for rows and columns.
Since each box contains 3x3 elements and there are 9 boxes in a board. So an outer for loop runs 3 times to for each row of boxes
For Example:
A sudoku board can be updated as:
[ box1 , box2 , box3
box4 , box5 , box6
box7 , box8 , box9 ]

For individual boxes, first, traverse vertically in the board for 3 iterations to get a column for the individual box. This step is repeated 3 times to get a total for 9 elements (3x3) which are then compared for dublicates using a dictionary "box".
When the loop reaches the start of a new box i.e., column 0 , column 3, and column 6, the "box dictionary is reset to zero."
'''

def isValidSudoku(self, board: List[List[str]]) -> bool:
row = {}
col = {}
box = {}

    #Check for Row:
    for array in board:
        for key, val  in enumerate(array):
            if val in row:  #check if value already exists in the dictionary 
                return False
            if val != ".":
                row[val] = key   #add new value to dictionary
        row = {}

    # Check for column:
    for i in range(len(board)):  # iterate over corresponding elements of rows in the board.
        for array in board:
            if array[i] in col: #check if value already exists in the dictionary 
                return False 
            if array[i] != ".":
                col[array[i]] = i
        col = {}
        
    #check for box:
    for k in range(0,8,3):       #runs 3 times for 0,3,6 -> 0 for 1st row of boxes , 3 for 2nd row of boxes and ...
        for i in range(len(board)): # runs for length of row, after every 3rd iteration, box dict resets to zero
            if i % 3 == 0:             
                box = {}
            for j in range(3):            #this for loop is to iterate vertically for 3 iterations.  
                if board[j+k][i] in box:
                    return False
                if board[j+k][i] != ".":
                    box[board[j+k][i]] = i+j+k   
    return True

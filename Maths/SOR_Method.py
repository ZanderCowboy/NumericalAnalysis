#SOR Method

import math

# truncate - chops a number at the given number of decimal places.
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def printMatrix(a_matrix, n):
    for i in range(n):
        for j in range(n):
            print(f"Entry {i+1},{j+1}: {a_matrix[i][j]}")
        print()

# row_matrix - the row-i vector of the matrix 
def sigma(row_matrix, a_vector, bot, top):
    value = 0
    if bot > top:
        return 0
    else:
        for i in range(bot, top+1):
            value += (row_matrix[i-1])*(a_vector[i-1])
        return value
        

# INPUT
# n = matrix size
# w = omega
n = 4
matrix = [[1.19, 2.11, -100, 1],
          [14.2, -0.122, 12.2, -1],
          [0, 100, -99.9, 1],
          [15.3, 0.110, -13.1, -1]]
vector = [1.12, 3.44, 2.15, 4.16]
w = 0.5
x_answer = [1, 3, 2, 4]

tol = 10 ** -5
iteration = 3

k = 1
while k <= iteration:
    for i in range(1,n+1):
        one = (1 - w) * x_answer[i-1]
        two = w / matrix[i-1][i-1]
        three = sigma(matrix[i-1],x_answer, 1, i-1)
        four = sigma(matrix[i-1],x_answer, i+1, n)
        x_answer[i-1] = one + two*(vector[i-1] - three - four)
        x_answer[i-1] = float(truncate(x_answer[i-1], 4))
        print(f"****Ans x{i}: {x_answer[i-1]}****")
    print()

    k += 1


#Output matrix*****************************
#printMatrix(matrix, n)
#for i in range(n):
    #print(vector[i])






'''
#input from user
x = int(input("Enter the size of the matrix: "))
x_matrix = [[0] * x] * x
row = [0] * x
b_vector = [0] * x

print(x_matrix)

for i in range(x):
    for j in range(x):
        row[j] = input(f"Entry a{i+1}: ")
    x_matrix[i] = row

#x_matrix[0] = [1, 2]
#x_matrix[1] = [3, 4]

        
for i in range(x):
    b_vector[i] = input(f"Entry b{i+1}: ")


#print matrix of user
for i in range(x):
    print(x_matrix[i])

for i in range(x):
    print(b_vector[i])


print(x_matrix)
#print(a_matrix)
#print(matrix[1][1])
'''



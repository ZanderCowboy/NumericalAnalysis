# Gauss-Seidel Iterative Method

# truncate - chops a number at the given number of decimal places.
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

# row_matrix - the row-i vector of the matrix 
def sigma(row_matrix, a_vector, bot, top):
    value = 0
    if bot > top:
        return 0
    else:
        for i in range(bot, top+1):
            value += (row_matrix[i-1])*(a_vector[i-1])
        return value

# input
n = 4
matrix = [[1.19, 2.11, -100, 1],
          [14.2, -0.122, 12.2, -1],
          [0, 100, -99.9, 1],
          [15.3, 0.110, -13.1, -1]]
vector = [1.12, 3.44, 2.15, 4.16]
x_answer = [1, 3, 2, 4]
tol = 10 ** -5
iteration = 3

k = 1
while k <= iteration:
    for i in range(1,n+1):
        one = 1 / matrix[i-1][i-1]
        two = sigma(matrix[i-1],x_answer, 1, i-1)
        three = sigma(matrix[i-1],x_answer, i+1, n)
        x_answer[i-1] = one *(- two - three + vector[i-1])
        x_answer[i-1] = float(truncate(x_answer[i-1],1))
        print(f"****Ans x{i}: {x_answer[i-1]}****")
    print()

    k += 1

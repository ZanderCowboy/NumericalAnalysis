# Jacobi Iterative Technique

# truncate - chops a number at the given number of decimal places.
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


# row_matrix - the row-i vector of the matrix
# a_vector = x vector
# bot = bottom start value of sigma
# top = top end value of sigma
# row = current row
def sigma(row_matrix, a_vector, bot, top, row):
    value = 0
    ans = 0
    if bot > top:
        return 0
    else:
        for i in range(bot, top+1):
            ans = (row_matrix[i-1])*(a_vector[i-1])
            if row != i:
                value += ans
        return value

# INPUT
n = 4
matrix = [[1.19, 2.11, -100, 1],
          [14.2, -0.122, 12.2, -1],
          [0, 100, -99.9, 1],
          [15.3, 0.110, -13.1, -1]]
vector = [1.12, 3.44, 2.15, 4.16]
x_answer = [1, 3, 2, 4]
new_vec = [0] * n
tol = 10 ** -5
iteration = 3

k = 1
while k <= iteration:
    for i in range(1,n+1):
        one = 1 / matrix[i-1][i-1]
        two = sigma(matrix[i-1],x_answer, 1, n, i)
        new_vec[i-1] = one *(- two + vector[i-1])
        new_vec[i-1] = float(truncate(new_vec[i-1], 4))
        print(f"****Ans x{i}: {new_vec[i-1]}****")
    x_answer = new_vec
    print()

    k += 1

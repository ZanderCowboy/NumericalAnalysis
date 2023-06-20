from math import factorial

def func_derivative(i_f, x_f):
    # i_f is the ith derivative of the function f
    x = i_f + x_f

    return x


# INPUT
m = int(input("Enter non-negative m: "))
n = int(input("Enter non-negative n: "))

# STEP 1
N = m + n
a_list = [] * N
q_list = [] * N
p_list = [] * N
b_list = [[] * N] * N

# STEP 2
for i in range(0, N):
    # TODO
    a_list[i] = func_derivative(i, 0) / factorial(i)
    # a_i = (f^i(0)) / (i!)  # f is a function

# STEP 3
q_list[0] = 1
p_list[0] = a_list[0]

# STEP 4
for i in range(1, N):  # do STEPS 5-10
    # STEP 5
    for j in range(1, i-1):
        if j <= n:
            b_list[i][j] = 0

    # STEP 6
    if i <= n:
        b_list[i][i] = 1

    # STEP 7
    for j in range(i+1, N):
        b_list[i][j] = 0

    # STEP 8
    for j in range(1, i):
        if j <= m:
            b_list[i][n+j] = -(a_list[i-j])

    # STEP 9
    for j in range(n+i+1, N):
        b_list[i][j] = 0

    # STEP 10
    b_list[i][N+1] = a_list[i]

# STEP 11
for i in range(n+1, N-1):  # do STEPS 12-18
    # STEP 12
    k = 1
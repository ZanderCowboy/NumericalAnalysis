# def input_matrix_a(n_this):
# 	print("Enter the values of A")
# 	matrix_a = [0] * n_this
# 	for i in range(n_this):
# 		a[i] = [0] * (n_this+1)
# 		print("Row {}".format(i+1))
# 		for j in range(n_this+1):
# 			a[i][j] = float(input("Enter a{}{}: ".format(i+1, j+1)))
#
# 	return matrix_a

# A MATRIX
# a = [[2, -1, 0, 0, 1],
# 		  [-1, 2, -1, 0, 0],
# 		  [0, -1, 2, -1, 0],
# 		  [0, 0, -1, 2, 1]]

# Input
# n = int(input("Enter dimension n: "))
n = 12

# initialization
# rows
a = [0] * n
l = [0] * n
u = [0] * n
z = [0] * n
x = [0] * n

# columns
for i in range(n):
	a[i] = [0] * (n + 1)
	l[i] = [0] * n
	u[i] = [0] * n


for i in range(n):
	for j in range(n):
		if i == j:
			u[i][i] = 1

# adding A values
# print("Enter values of A: to be added")
# for i in range(n):
# 	print("Row {}".format(i + 1))
# 	for j in range(n + 1):
# 		if j != n:
# 			a[i][j] = float(input("Enter a{}{}: ".format(i + 1, j + 1)))
# 		else:
# 			a[i][j] = float(input("Enter b{}: ".format(i + 1)))

a = [[3, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	 [-1, 3, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
	 [0, -1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
	 [0, 0, 0, 3, -1, 0, 0, 0, 0, 0, 0, 0, 4],
	 [0, 0, 0, -1, 3, -1, 0, 0, 0, 0, 0, 0, 5],
	 [0, 0, 0, 0, -1, 3, 0, 0, 0, 0, 0, 0, 6],
	 [0, 0, 0, 0, 0, 0, 3, -1, 0, 0, 0, 0, 7],
	 [0, 0, 0, 0, 0, 0, -1, 3, -1, 0, 0, 0, 8],
	 [0, 0, 0, 0, 0, 0, 0, -1, 3, 0, 0, 0, 9],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, -1, 0, 10],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 3, -1, 11],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 3, 12]]

# Step 1
l[0][0] = a[0][0]
u[0][1] = a[0][1] / l[0][0]
z[0] = a[0][n] / l[0][0]

# Step 2
for i in range(1, n-1):
	l[i][i - 1] = a[i][i - 1]  # ith row of L
	l[i][i] = a[i][i] - (l[i][i - 1] * u[i - 1][i])
	u[i][i + 1] = a[i][i + 1] / l[i][i]  # (i+1)th column of U
	z[i] = (a[i][n] - l[i][i - 1] * z[i - 1]) / l[i][i]

# Step 3
l[n - 1][n - 2] = a[n - 1][n - 2]  # nth row of L
l[n - 1][n - 1] = a[n - 1][n - 1] - l[n - 1][n - 2] * u[n - 2][n - 1]
z[n - 1] = (a[n - 1][n] - l[n - 1][n - 2] * z[n - 2]) / l[n - 1][n - 1]

# Steps 4 and 5 solve Ux = z
# Step 4
x[n - 1] = z[n - 1]

# Step 5
for i in range(n - 2, -1, -1):
	x[i] = z[i] - u[i][i + 1] * x[i + 1]

# Step 6
string = ""
for i in range(n):
	print("x{}: {:.8f}".format(i + 1, x[i]))


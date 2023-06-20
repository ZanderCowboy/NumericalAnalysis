from math import exp
from math import fabs as abs

# example
a, b, c, d = 0, 2, 0, 1
m, n = 5, 6
TOL = -10
N = 100


def f_func(x_val, y_val):
	# some_val = x_val + y_val
	some_val = x_val * exp(y_val)

	return some_val


def g_func(x_val, y_val):
	# some_val = x_val + y_val
	if x_val == 0:
		some_val = 0
	elif x_val == 2:
		some_val = 2 * exp(y_val)
	elif y_val == 0:
		some_val = x_val
	elif y_val == 1:
		some_val = exp(y_val) * x_val
	else:
		some_val = 0

	return some_val


# input
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))
# d = float(input("Enter d: "))
# m = int(input("Enter m (>=3): "))
# n = int(input("Enter n (>=3): "))
# TOL = int(input("Enter tol: 10^...: "))
# N = int(input("Max # of iterations: "))


# initialization
# n = n+1
# m = m+1
TOL = 10 ** TOL
x = [1] * (n + 1)
y = [1] * (m + 1)
# w = [[1] * m] * n
w = [[1] * (n + 1)] * (m + 1)

# Step 1
h = (b - a) / n
k = (d - c) / m
# print("{}\t{}".format(h, k))

# Step 2
for i in range(1, n):
	x[i] = a + i * h
# for i in range(1, n):
# 	print(x[i], end=" ")
# print("\n")

# Step 3
for j in range(1, m):
	y[j] = c + j * k
# for j in range(1, m):
# 	print(y[j], end=" ")
# print("\n")


# Step 4
for i in range(1, n):
	for j in range(1, m + 1):
		w[i][j] = 0
	# w[j][i] = 0

# print(w[0][0])
# print(w[1][0])
# w[2][4] = 5
# print(w[3][2])

for i in range(m + 1):
	for j in range(n + 1):
		print(w[i][j], end=" ")
		if i == 2:
			if j == 4:
				w[i][j] = 5
	# print("{}/{}".format(i, j), end=" ")
	print("\n")

# Step 5
lamda = (h ** 2) / (k ** 2)
micro = 2 * (1 + lamda)
l = 1

# Step 6
while (l <= N):  # do Steps 7-20
	# Step 7
	z = (-(h ** 2) * f_func(x[1], y[m - 1]) + g_func(a, y[m - 1]) + lamda * g_func(x[1], d)
		 + lamda * (w[1][m - 2]) + w[2][m - 1]) / micro
	NORM = abs(z - w[1][m - 1])
	w[1][m - 1] = z

	# Step 8
	for i in range(2, n - 2 + 1):
		z = (-(h ** 2) * f_func(x[i], y[m - 1]) + lamda * g_func(x[i], d) + w[i - 1][m - 1]
			 + w[i + 1][m - 1] + lamda * (w[i][m - 2])) / micro
		if abs(w[i][m - 1] - z) > NORM:
			NORM = abs(w[i][m - 1] - z)
		w[i][m - 1] = z

	# Step 9
	z = (-(h ** 2) * f_func(x[n - 1], y[m - 1]) + g_func(b, y[m - 1]) + lamda * g_func(x[n - 1], d)
		 + w[n - 2][m - 1] + lamda * (w[n - 1][m - 2])) / micro
	if abs(w[n - 1][m - 1] - z) > NORM:
		NORM = abs(w[n - 1][m - 1] - z)
	w[n - 1][m - 1] = z

	# Step 10
	for j in range(m - 2, 2 - 1, -1):
		# Step 11
		z = (-(h ** 2) * f_func(x[1], y[j]) + g_func(a, y[j]) + lamda * w[1][j + 1]
			 + lamda * w[1][j - 1] + w[2][j]) / micro
		if abs(w[1][j] - z) > NORM:
			NORM = abs(w[1][j] - z)
		w[1][j] = z

		# Step 12
		for i in range(2, n - 2 + 1):
			z = (-(h ** 2) * f_func(x[i], y[j]) + w[i - 1][j] + lamda * (w[i][j + 1])
				 + w[i + 1][j] + lamda * (w[i][j - 1])) / micro
			if abs(w[i][j] - z) > NORM:
				NORM = abs(w[i][j] - z)
			w[i][j] = z

		# Step 13
		z = (-(h ** 2) * f_func(x[n - 1], y[j]) + g_func(b, y[j]) + w[n - 2][j]
			 + lamda * (w[n - 1][j + 1]) + lamda * (w[n - 1][j - 1])) / micro
		if abs(w[n - 1][j] - z) > NORM:
			NORM = abs(w[n - 1][j] - z)
		w[n - 1][j] = z

	# Step 14
	z = (-(h ** 2) * f_func(x[1], y[1]) + g_func(a, y[1]) + lamda * g_func(x[1], c)
		 + lamda * w[1][2] + w[2][1]) / micro
	if abs(w[1][1] - z) > NORM:
		NORM = abs(w[1][1] - z)
	w[1][1] = z

	# Step 15
	for i in range(2, n - 2 + 1):
		z = (-(h ** 2) * f_func(x[n - 1], y[m - 1]) + lamda * g_func(x[i], c) + w[i - 1][1]
			 + lamda * (w[i][2]) + w[i + 1][1]) / micro
		if abs(w[i][1] - z) > NORM:
			NORM = abs(w[i][1] - z)
		w[i][1] = z

	# Step 16
	z = (-(h ** 2) * f_func(x[n - 1], y[1]) + g_func(b, y[1]) + lamda * g_func(x[n - 1], c)
		 + w[n - 2][1] + lamda * (w[n - 1][2])) / micro
	if abs(w[n - 1][1] - z) > NORM:
		NORM = abs(w[n - 1][1] - z)
	w[n - 1][1] = z

	# Step 17
	if NORM <= TOL:
		# Step 18
		for i in range(1, n - 1 + 1):
			for j in range(1, m - 1 + 1):
				print("{}, {}, {}".format(x[i], y[j], w[i][j]))

		# Step 19
		break

	# Step 20
	l = l + 1

# Step 21
print("Maximum number of iterations exceeded.")

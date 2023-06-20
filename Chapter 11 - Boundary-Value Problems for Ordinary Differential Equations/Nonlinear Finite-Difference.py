from math import sqrt


def f_func(x_this, y_this, yp_this):
	ans = (1 / 8) * (32 + 2 * pow(x_this, 3) - y_this * yp_this)
	return ans


def fy_func(x_this, y_this, yp_this):
	blank = (x_this + y_this) * 0
	ans = -(1 / 8) * yp_this
	return ans + blank


def fyp_func(x_this, y_this, yp_this):
	blank = (x_this + y_this) * 0
	ans = -(1 / 8) * pow(yp_this, 2)
	return ans + blank


# Input
# a_val = float(input("Enter a: "))
# b_val = float(input("Enter b: "))
# alpha = float(input("Enter alpha: "))
# beta = float(input("Enter beta: "))
# N = int(input("Enter N (N>=2): "))
# TOL = int(input("Enter TOL: 10^ -... "))
# TOL = pow(10, -TOL)
# M = int(input("Enter M: "))
a_val = 1
b_val = 3
alpha = 17
beta = 43 / 3
N = 20
TOL = pow(10, -5)
M = 15

# Initialization
w = [0] * (N + 2)
a = [0] * N
b = [0] * N
c = [0] * N
d = [0] * N

l = [0] * N
u = [0] * N
z = [0] * N

v = [0] * N

# Step 1
h = (b_val - a_val) / (N + 1)
w[0] = alpha
w[N + 1] = beta

# Step 2
for i in range(1, N + 1):
	w[i] = alpha + i * (beta - alpha / b_val - a_val) * h

# Step 3
k = 1

# Step 4
while k <= M:  # Do steps 5 - 16
	# Step 5
	x = a_val + h
	t = (w[2] - alpha) / 2 * h
	a[0] = 2 + pow(h, 2) * fy_func(x, w[1], t)
	b[0] = -1 + (h / 2) * fyp_func(x, w[1], t)
	d[0] = -(2 * w[1] - w[2] - alpha + pow(h, 2) * f_func(x, w[1], t))

	# Step 6
	for i in range(1, N):
		x = a_val + (i * h)
		t = (w[i + 1] - w[i - 1]) / 2 * h
		a[i] = 2 + pow(h, 2) * fy_func(x, w[i], t)
		b[i] = -1 + (h / 2) * fyp_func(x, w[i], t)
		c[i] = -1 - (h / 2) * fyp_func(x, w[i], t)
		d[i] = -(2 * w[i] - w[i + 1] - w[i - 1] + pow(h, 2) * f_func(x, w[i], t))

	# Step 7
	x = b_val - h
	t = (beta - w[N - 1]) / 2 * h
	a[N - 1] = 2 + pow(h, 2) * fy_func(x, w[i], t)
	c[N - 1] = -1 - (h / 2) * fyp_func(x, w[N], t)
	d[N - 1] = -(2 * w[N] - w[i + 1] - beta + pow(h, 2) * f_func(x, w[N], t))

	# Step 8
	l[0] = a[0]
	u[0] = b[0] / a[0]
	z[0] = d[0] / l[0]

	# Step 9
	for i in range(1, N):
		l[i] = a[i] - c[i] * u[i - 1]
		u[i] = b[i] / l[i]
		z[i] = (d[i] - c[i] * z[i - 1]) / l[i]

	# Step 10
	l[N - 1] = a[N - 1] - c[N - 1] * u[N - 2]
	z[N - 1] = (d[N - 1] - c[N - 1] * z[N - 2]) / l[N - 1]

	# Step 11
	v[N - 1] = z[N - 1]
	w[N - 1] = w[N - 1] + v[N - 1]

	# Step 12
	for i in range(N - 2, -1, -1):
		v[i] = z[i] - u[i] * v[i + 1]
		w[i] = w[i] + v[i]
	# print(v[i])
	# print(w[i])

	# Calculate ||v||
	val = 0
	for i in range(0, N):
		# print(v[i])
		temp = pow(v[i], 2)
		# print(temp)
		val += temp

	norm_v = sqrt(val)

	# Step 13
	print(norm_v)
	if norm_v <= TOL:
		# Step 14
		for i in range(0, N + 1):
			x = a_val + i * h
			print("{:.2f}\t{:.8f}".format(x, w[i]))

		# Step 15 - stop
		break

	# Step 16
	k = k + 1

# Step 17
print("The procedure was not successful")

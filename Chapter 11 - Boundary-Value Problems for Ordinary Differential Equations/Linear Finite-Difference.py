from math import sin
from numpy import log as ln


def p_func(x_this):
	ans = -2 / x_this
	return ans


def q_func(x_this):
	ans = 2 / pow(x_this, 2)
	return ans


def r_func(x_this):
	ans = sin(ln(x_this)) / pow(x_this, 2)
	return ans


# Input
# a_val = float(input("Enter a: "))
# b_val = float(input("Enter b: "))
# alpha = float(input("Enter alpha: "))
# beta = float(input("Enter beta: "))
# N = int(input("Enter N (N>=2): "))
a_val = 1
b_val = 2
alpha = 1
beta = 2
N = 9-1

# Initialization
# Step 1
newn = N + 1
a = [0] * newn
b = [0] * newn
c = [0] * newn
d = [0] * newn
l = [0] * newn
u = [0] * newn
z = [0] * newn
w = [0] * (N + 2)

h = (b_val - a_val) / (N + 1)
x = a_val + h
# print(x)

a[1] = 2 + pow(h, 2) * q_func(x)
b[1] = -1 + (h / 2) * p_func(x)
d[1] = -pow(h, 2) * r_func(x) + (1 + (h / 2) * p_func(x) * alpha)
# print(av)
# print(bv)
# print(cv)
# print(dv)
# print("\n")

# Step 2
for i in range(2, N-1):
	# print(i)
	x = a_val + (i * h)
	# print(x)
	c[i] = -1 - (h / 2) * p_func(x)
	a[i] = 2 + pow(h, 2) * q_func(x)
	b[i] = -1 + (h / 2) * p_func(x)
	d[i] = -pow(h, 2) * r_func(x)
# print(av)
# print(bv)
# print(cv)
# print(dv)
print("\n")

# Step 3
x = b_val - h
print(x)
a[N] = 2 + pow(h, 2) * q_func(x)
c[N] = -1 - (h / 2) * p_func(x)
d[N] = -pow(h, 2) * r_func(x) + (1 - (h / 2) * p_func(x) * beta)
print(a)
print(b)
print(c)
print(d)

# Step 4
# l[0] = a[0]
# u[0] = b[0] / a[0]
# z[0] = d[0] / l[0]
l[1] = a[1]
u[1] = b[1] / a[1]
z[1] = d[1] / l[1]

# Step 5
for i in range(2, N - 1):
	# print(i)
	l[i] = a[i] - c[i] * u[i - 1]
	u[i] = b[i] / l[i]
	z[i] = (d[i] - c[i] * z[i - 1]) / l[i]

# Step 6
# l[N - 1] = a[N - 1] - c[N - 1] * u[N - 2]
# z[N - 1] = (d[N - 1] - c[N - 1] * z[N - 2]) / l[N - 1]
l[N] = a[N] - c[N] * u[N - 1]
z[N] = (d[N] - c[N] * z[N - 1]) / l[N]

# Step 7
w[0] = alpha
w[N + 1] = beta
w[N] = z[N]
print(w)

# Step 8
for i in range(1, N-1):
	# print(i)
	j = N - i
	w[j] = z[j] - u[j] * w[j + 1]

# Step 9
for i in range(0, N+1):
	x = a_val + (i * h)
	print("{:.2f}\t\t{:.8f}".format(x, w[i]))

# Step 10 - STOP

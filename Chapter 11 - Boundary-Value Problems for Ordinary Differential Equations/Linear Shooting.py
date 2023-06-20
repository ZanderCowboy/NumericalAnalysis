# import math
from math import pow


# Define FUNCTIONS
def insert_values():
	a_val = 1
	b_val = 2
	alpha_val = 1
	beta_val = 2
	n_val = 10
	return a_val, b_val, alpha_val, beta_val, n_val


def p_func(x_this):
	# ans = -2 / x_this
	ans = pow(x_this, 2)
	return ans


def q_func(x_this):
	ans = 2 / pow(x_this, 2)
	return ans


def r_func(x_this):
	# ans = (sn(log(x_this))) / pow(x_this, 2)
	ans = 0
	return ans


# Input
a, b, alpha, beta, N = insert_values()
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# alpha = float(input("Enter alpha: "))
# beta = float(input("Enter beta: "))
# N = int(input("Enter N: "))

# Initialize u and v and w
newN = N + 1
u1 = [0] * newN
u2 = [0] * newN
v1 = [0] * newN
v2 = [0] * newN
w1 = [0] * newN
w2 = [0] * newN

# Step 1
h = (b - a) / N
u1[0] = alpha
u2[0] = 0
v1[0] = 0
v2[0] = 1

# Step 2
for i in range(0, N - 1 + 1):  # Do steps 3 and 4
	# The Runge-Kutta method for systems is used in Steps 3 and 4
	# Step 3
	x = a + i * h

	# Step 4
	k11 = h * u2[i]
	k12 = h * (p_func(x) * u2[i] + q_func(x) * u1[i] + r_func(x))
	k21 = h * (u2[i] + (1 / 2) * k12)
	k22 = h * (p_func(x + h / 2) * (u2[i] + (1 / 2) * k12) +
			   q_func(x + h / 2) * (u1[i] + (1 / 2) * k11) +
			   r_func(x + h / 2))
	k31 = h * (u2[i] + (1 / 2) * k22)
	k32 = h * (p_func(x + h / 2) * (u2[i] + (1 / 2) * k22) +
			   q_func(x + h / 2) * (u1[i] + 0.5 * k21) +
			   r_func(x + h / 2))
	k41 = h * (u2[i] + k32)
	k42 = h * (p_func(x + h) * (u2[i] + k32) +
			   q_func(x + h) * (u1[i] + k31) +
			   r_func(x + h))

	u1[i + 1] = u1[i] + (1 / 6) * (k11 + 2 * k21 + 2 * k31 + k41)
	u2[i + 1] = u2[i] + (1 / 6) * (k12 + 2 * k22 + 2 * k32 + k42)

	kp11 = h * (v2[i])
	kp12 = h * (p_func(x) * v2[i] + q_func(x) * v1[i])
	kp21 = h * (v2[i] + 0.5 * kp12)
	kp22 = h * (p_func(x + h / 2) * (v2[i] + 0.5 * kp12) +
				q_func(x + h / 2) * (v1[i] + 0.5 * kp11))
	kp31 = h * (v2[i] + 0.5 * kp22)
	kp32 = h * (p_func(x + h / 2) * (v2[i] + 0.5 * kp22) +
				q_func(x + h / 2) * (v1[i] + 0.5 * kp21))
	kp41 = h * (v2[i] + kp32)
	kp42 = h * (p_func(x + h) * (v2[i] + kp32) +
				q_func(x + h) * (v1[i] + kp31))

	v1[i + 1] = v1[i] + (1 / 6) * (kp11 + 2 * kp21 + 2 * kp31 + kp41)
	v2[i + 1] = v2[i] + (1 / 6) * (kp12 + 2 * kp22 + 2 * kp32 + kp42)

# Step 5
w1[0] = alpha
w2[0] = (beta - u1[N]) / v1[N]
print("xi\t\t\t u1_i\t\t\t v1_i\t\t wi=y(xi)\t\t\t w2_i")
print("{:.1f}\t\t {:.8f}\t\t {:.8f}\t\t {:.8f}\t\t {:.8f}".format(a, u1[0], v1[0], w1[0], w2[0]))

# Step 6
for i in range(1, N + 1):
	W1 = u1[i] + w2[0] * v1[i]
	W2 = u2[i] + w2[0] * v2[i]
	x = a + i * h
	print("{:.1f}\t\t {:.8f}\t\t {:.8f}\t\t {:.8f}\t\t {:.8f}".format(x, u1[i], v1[i], W1, W2))

# Step 7 - STOP

import math
from math import pow


# Define FUNCTIONS
def insert_values():
	a_val = 1
	b_val = 3
	alpha_val = 17
	beta_val = 43 / 3
	N_val = 20
	TOL_val = pow(10, -5)
	M_val = 10
	return a_val, b_val, alpha_val, beta_val, N_val, TOL_val, M_val


def f_func(x_this, y_this, yp_this):
	ans = 0.125*(32 + 2*pow(x_this, 3) - y_this*yp_this)
	return ans


def fy_func(x_this, y_this, yp_this):
	ans = -0.125*yp_this
	return ans


def fyp_func(x_this, y_this, yp_this):
	ans = -0.125*y_this
	return ans


# Input
# a, b, alpha, beta, N, TOL, M = insert_values()
a = float(input("Enter a: "))
b = float(input("Enter b: "))
alpha = float(input("Enter alpha: "))
beta = float(input("Enter beta: "))
N = int(input("Enter N (N>=2): "))
TOL = int(input("Enter TOL: 10^...:"))
TOL = pow(10, TOL)
M = int(input("Enter M: "))

beta = 43/3

# Initialize u and v and w
newN = N + 1
w1 = [0] * newN
w2 = [0] * newN

# Step 1
h = (b - a) / N
k = 1
TK = (beta - alpha) / (b - a)

# Step 2
while k <= M:  # Do Steps 3-10
	# Step 3
	w1[0] = alpha
	w2[0] = TK
	u1 = 0
	u2 = 1

	# Step 4
	for i in range(1, N+1):  # Do steps 5 and 6
		# The Runge-Kutta method for systems is used in Steps 5 and 6
		# Step 5
		x = a + (i - 1) * h

		# Step 6
		k11 = h * w2[i - 1]
		k12 = h * (f_func(x, w1[i - 1], w2[i - 1]))
		k21 = h * (w2[i - 1] + 0.5 * k12)
		k22 = h * (f_func(x + h / 2, w1[i - 1] + 0.5 * k11, w2[i - 1] + 0.5 * k12))
		k31 = h * (w2[i - 1] + 0.5 * k22)
		k32 = h * (f_func(x + h / 2, w1[i - 1] + 0.5 * k21, w2[i - 1] + 0.5 * k22))
		k41 = h * (w2[i - 1] + k32)
		k42 = h * (f_func(x + h, w1[i - 1] + k31, w2[i - 1] + k32))

		w1[i] = w1[i - 1] + (k11 + 2 * k21 + 2 * k31 + k41) / 6
		w2[i] = w2[i - 1] + (k12 + 2 * k22 + 2 * k32 + k42) / 6

		kp11 = h * u2
		kp12 = h * (fy_func(x, w1[i - 1], w2[i - 1]) * u1 + fyp_func(x, w1[i - 1], w2[i - 1] * u2))
		kp21 = h * (u2 + 0.5 * kp12)
		kp22 = h * (fy_func(x + h / 2, w1[i - 1], w2[i - 1]) * (u1 + 0.5 * kp11) +
					fyp_func(x + h / 2, w1[i - 1], w2[i - 1]) * (u2 + 0.5 * kp12))
		kp31 = h * (u2 + 0.5 * kp22)
		kp32 = h * (fy_func(x + h / 2, w1[i - 1], w2[i - 1]) * (u1 + 0.5 * kp21) +
					fyp_func(x + h / 2, w1[i - 1], w2[i - 1]) * (u2 + 0.5 * kp22))
		kp41 = h * (u2 + kp32)
		kp42 = h * (fy_func(x + h, w1[i - 1], w2[i - 1]) * (u1 + 0.5 * kp31) +
					fyp_func(x + h, w1[i - 1], w2[i - 1]) * (u2 + 0.5 * kp32))

		u1 = u1 + (kp11 + 2 * kp21 + 2 * kp31 + kp41) / 6
		u2 = u2 + (kp12 + 2 * kp22 + 2 * kp32 + kp42) / 6

	# Step 7
	g = math.fabs(w1[N] - beta)
	if g <= TOL:  # do Steps 8 and 9
		# Step 8
		for i in range(0, N+1):
			x = a + i * h
			# print("xi\t\t\t u1_i\t\t\t v1_i\t\t wi=y(xi)\t\t\t w2_i")
			print("{:.1f}\t\t {:.6f}\t\t {:.6f}".format(x, w1[i], w2[i]))

	# Step 9 - STOP

	# Step 10
	TK = TK - (w1[N] - beta) / u1
	k = k + 1

# Step 11 - STOP
print("The procedure was unsuccessful.")

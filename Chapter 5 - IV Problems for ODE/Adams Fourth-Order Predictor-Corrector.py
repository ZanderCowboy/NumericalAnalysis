from math import fabs
from math import exp


def func(t_i, w_i):
	y = w_i
	# dy_dt = y - t_i ** 2 + 1
	dy_dt = t_i + y

	return dy_dt


def y_func(t_y):
	y = ((t_y + 1) ** 2) - (0.5 * exp(t_y))

	return y


# INPUT
# a, b, N, alpha = 0, 2, 10, 0.5
a = float(input("Enter a: "))
b = float(input("Enter b: "))
N = int(input("Enter N: "))
alpha = float(input("Enter alpha: "))
print("-" * 56)

# OUTPUT
print("ti\t\tyi = y(ti)\t\t\twi\t\t\tError: |yi - wi|")
print("-" * 56)

# STEP 1
h = (b - a) / N
t_list = [a, 0, 0, 0]
w_list = [alpha, 0, 0, 0]
y_value = y_func(t_list[0])
error = fabs(y_value - w_list[0])
# print("{:.1f}\t\t{:.7f}".format(t_list[0], w_list[0]))
print("{:.1f}\t\t{:.7f}\t\t{:.7f}\t\t\t{:.7f}".format(t_list[0], y_value, w_list[0], error))

# STEP 2 - Compute starting values using Runge-Kutta method
for i in range(1, 4):
	# STEP 3
	k1 = h * func(t_list[i - 1], w_list[i - 1])
	k2 = h * func(t_list[i - 1] + (h / 2), w_list[i - 1] + (k1 / 2))
	k3 = h * func(t_list[i - 1] + (h / 2), w_list[i - 1] + (k2 / 2))
	k4 = h * func(t_list[i - 1] + h, w_list[i - 1] + k3)

	# STEP 4
	w_list[i] = w_list[i - 1] + (k1 + (2 * k2) + (2 * k3) + k4) / 6
	t_list[i] = a + i * h

	# STEP 5
	y_value = y_func(t_list[i])
	error = fabs(y_value - w_list[i])
	print("{:.1f}\t\t{:.7f}\t\t{:.7f}\t\t\t{:.7f}".format(t_list[i], y_value, w_list[i], error))

# STEP 6
for i in range(4, N + 1):
	# STEP 7
	t = a + i * h

	# predict wi
	w = w_list[3] + h * ((55 * func(t_list[3], w_list[3]) - 59 * func(t_list[2], w_list[2]) + 37 * func(t_list[1], w_list[1]) - 9 * func(t_list[0], w_list[0])) / 24)
	w_p = w
	# correct wi
	w = w_list[3] + h * (
				(9 * func(t, w) + 19 * func(t_list[3], w_list[3]) - 5 * func(t_list[2], w_list[2]) + func(t_list[1], w_list[1])) / 24)

	y_value = y_func(t)
	error = fabs(y_value - w)

	# STEP 8
	# print("{:.7f}, {:.7f}, {:.7f}".format(t, w_p, w))
	print("{:.1f}\t\t{:.7f}\t\t{:.7f}\t\t\t{:.7f}".format(t, y_value, w, error))

	# STEP 9
	for j in range(0, 3):
		# Prepare for next iteration
		t_list[j] = t_list[j + 1]
		w_list[j] = w_list[j + 1]

	# STEP 10
	t_list[3] = t
	w_list[3] = w

# STEP 11
print("-" * 56)
# STOP

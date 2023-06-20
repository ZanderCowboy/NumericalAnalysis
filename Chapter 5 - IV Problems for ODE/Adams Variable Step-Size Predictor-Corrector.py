from math import fabs
from math import pow
from math import exp


def y_func(t_y):
	y = ((t_y + 1) ** 2) - (0.5 * exp(t_y))

	return y


def func(t_i, w_i):
	y = w_i
	dy_dt = y - t_i ** 2 + 1

	return dy_dt


# STEP 1
def runge_kutta_4(h_i, v0, x0):
	# print("h_i: {} \t v0: {} \t x0: {}".format(h_i, v0, x0))
	v_list = [v0, 0, 0, 0]
	x_list = [x0, 0, 0, 0]

	for j in range(1, 4):
		k1 = h_i * func(x_list[j-1], v_list[j-1])
		k2 = h_i * func(x_list[j-1] + (h_i / 2), v_list[j-1] + (k1 / 2))
		k3 = h_i * func(x_list[j-1] + (h_i / 2), v_list[j-1] + (k2 / 2))
		k4 = h_i * func(x_list[j-1] + h_i, v_list[j-1] + k3)
		v_list[j] = v_list[j-1] + ((k1 + 2*k2 + 2*k3 + k4) / 6)
		x_list[j] = x_list[0] + j*h_i

	return v_list, x_list


def output():
	print("\ti\t\tti\t\t\t\ty(ti)\t\t\twi\t\t\t\thi\t\t\tsigma_i\t\t\tError: |yi - wi|")
	print("-" * 100)


# INPUT
a, b, alpha, TOL, h_max, h_min = 0, 2, 0.5, -5, 0.2, 0.01
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# alpha = float(input("Enter alpha: "))
# TOL = int(input("Enter TOL 10^...: "))
# h_max = float(input("Enter max step size: "))
# h_min = float(input("Enter min step size: "))

TOL = 10 ** TOL
list_size = int(h_max / h_min) + 1

# STEP 2
t_list = [0] * list_size
t_list[0] = a
w_list = [0] * list_size
w_list[0] = alpha
h = h_max
FLAG = 1  # FLAG will be used to exit the loop in STEP 4
LAST = 0  # LAST will indicate when the last value is calculated
output()
print("{:.0f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}"
	  .format(0, t_list[0], y_func(t_list[0]), w_list[0]))

# STEP 3
w_new_list, t_new_list = runge_kutta_4(h, w_list[0], t_list[0])
# assign values from new lists to old lists
for z in range(1, 4):
	w_list[z] = w_new_list[z]
	t_list[z] = t_new_list[z]

N_FLAG = 1  # Indicates computation from runge_kutta_4
i = 4
t = t_list[3] + h


# STEP 4
while FLAG == 1:  # Do steps 5-20
	# STEP 5
	# Predict wi
	WP = w_list[i-1] + ((h/24)*(55*func(t_list[i-1], w_list[i-1]) - 59*func(t_list[i-2], w_list[i-2])
								+ 37*func(t_list[i-3], w_list[i-3]) - 9*func(t_list[i-4], w_list[i-4])))
	# Correct wi
	WC = w_list[i-1] + ((h/24)*(9*func(t, WP) + 19*func(t_list[i-1], w_list[i-1]) - 5*func(t_list[i-2], w_list[i-2])
								+ func(t_list[i-3], w_list[i-3])))
	sigma = (19*fabs(WC - WP))/(270*h)

	# STEP 6
	if sigma <= TOL:  # do STEPS 7-16 - Result accepted
		# STEP 7
		w_list[i] = WC
		t_list[i] = t

		# STEP 8
		if N_FLAG == 1:
			for p in (i-3, i-2, i-1, i):
				# Previous results also accepted
				error = fabs(y_func(t_list[p]) - w_list[p])
				print("{:.0f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}"
					  .format(p, t_list[p], y_func(t_list[p]), w_list[p], h, sigma, error))
		else:
			# Previous results already accepted
			error = fabs(y_func(t_list[i]) - w_list[i])
			print("{:.0f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}\t\t{:.8f}"
				  .format(i, t_list[i], y_func(t_list[i]), w_list[i], h, sigma, error))

		# STEP 9
		if LAST == 1:
			FLAG = 0  # Next STEP is 20
		else:  # do STEPS 10-16
			# STEP 10
			i = i + 1
			N_FLAG = 0

			# STEP 11
			if sigma <= 0.1*TOL or (t_list[i-1] + h) > b:  # do STEPS 12-16
				# Increase h if it is more accurate than required or decrease h to include b as a mesh point
				# STEP 12
				q = pow(TOL / (2 * sigma), 0.25)

				# STEP 13
				if q > 4:
					h = 4*h
				else:
					h = q*h

				# STEP 14
				if h > h_max:
					h = h_max

				# STEP 15
				if (t_list[i-1] + 4*h) > b:
					h = (b - t_list[i-1]) / 4
					LAST = 1

				# STEP 16
				w_new_list, t_new_list = runge_kutta_4(h, w_list[i-1], t_list[i-1])
				# assign values from new lists to old lists
				l = 1
				for z in (i, i+1, i+2):
					# print("w_new_list[z]: {:.7f} \t t_new_list[z]: {:.7f}".format(w_new_list[l], t_new_list[l]))
					w_list[z] = w_new_list[l]
					t_list[z] = t_new_list[l]
					l += 1

				N_FLAG = 1
				i = i + 3  # True branch completed. End STEP 6...
				# Next STEP is 20

	else:  # do STEPS 17-19 - Result rejected
		# STEP 17
		q = pow((TOL/(2 * sigma)), 0.25)  # False branch from STEP 6: Result rejected

		# STEP 18
		if q < 0.1:
			h = 0.1 * h
		else:
			h = q*h

		# STEP 19
		if h < h_min:
			FLAG = 0
			print("h_min exceeded")
		else:
			if N_FLAG == 1:
				i = i - 3
				# Previous results also rejected
			w_new_list, t_new_list = runge_kutta_4(h, w_list[i-1], t_list[i-1])
			# assign values from new lists to old lists
			g = 1
			for z in (i, i+1, i+2):
				# print("w_new_list[z]: {:.7f} \t t_new_list[z]: {:.7f}".format(w_new_list[z], t_new_list[z]))
				w_list[z] = w_new_list[g]
				t_list[z] = t_new_list[g]
				g += 1
			# if i in range(0, 4):
			# 	for z in (i, i+1, i+2):
			# 		# print("w_new_list[z]: {:.7f} \t t_new_list[z]: {:.7f}".format(w_new_list[z], t_new_list[z]))
			# 		w_list[z] = w_new_list[z]
			# 		t_list[z] = t_new_list[z]
			# else:
			# 	w_list[i] = w_new_list[1]
			# 	w_list[i+1] = w_new_list[2]
			# 	w_list[i+2] = w_new_list[3]

			i = i + 3
			N_FLAG = 1  # End STEP 6

	# STEP 20
	t = t_list[i-1] + h  # End STEP 4

# STEP 21
# STOP

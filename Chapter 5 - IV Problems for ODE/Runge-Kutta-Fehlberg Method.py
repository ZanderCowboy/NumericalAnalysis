# RKF-4 Method
from math import fabs


def func(t0, w0):
	ti = t0
	yi = w0

	dy_dt = yi - ti**2 + 1

	return dy_dt


# INPUT
a, b, alpha, TOL, h_max, h_min = 0, 2, 0.5, -5, 0.25, 0.01
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# alpha = float(input("Enter alpha: "))
# TOL = float(input("Enter TOL 10^(...): "))
# h_max = float(input("Max step size: "))
# h_min = float(input("Min step size: "))

# STEP 1
TOL = 10 ** TOL
t = a
w = alpha
h = h_max
FLAG = 1
print("({:.7f}, {:.7f})\n".format(t, w))
print("\tt \t\t\t w \t\t\t h")

# STEP 2
while FLAG == 1:
	# STEP 3
	k1 = h * func(t, w)
	k2 = h * func(t + ((1/4)*h), w + ((1/4)*k1))
	k3 = h * func(t + ((3/8)*h), w + ((3/32)*k1) + ((9/32)*k2))
	k4 = h * func(t + ((12/13)*h), w + ((1932/2197)*k1) - ((7200/2197)*k2) + ((7296/2197)*k3))
	k5 = h * func(t + h, w + ((439/216)*k1) - (8*k2) + ((3680/513)*k3) - ((845/4104)*k4))
	k6 = h * func(t + ((1/2)*h), w - ((8/27)*k1) + (2*k2) - ((3544/2565)*k3) + ((1859/4104)*k4) - ((11/40)*k5))
	# print("{:.7f}, {:.7f}, {:.7f}, {:.7f}, {:.7f}, {:.7f}".format(k1, k2, k3, k4, k5, k6))

	# STEP 4
	R = (1/h)*fabs(((1/360)*k1) - ((128/4275)*k3) - ((2197/75240)*k4) + ((1/50)*k5) + ((2/55)*k6))

	# STEP 5
	if R <= TOL:
		# STEP 6
		t = t + h
		w = w + ((25/216)*k1) + ((1408/2565)*k3) + ((2197/4104)*k4) - ((1/5)*k5)

		# STEP 7
		print("({:.7f}, {:.7f}, {:.7f})".format(t, w, h))

	# STEP 8
	delta = 0.84 * ((TOL / R) ** (1/4))

	# STEP 9
	if delta <= 0.1:
		h = 0.1 * h
	elif delta >= 4:
		h = 4 * h
	else:
		h = delta * h

	# STEP 10
	if h > h_max:
		h = h_max

	# STEP 11
	if t >= b:
		FLAG = 0
	elif t + h > b:
		h = b - t
	elif h < h_min:
		FLAG = 0
		print("Minimum h exceeded")

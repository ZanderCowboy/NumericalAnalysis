from math import fabs as abs_val


def func_y_d(x_val, y_val, z_val):
	some_ans = 0
	some_ans = z_val

	return some_ans


def func_z_d(x_val, y_val, z_val):
	some_ans = 0
	some_ans = -(z_val**2) + (9*x_val*y_val) - 9*(x_val**3) \
			   + 36*(x_val**2) + 6*x_val - 6

	return some_ans


def analysis(g_1, g_2, r_1, r_2, g_3):
	print("Error analysis: ")
	print("Guess 1:\t {:.9f}".format(g_1))
	print("Guess 2:\t {:.9f}".format(g_2))
	print("Result 1:\t {:.9f}".format(r_1))
	print("Result 2:\t {:.9f}".format(r_2))
	print("*" * 25)
	print("Guess 3:\t {:.9f}\n\n".format(g_3))


def question_3():
	number = 6
	h = 0.2
	x_vec = [0] * number
	y_vec = [0] * number
	z_vec = [0] * number
	z_initial = [0] * number

	# initialization
	z_initial[0] = -2.99
	z_initial[1] = -3.01
	guess_1, guess_2 = z_initial[0], z_initial[1]
	result_1, result_2 = 0, 0
	guess_3 = 0
	desired_result = -4

	TOL = 10**-3

	k = 0
	while True:
		x_vec[0] = 1
		y_vec[0] = -2

		if k == 0:
			z_vec[0] = z_initial[0]
		elif k == 1:
			z_vec[0] = z_initial[1]
		else:
			# z_vec[0] = guess_3

			z_vec[0] = round(guess_3, 9)

		for i in range(number-1):
			x, y, z = x_vec[i], y_vec[i], z_vec[i]

			z_p = z_vec[i] + h*func_z_d(x, y, z)
			y_p = y_vec[i] + h*func_y_d(x, y, z)

			# Corrector
			z_vec[i+1] = z_vec[i] + (h/2)*(func_z_d(x, y, z) + func_z_d(x + h, y_p, z_p))
			y_vec[i+1] = y_vec[i] + (h/2)*(func_y_d(x, y, z) + func_y_d(x + h, y_p, z_p))

			x_vec[i+1] = x_vec[i] + h


		if k == 0:
			result_1 = y_vec[5]
		elif k == 1:
			result_2 = y_vec[5]
		else:
			guess_1 = guess_2
			guess_2 = z_vec[0]

			result_1 = result_2
			result_2 = y_vec[5]

		if k != 0:
			guess_3 = guess_2 + ((desired_result - result_2)*(guess_1 - guess_2))/(result_1 - result_2)

		print("Iteration {}".format(k+1))
		print("x\t\t\ty\t\t\t\tz")
		for i in range(number):
			print("{:.1f}\t{:.9f}\t{:.9f}".format(x_vec[i], y_vec[i], z_vec[i]))

		analysis(guess_1, guess_2, result_1, result_2, guess_3)

		if abs_val(guess_2 - guess_1) < TOL:
			break

		k += 1

	# ANALYTICAL SOLUTION
	y_func = [0] * number
	z_func = [0] * number
	for i in range(number-1):
		x_vec[i+1] = x_vec[i] + h
	for i in range(number):
		y_func[i] = x_vec[i]**3 - 3*(x_vec[i]**2)
		z_func[i] = 3*(x_vec[i]**2) - 6*x_vec[i]

	print("Analytical Solution")
	print("x\t\t\ty\t\t\tz")
	for i in range(number):
		print("{:.1f}\t\t{:.4f}\t\t{:.4f}".format(x_vec[i], y_func[i], z_func[i]))


def question_5():
	m = 4
	n = 3
	u_old = [0] * (m*n)
	u_new = [0] * (m*n)

	TOL = 10**-5
	w = 1.21052
	avg = 60.00

	print("Starting interior point values: {}".format(avg))
	print("Tolerance: {}\n".format(TOL))

	print("Iteration: 0")
	for i in range(m*n):
		u_old[i] = avg
		print("u{}\t\t{:.8f}".format(i+1, u_old[i]))

	exit_bool = False
	j = 1
	while not exit_bool:
		print("\nIteration: {}".format(j))

		u_new[0] = (1-w)*u_old[0] + (w/4)*(125 + 70 + u_old[1] + u_old[3])
		u_new[1] = (1-w)*u_old[1] + (w/4)*(u_new[0] + 50 + u_old[2] + u_old[4])
		u_new[2] = (1-w)*u_old[2] + (w/4)*(u_new[1] + 30 + 0 + u_old[5])

		u_new[3] = (1-w)*u_old[3] + (w/4)*(150 + u_new[0] + u_old[4] + u_old[6])
		u_new[4] = (1-w)*u_old[4] + (w/4)*(u_new[3] + u_new[1] + u_old[5] + u_old[7])
		u_new[5] = (1-w)*u_old[5] + (w/4)*(u_new[4] + u_new[2] + 0 + u_old[8])

		u_new[6] = (1-w)*u_old[6] + (w/4)*(135 + u_new[3] + u_old[7] + u_old[9])
		u_new[7] = (1-w)*u_old[7] + (w/4)*(u_new[6] + u_new[4] + u_old[8] + u_old[10])
		u_new[8] = (1-w)*u_old[8] + (w/4)*(u_new[7] + u_new[5] + 0 + u_old[11])

		u_new[9] = (1-w)*u_old[9] + (w/4)*(110 + u_new[6] + u_old[10] + 90)
		u_new[10] = (1-w)*u_old[10] + (w/4)*(u_new[9] + u_new[7] + u_old[11] + 70)
		u_new[11] = (1-w)*u_old[11] + (w/4)*(u_new[10] + u_new[8] + 0 + 50)

		for i in range(m*n):
			print("u{}\t\t{:.8f}".format(i+1, u_new[i]))

		for i in range(m*n):
			if abs_val(u_new[i] - u_old[i]) < TOL:
				exit_bool = True
			u_old[i] = u_new[i]

		j += 1


def question_6():
	m = 4
	nn = 3
	u_old = [0] * (m*nn)
	v_old = [0] * (m*nn)
	u_new = [0] * (m*nn)
	v_new = [0] * (m*nn)

	TOL = 10**-5
	avg = 60

	for i in range(m*nn):
		u_old[i] = avg
		v_old[i] = avg

	v_right = [0] * 12
	u_right = [0] * 12

	exit_value = 0
	j = 1
	while exit_value != -99:
		print("\nIteration: {}".format(j))

		v_right[0] = 200 - v_old[0] + v_old[1]
		v_right[1] = 70 - v_old[4] + v_old[5]
		v_right[2] = 50 - v_old[8] + v_old[9]

		v_right[3] = 135 + v_old[0] - v_old[1] + v_old[2]
		v_right[4] = v_old[4] - v_old[5] + v_old[6]
		v_right[5] = v_old[8] - v_old[9] + v_old[10]

		v_right[6] = 150 + v_old[1] - v_old[2] + v_old[3]
		v_right[7] = v_old[5] - v_old[6] + v_old[7]
		v_right[8] = v_old[9] - v_old[10] + v_old[11]

		v_right[9] = 195 + v_old[2] - v_old[3]
		v_right[10] = 50 + v_old[6] - v_old[7]
		v_right[11] = 30 + v_old[10] - v_old[11]

		########################################################################
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

		a = [[3, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, v_right[0]],
			 [-1, 3, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, v_right[1]],
			 [0, -1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, v_right[2]],
			 [0, 0, 0, 3, -1, 0, 0, 0, 0, 0, 0, 0, v_right[3]],
			 [0, 0, 0, -1, 3, -1, 0, 0, 0, 0, 0, 0, v_right[4]],
			 [0, 0, 0, 0, -1, 3, 0, 0, 0, 0, 0, 0, v_right[5]],
			 [0, 0, 0, 0, 0, 0, 3, -1, 0, 0, 0, 0, v_right[6]],
			 [0, 0, 0, 0, 0, 0, -1, 3, -1, 0, 0, 0, v_right[7]],
			 [0, 0, 0, 0, 0, 0, 0, -1, 3, 0, 0, 0, v_right[8]],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, -1, 0, v_right[9]],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 3, -1, v_right[10]],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 3, v_right[11]]]

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

		########################################################################
		for i in range(12):
			u_new[i] = x[i]

		#
		u_right[0] = 200 - u_new[0] + u_new[1]
		u_right[1] = 135 - u_new[3] + u_new[4]
		u_right[2] = 150 - u_new[6] + u_new[7]
		u_right[3] = 195 - u_new[9] + u_new[10]
		u_right[4] = 70 + u_new[0] - u_new[1] + u_new[2]
		u_right[5] = u_new[3] - u_new[4] + u_new[5]
		u_right[6] = u_new[6] - u_new[7] + u_new[8]
		u_right[7] = 50 + u_new[9] - u_new[10] + u_new[11]
		u_right[8] = 50 + u_new[1] - u_new[2]
		u_right[9] = u_new[4] - u_new[5]
		u_right[10] = u_new[7] - u_new[8]
		u_right[11] = 30 + u_new[10] - u_new[11]

		########################################################################
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

		a = [[3, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u_right[0]],
			 [-1, 3, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, u_right[1]],
			 [0, -1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, u_right[2]],
			 [0, 0, 0, 3, -1, 0, 0, 0, 0, 0, 0, 0, u_right[3]],
			 [0, 0, 0, -1, 3, -1, 0, 0, 0, 0, 0, 0, u_right[4]],
			 [0, 0, 0, 0, -1, 3, 0, 0, 0, 0, 0, 0, u_right[5]],
			 [0, 0, 0, 0, 0, 0, 3, -1, 0, 0, 0, 0, u_right[6]],
			 [0, 0, 0, 0, 0, 0, -1, 3, -1, 0, 0, 0, u_right[7]],
			 [0, 0, 0, 0, 0, 0, 0, -1, 3, 0, 0, 0, u_right[8]],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, -1, 0, u_right[9]],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 3, -1, u_right[10]],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 3, u_right[11]]]

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

		########################################################################
		for i in range(12):
			v_new[i] = x[i]

		for i in range(m*nn):
			print("{}\t{:.8f}".format(i+1, v_new[i]))

			# exit_value = int(input("Exit	Yes(-99) | No(1)? "))
		for i in range(m*nn):
			if abs_val(v_new[i] - v_old[i]) < TOL:
				exit_value = -99
			else:
				exit_value = 1
			v_old[i] = v_new[i]

		j += 1


# question_3()
# question_5()
# question_6()

def func(t0, w0):
	ti = t0
	yi = w0
	# TODO
	dy_dt = yi - ti**2 + 1

	return dy_dt


# a, b, N, alpha = 0, 2, 10, 0.5
a = float(input("Enter a: "))
b = float(input("Enter b: "))
N = int(input("Enter N: "))
alpha = float(input("Enter alpha: "))

h = (b - a) / N
t = a
w = alpha
print("({:f}, {:f})".format(t, w))

for i in range(1, N+1):
	x = t + (h / 2)
	y = w + ((h / 2) * func(t, w))
	w = w + (h * func(x, y))
	t = a + (i * h)
	print("({:f}, {:f})".format(t, w))

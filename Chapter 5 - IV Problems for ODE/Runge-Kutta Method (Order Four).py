def func(t0, w0):
    ti = t0
    yi = w0

    dy_dt = yi - ti**2 + 1

    return dy_dt


a, b, N, alpha = 0, 2, 20, 0.5
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# N = int(input("Enter N: "))
# alpha = float(input("Enter alpha: "))

h = (b - a) / N
t = a
w = alpha
print("({:f}, {:f})".format(t, w))

for i in range(1, N+1):
    k1 = h * func(t, w)
    k2 = h * func(t + (h / 2), w + (k1 / 2))
    k3 = h * func(t + (h / 2), w + (k2 / 2))
    k4 = h * func(t + h, w + k3)

    w = w + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)
    t = a + (i * h)

    print("({:f}, {:f})".format(t, w))

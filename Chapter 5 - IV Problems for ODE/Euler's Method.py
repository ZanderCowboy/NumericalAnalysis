def func(t0, w0):
    ti = t0
    yi = w0
    # TODO
    # dy_dt = yi - ti**2 + 1
    # dy_dt = ti / yi

    return dy_dt


# a, b, N, alpha = 0, 2, 10, 0.5
# print("If values not provided, please enter -1")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
N = int(input("Enter N: "))
# if h == 0:
#     h = float(input("Enter h: "))
alpha = float(input("Enter alpha: "))

h = (b - a) / N
t = a
w = alpha
print("({:f}, {:f})".format(t, w))

for i in range(1, N+1):
    w = w + (h * func(t, w))
    t = a + (i * h)
    print("({:f}, {:f})".format(t, w))

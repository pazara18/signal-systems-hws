import numpy as np
import matplotlib.pyplot as plt
import control
import sympy as sp

# coefficients of numerator and denominator as parameters to create transfer function
G = control.tf([0, 0, 0.1, 0, 0], [10 ** (-6), 22 * 10 ** (-5), 141 * 10 ** (-4), 22 * 10 ** (-2), 1])

a = control.bode_plot(G, dB=True, omega_limits=[1, 1000])
plt.show()

# given x(t)
x_t = lambda t: 10 * (np.sin(2 * np.pi * t) + np.sin(10 * np.pi * t) + np.sin(100 * np.pi * t))

# range of t values
t_sample = np.arange(0, 2, 0.002)
T, y_t = control.forced_response(G, t_sample, x_t(t_sample))
plt.plot(T, x_t(t_sample), label="x(t)")
plt.plot(T, y_t, label="y(t)")
plt.legend()
plt.show()

s = sp.Symbol("s")
t = sp.Symbol("t")
z = sp.Symbol("z")

G_s = ((0.1 * s ** 2) / ((10 ** (-6) * s ** 4) + (22 * 10 ** (-5) * s ** 3) + (141 * 10 ** (-4) * s ** 2) + (
            22 * 10 ** (-2) * s) + 1)).subs(s, 1000 * (1 - z ** (-1)) / (1 + z ** (-1)))

print("H(z) = ", end='')
print(sp.simplify(G_s))

# define a sympy symbol to define the system
n = sp.Symbol("n")
# system (using inverse z transform from wolfram alpha)
dscrt_sys = 400000 * 9 ** (n - 4) * 1111 ** (-n - 2) * (
            100 * 11 ** (2 * n) * n + 101 ** (n + 2) * n - 11111 * 11 ** (2 * n) + 101 ** (n + 2)) * (
                        1 - sp.Heaviside(-n, 1)) + 0.0810162 * sp.Heaviside(-n, 1)

# t values to sample the system and the input
n_sample = np.arange(0, 1000, 1)

# calculating the values at the given sample times for the system
scalar_func = lambda x: float(dscrt_sys.evalf(subs={n: x}))
vector_func = np.vectorize(scalar_func)
system_t = vector_func(n_sample)

# convolve h and x
res = np.convolve(system_t, x_t(t_sample), mode="full")
# take first 1000 values
res = res[0:1000]
plt.scatter(n_sample, res, s=10)
plt.show()

err = y_t - res
for val in err:
    val = abs(val)
abs_mean = np.mean(err)
print("Absolute mean is: ", end='')
print(abs_mean)

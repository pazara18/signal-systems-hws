# This is the code for parts b and c of Term Project
# Author: Abdulkadir Pazar
# Date: 12/06/2021
# No: 150180028

from scipy.io import wavfile
import numpy as np
# import sympy as sp
# s = sp.Symbol("s")
# z = sp.Symbol("z")
# w_cl = sp.Symbol("w_cl")
# w_ch = sp.Symbol("w_ch")
# T = sp.Symbol("T")
#
# G_s = ((w_cl ** (-3) * s ** 3) / ((1+s/w_cl)**3 * (1+s/w_ch)**3))
# G_s = G_s.subs(s, 2/T * (1 - z ** (-1)) / (1 + z ** (-1)))
#
# print(sp.collect((sp.simplify(G_s).expand()), z))

# We obtain the coefficients for the Z transfer function by using sympy and commented lines above

filename = "WinnerTakesAll.wav"
sample_rate, data = wavfile.read(filename)

T = 1/sample_rate
f_c = 1700
BW = 1300/1700
f_cl = 2 * np.pi * int(f_c - BW * f_c)
f_ch = 2 * np.pi * int(f_c + BW * f_c)

b_0 = 8*T**3*f_ch**3
b_2 = -24*T**3*f_ch**3
b_4 = +24*T**3*f_ch**3
b_6 = -8*T**3*f_ch**3

a_0 = T**6*f_ch**3*f_cl**3 + 6*T**5*f_ch**3*f_cl**2 + 6*T**5*f_ch**2*f_cl**3 + 12*T**4*f_ch**3*f_cl + 36*T**4*f_ch**2*f_cl**2 + 12*T**4*f_ch*f_cl**3 + 8*T**3*f_ch**3 + 72*T**3*f_ch**2*f_cl + 72*T**3*f_ch*f_cl**2 + 8*T**3*f_cl**3 + 48*T**2*f_ch**2 + 144*T**2*f_ch*f_cl + 48*T**2*f_cl**2 + 96*T*f_ch + 96*T*f_cl + 64
a_1 = 6*T**6*f_ch**3*f_cl**3 + 24*T**5*f_ch**3*f_cl**2 + 24*T**5*f_ch**2*f_cl**3 + 24*T**4*f_ch**3*f_cl + 72*T**4*f_ch**2*f_cl**2 + 24*T**4*f_ch*f_cl**3 - 96*T**2*f_ch**2 - 288*T**2*f_ch*f_cl - 96*T**2*f_cl**2 - 384*T*f_ch - 384*T*f_cl - 384
a_2 = 15*T**6*f_ch**3*f_cl**3 + 30*T**5*f_ch**3*f_cl**2 + 30*T**5*f_ch**2*f_cl**3 - 12*T**4*f_ch**3*f_cl - 36*T**4*f_ch**2*f_cl**2 - 12*T**4*f_ch*f_cl**3 - 24*T**3*f_ch**3 - 216*T**3*f_ch**2*f_cl - 216*T**3*f_ch*f_cl**2 - 24*T**3*f_cl**3 - 48*T**2*f_ch**2 - 144*T**2*f_ch*f_cl - 48*T**2*f_cl**2 + 480*T*f_ch + 480*T*f_cl + 960
a_3 = 20*T**6*f_ch**3*f_cl**3 - 48*T**4*f_ch**3*f_cl - 144*T**4*f_ch**2*f_cl**2 - 48*T**4*f_ch*f_cl**3 + 192*T**2*f_ch**2 + 576*T**2*f_ch*f_cl + 192*T**2*f_cl**2 - 1280
a_4 = 15*T**6*f_ch**3*f_cl**3 - 30*T**5*f_ch**3*f_cl**2 - 30*T**5*f_ch**2*f_cl**3 - 12*T**4*f_ch**3*f_cl - 36*T**4*f_ch**2*f_cl**2 - 12*T**4*f_ch*f_cl**3 + 24*T**3*f_ch**3 + 216*T**3*f_ch**2*f_cl + 216*T**3*f_ch*f_cl**2 + 24*T**3*f_cl**3 - 48*T**2*f_ch**2 - 144*T**2*f_ch*f_cl - 48*T**2*f_cl**2 - 480*T*f_ch - 480*T*f_cl + 960
a_5 = 6*T**6*f_ch**3*f_cl**3 - 24*T**5*f_ch**3*f_cl**2 - 24*T**5*f_ch**2*f_cl**3 + 24*T**4*f_ch**3*f_cl + 72*T**4*f_ch**2*f_cl**2 + 24*T**4*f_ch*f_cl**3 - 96*T**2*f_ch**2 - 288*T**2*f_ch*f_cl - 96*T**2*f_cl**2 + 384*T*f_ch + 384*T*f_cl - 384
a_6 = T**6*f_ch**3*f_cl**3 - 6*T**5*f_ch**3*f_cl**2 - 6*T**5*f_ch**2*f_cl**3 + 12*T**4*f_ch**3*f_cl + 36*T**4*f_ch**2*f_cl**2 + 12*T**4*f_ch*f_cl**3 - 8*T**3*f_ch**3 - 72*T**3*f_ch**2*f_cl - 72*T**3*f_ch*f_cl**2 - 8*T**3*f_cl**3 + 48*T**2*f_ch**2 + 144*T**2*f_ch*f_cl + 48*T**2*f_cl**2 - 96*T*f_ch - 96*T*f_cl + 64

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
Y_arr = []
for X in data:
    A = X + (-a_1 * B -a_2 * C -a_3 * D -a_4 * E -a_5 * F -a_6 * G) / a_0
    Y = int((b_0 * A + b_2 * C + b_4 * E + b_6 * G) / a_0)
    Y_arr.append(Y)
    G = F
    F = E
    E = D
    D = C
    C = B
    B = A

BSP = data - np.array(Y_arr)
wavfile.write(filename[0:filename.rfind('.')] + "BPF" + ".wav", sample_rate, np.array(Y_arr).astype(np.int16))
wavfile.write(filename[0:filename.rfind('.')] + "BSP" + ".wav", sample_rate, BSP.astype(np.int16))

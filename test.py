from matplotlib import pyplot as plt
import numpy as np

# Resistor Voltage (simulation data)
V_sim = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, \
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]
# Gate-to-Source Voltage (sweep from 0 V to 5 V)
V_GS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
#fixed parameters
VDS = 5         # Drain-to-Source Voltage
V_TH = 0.69       # Treshold Voltage
beta = 4.5e-6   # Beta
r_sh = 25        # Sheet Resistance
#transistor variables
W = int(input("W (μm): "))      # Gate Width
W = W*(1e-6)
L = int(input("L (μm): "))      # Gate Length
L = L*(1e-6)
#resistor
m = int(input("m: "))       # squares
n = int(input("n: "))

n_l = (n + 1) / 2       # rows

R = r_sh * ((m * n_l) + (n_l - 1) - ((1 / 3)*(n_l - 1) * 2))
print("R: ", R, 'Ohms')

V = []
for i in range(len(V_GS)):
    if V_GS[i] <= V_TH:
        ID = 0.0
    else:
        ID = (beta/2)*(W/L)*((V_GS[i]-V_TH)**2)*(1 + 0.01*VDS)
    V.append(R*ID)

# mean square error
MSE = (1/len(V_sim))*(sum((np.array(V_sim)-np.array(V))**2))
print("MSE: ", round(100*MSE, 4), "%")

plt.figure(1)
plt.plot(V_GS,V_sim)
plt.plot(V_GS,V)
plt.grid()
plt.legend(['pre-built V','estimated V'])
plt.title("V_R vs V_GS")
plt.ylabel("Resistor Voltage (V)")
plt.xlabel("Gate-to-Source voltage (V)")
plt.show()
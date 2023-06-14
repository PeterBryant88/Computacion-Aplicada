import numpy as np

def fitness(R):

    V_sim = [1.001e-7, 2.50001e-2, 1.000001e-1, 2.250001e-1, 4.000001e-1, 6.250001e-1, 9.000001e-1, 1.225, 1.467761,
             1.844197, 2.070994]
    V_sw = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    # Arreglos para V_sim y V_sw
    vsw = np.array(V_sw)
    V_e = np.array(V_sim)

    # Resistencia de la Hoja
    R_sh = 25
    # Cálculo de la resistencia
    # Donde, Res = R_sheet * ((m * num_l) + (num_l-1) - ((2/3) * (num_l-1)))
    # Donde, num_l = (m + 1) / 2
    num_l = (R[3] + 1) / 2
    Res = R_sh * ((R[2] * num_l) + (num_l - 1) - ((2 / 3) * (num_l - 1)))

    # Parámetros de transconductancia del transistor
    Beta = 4.5e-6
    Gamma = 0.01
    # Voltaje de drenador
    V_DS = 5
    # Voltaje de umbral
    V_TH = 0.69

    # Cálculo de V_r = Res * I_D
    # Donde, I_D = (Beta / 2) * (W / L) * ((V_GS - V_TH) ** 2) * (1 + Gamma * V_DS)
    V_r = []
    for V_GS in vsw:
        V_r.append(Res * (Beta / 2) * (R[0] / R[1]) * ((V_GS - V_TH) ** 2) * (1 + Gamma * V_DS))

    # Cálculo de MSE = (1/n) * Sum (V_e - V_r)^2
    n = 11
    mse = (1 / n) * sum((V_e - np.array(V_r)) ** 2)
    mse = 1 / mse

    return mse
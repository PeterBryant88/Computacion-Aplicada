def gray2real(indiv):

    g1 = indiv[0:8] # Segmento de bits 0-9 <9=10-1>
    g2 = indiv[8:16]
    g3 = indiv[16:24]
    g4 = indiv[24:32]

    b1 = [g1[0]]
    b2 = [g2[0]]
    b3 = [g3[0]]
    b4 = [g4[0]]

    for i in range(0,7):
        b1.append(int(b1[i])^int(g1[i+1]))
        b2.append(int(b2[i])^int(g2[i+1]))
        b3.append(int(b3[i])^int(g3[i+1]))
        b4.append(int(b4[i])^int(g4[i+1]))

    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0

    for i in range(len(b1)):
        d1 += b1[i]*2**(7-i)
        d2 += b2[i]*2**(7-i)
        d3 += b3[i]*2**(7-i)
        d4 += b4[i]*2**(7-i)

    r1 = int(abs((d1 * 4 / 16) - 2))    # W = 2*L
    r2 = int(abs((d2 * 4 / 15) - 2))
    r3 = int(abs((d3 * 4 / 31) - 2))
    r4 = r3                             # m = n

    if abs(r2) < 0.5:
        r2 = 1

    R = [abs(r1), abs(r2), abs(r3), abs(r4)]

    return R
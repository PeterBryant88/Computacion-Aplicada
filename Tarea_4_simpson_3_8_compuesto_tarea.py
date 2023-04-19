import math

# Selector de funciones
def f(x,i):
    if i == 1:
        return math.exp(x**2)
    elif i == 2:
        return 1 + (math.exp(-x)) * (math.sin(4*x))
    elif i == 3:
        return math.sin(math.pi*x)
    elif i == 4:
        return 1 + (math.exp(-x)) * (math.cos(4*x))
    elif i == 5:
        return math.sin(math.sqrt(x))

# Regla de Simpson 3/8 Compuesta
def Simpson38C(a,b,n,fn):
    h = (b-a)/n # Tamaño del subintervalo
    # Acumulador de suma (integral)
    s = f(a,fn) + f(b,fn) # suma de f evaluada en los límites a y b
    # Bucle de suma de los subintervalos internos
    for i in range(1,n):
        k = a + (i*h) # Subintervalo en turno
        if i % 3 == 0: # Múltiplo de 3
            s += 2 * f(k,fn) # Suma de 2*f evaluada en k
        else:
            s += 3 * f(k,fn) # Suma de 2*f evaluada en k
    s = s * 3*h/8 # Factor de corrección 3/8
    return s # Resultado de la integral aproximada

def main():
    print("Integración por Método de Simpson 3/8 Compuesto")
    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))
    n = int(input("# de Subintervalos de integración: "))
    func = ["e^(x^2)", "1 + e^(-x) * sin(4x)", "sin(\u03C0x)",
            "1 + e^(-x) * cos(4x)", "sin(\u221Ax)"]
    print("Funciones y Resultados:")
    # Selector de función a resolver e imprimir
    for fn in range(1,6):
        s = Simpson38C(a,b,n,fn) # Llamada a función de integración
        print(f"{fn}. f(x) = {func[fn-1]}")
        # Bucle complementario para imprimir intervalos enteros o decimales
        if (a or b) <= 1:
            print(f"   \u222B{a}\u2192{b} f(x) dx = %0.9f" % (s))
        else:
            print(f"   \u222B{int(a)}\u2192{int(b)} f(x) dx = %0.9f" % (s))

main()

import math


# ======================================
#   FUNCION Y DERIVADA
# ======================================
def f(x):
    return x ** 3 - x ** 2 * math.e ** (-0.5 * x) - 3 * x + 1


def df(x):
    # Derivada: 3x^2 - [2x e^{-0.5x} - 0.5x^2 e^{-0.5x}] - 3
    return 3 * x ** 2 - (2 * x * math.e ** (-0.5 * x) - 0.5 * x ** 2 * math.e ** (-0.5 * x)) - 3


# ======================================
#   BISECCIÓN
# ======================================
def biseccion(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en el intervalo")

    xs, errors = [], []
    for k in range(max_iter):
        c = (a + b) / 2
        xs.append(c)
        errors.append(abs(f(c)))
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, k + 1, errors


# ======================================
#   NEWTON-RAPHSON
# ======================================
def newton(x0, tol=1e-6, max_iter=100):
    x = x0
    xs, errors = [x], [abs(f(x))]

    for k in range(max_iter):
        x = x - f(x) / df(x)
        xs.append(x)
        errors.append(abs(f(x)))
        if abs(f(x)) < tol:
            break
    return x, k + 1, errors


# ======================================
#   SECANTE
# ======================================
def secante(x0, x1, tol=1e-6, max_iter=100):
    xs = [x0, x1]
    errors = [abs(f(x0)), abs(f(x1))]

    for k in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x2
        xs.append(x2)
        errors.append(abs(f(x2)))
        if abs(f(x2)) < tol:
            break
    return x1, k + 1, errors


# ======================================
#   INTERVALOS A EVALUAR
# ======================================
intervalos = [
    (-1.5, -0.5),
    (0, 0.5),
    (1.5, 2)
]

print("\n====================================")
print("           RESULTADOS")
print("====================================")

for (a, b) in intervalos:
    print(f"\n>>> Intervalo: [{a}, {b}]")

    # Bisección
    xb, itb, eb = biseccion(a, b)

    # Newton (punto medio)
    x0 = (a + b) / 2
    xn, itn, en = newton(x0)

    # Secante
    xs, its, es = secante(a, b)

    # Resultados
    print(f"Bisección:       raíz = {xb:.10f}, iteraciones = {itb}, error = {eb[-1]:.2e}")
    print(f"Newton-Raphson:  raíz = {xn:.10f}, iteraciones = {itn}, error = {en[-1]:.2e}")
    print(f"Secante:         raíz = {xs:.10f}, iteraciones = {its}, error = {es[-1]:.2e}")

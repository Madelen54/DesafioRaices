import math


# ======================================
#   FUNCION Y DERIVADA
# ======================================
def f(x):
    return math.cos(x) ** 2 - 0.5 * x * math.e ** (0.3 * x) + 5


def df(x):
    # Derivada:
    # d/dx [cos^2(x)] = -2 cos(x) sin(x) = -sin(2x)
    # d/dx [-0.5 x e^{0.3x}] = -0.5 e^{0.3x} - 0.15 x e^{0.3x}
    return -math.sin(2 * x) - 0.5 * math.e ** (0.3 * x) - 0.15 * x * math.e ** (0.3 * x)


# ======================================
#   BISECCIÓN
# ======================================
def biseccion(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en el intervalo")

    errors = []
    for k in range(max_iter):
        c = (a + b) / 2
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
    errors = [abs(f(x))]

    for k in range(max_iter):
        x = x - f(x) / df(x)
        errors.append(abs(f(x)))
        if abs(f(x)) < tol:
            break
    return x, k + 1, errors


# ======================================
#   SECANTE
# ======================================
def secante(x0, x1, tol=1e-6, max_iter=100):
    errors = [abs(f(x0)), abs(f(x1))]

    for k in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x2
        errors.append(abs(f(x2)))
        if abs(f(x2)) < tol:
            break
    return x1, k + 1, errors


# ======================================
#   EJECUCIÓN
# ======================================
a, b = 3.7, 4.0
p0 = (a + b) / 2  # para Newton

# Bisección
xb, itb, eb = biseccion(a, b)

# Newton
xn, itn, en = newton(p0)

# Secante
xs, its, es = secante(a, b)

# ======================================
#   RESULTADOS
# ======================================
print("\n====================================")
print("      COMPARACIÓN FINAL")
print("====================================")
print(f"Bisección:       raíz = {xb:.10f}, iteraciones = {itb}, error final = {eb[-1]:.2e}")
print(f"Newton-Raphson:  raíz = {xn:.10f}, iteraciones = {itn}, error final = {en[-1]:.2e}")
print(f"Secante:         raíz = {xs:.10f}, iteraciones = {its}, error final = {es[-1]:.2e}")

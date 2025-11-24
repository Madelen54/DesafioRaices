import math

# ================================
#   FUNCION Y DERIVADA
# ================================
def f(x):
    return 3 * math.sin(0.5 * x) - 0.5 * x + 20

def df(x):
    return 3 * 0.5 * math.cos(0.5 * x) - 0.5   # f'(x)


# ================================
#   METODO DE BISECCION
# ================================
def biseccion(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en el intervalo, bisección no puede usarse.")

    iteraciones = 0
    while (b - a) / 2 > tol and iteraciones < max_iter:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteraciones += 1

    c = (a + b) / 2
    return c, iteraciones, abs(f(c))


# ================================
#   METODO DE NEWTON–RAPHSON
# ================================
def newton(x0, tol=1e-6, max_iter=100):
    x = x0
    iteraciones = 0

    while abs(f(x)) > tol and iteraciones < max_iter:
        x = x - f(x) / df(x)
        iteraciones += 1

    return x, iteraciones, abs(f(x))


# ================================
#   METODO DE LA SECANTE
# ================================
def secante(x0, x1, tol=1e-6, max_iter=100):
    iteraciones = 0

    while abs(f(x1)) > tol and iteraciones < max_iter:
        fx0, fx1 = f(x0), f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x2
        iteraciones += 1

    return x1, iteraciones, abs(f(x1))


# ========================================
#   EJECUCIÓN PRINCIPAL
# ========================================

a, b = 35, 38
punto_inicial = (a + b) / 2   # para Newton

# Bisección
xb, itb, errb = biseccion(a, b)

# Newton–Raphson
xn, itn, errn = newton(punto_inicial)

# Secante
xs, its, errs = secante(a, b)


# ================================
#   RESULTADOS
# ================================
print("\n====================================")
print("          COMPARACIÓN FINAL")
print("====================================")
print(f"Bisección:       raíz = {xb:.10f}, iter = {itb}, error = {errb:.2e}")
print(f"Newton-Raphson:  raíz = {xn:.10f}, iter = {itn}, error = {errn:.2e}")
print(f"Secante:         raíz = {xs:.10f}, iter = {its}, error = {errs:.2e}")

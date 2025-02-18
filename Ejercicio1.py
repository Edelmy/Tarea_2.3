#Chay Dzul Edelmy
import numpy as np
import matplotlib.pyplot as plt

# Función original
def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Ecuación

# Interpolación de Lagrange
def lagrange_interpolation(x, x_puntos, y_puntos):
    #x: EI valor donde se evalúa el polinomio interpolante.
    #x_puntos y y_puntos: Coordenadas X e y de los puntos conocidos.
    n = len(x_points)  # Número de puntos
    resultado = 0
    for i in range(n):
        termino = y_puntos[i]
        for j in range(n):
            if i != j:
                termino *= (x - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        resultado += termino
    return resultado

# Método de Bisección
def bisect(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("El intervalo no contiene una raíz")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tol or (b - a) / 2 < tol:
            return c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2  # Mejor estimación de la raíz

# Puntos de interpolación
x0, x1, x2 = 1.0, 2.0, 3.0
x_points = np.array([x0, x1, x2])
y_points = f(x_points)

# Polinomio interpolante
x_vals = np.linspace(x0, x2, 100)
y_interp = [lagrange_interpolation(x, x_points, y_points) for x in x_vals]

# Raíz del polinomio interpolante
#Usa el método de bisección para encontrar una raíz del polinomio interpolante en el intervalo [xo, x2].
root = bisect(lambda x: lagrange_interpolation(x, x_points, y_points), x0, x2)

# Errores
errores_absolutos = np.abs(y_interp - f(x_vals))
errores_relativos = errores_absolutos / np.where(np.abs(f(x_vals)) == 0, 1, np.abs(f(x_vals)))
errores_cuadraticos = errores_absolutos**2

# Tabla de errores
print(f"{'Iteración':<10}|{'x':<12}|{'Error absoluto':<18}|{'Error relativo':<18}|{'Error cuadrático'}")
print("-" * 80)
for i, (x_val, error_abs, error_rel, error_cuad) in enumerate(zip(x_vals, errores_absolutos, errores_relativos, errores_cuadraticos)):
    print(f"{i+1:<10}|{x_val:<12.6f}|{error_abs:<18.6e}|{error_rel:<18.6e}|{error_cuad:.6e}")

# Gráficas
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de errores
ax[0].plot(x_vals, errores_absolutos, label="Error Absoluto", color='blue')
ax[0].plot(x_vals, errores_relativos, label="Error Relativo", color='green')
ax[0].plot(x_vals, errores_cuadraticos, label="Error Cuadrático", color='red')
ax[0].set_xlabel("x")
ax[0].set_ylabel("Errores")
ax[0].legend()
ax[0].grid(True)

# Gráfica de la función y la interpolación
ax[1].plot(x_vals, f(x_vals), label="f(x)= x^3-6x^2+11x-6", linestyle='dashed', color='purple')
ax[1].plot(x_vals, y_interp, label="Interpolación", color='orange')
ax[1].axhline(0, color='black', linewidth=0.5, linestyle='--')  # Eje x
ax[1].axvline(root, color='red', linestyle='dotted', label=f"Raíz: {root:.4f}")  # Raíz
ax[1].scatter(x_points, y_points, color='black', label="Puntos de interpolación")
ax[1].set_xlabel("x")
ax[1].set_ylabel("f(x)")
ax[1].set_title("Interpolación y búsqueda de raíces")
ax[1].legend()
ax[1].grid(True)

plt.savefig("interpolacion_raices.png")  # Guarda la imagen
plt.show()

# Imprimir la raíz encontrada
print(f"La raíz aproximada usando interpolación es: {root:.4f}")
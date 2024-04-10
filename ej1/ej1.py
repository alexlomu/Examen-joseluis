import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros
a = 0
b = 5
c = 0
d = 10
N = 40
M = 400
v = 0.1

# Calculando los tamaños de paso
h = (b - a) / N
k = (d - c) / M

# Inicialización de la matriz w
w = np.zeros((N + 1, M + 1))

# Aplicando las condiciones de contorno
w[0, :] = 0  # u(0,t) = 0
w[N, :] = 0  # u(5,t) = 0

# Aplicando las condiciones iniciales
def f(x):
    return 10 * x * (5 - x)

def g(x):
    return 250 / 4 - 10 * x * (5 - x)

x_values = np.linspace(a, b, N + 1)
for i in range(N + 1):
    w[i, 0] = f(x_values[i])  # u(x,0) = f(x)
    w[i, 1] = w[i, 0] + k * g(x_values[i])  # du(x,0)/dt = g(x)

# Calculando los valores de w utilizando la ecuación diferencial
for j in range(1, M):
    for i in range(1, N):
        w[i, j + 1] = 2 * (1 - (v * k) ** 2 / (h ** 2)) * w[i, j] + ((v*k)/h)**2 * (w[i+1, j] + w[i - 1, j]) - w[i,j-1]

# Crear una malla tridimensional
X, T = np.meshgrid(np.linspace(a, b, N + 1), np.linspace(c, d, M + 1))

# Crear la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
surf = ax.plot_surface(X, T, w.T, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('w')
ax.set_title('Solución de la EDP en 3D')

# Agregar una barra de colores
fig.colorbar(surf, shrink=0.5, aspect=5)

# Mostrar el gráfico
plt.show()

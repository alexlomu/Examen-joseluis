import matplotlib.pyplot as plt
import numpy as np

# Parámetros del dominio y la malla
b = 5
d = 10
N = 40
M = 400
h = b / N
k = d / M
v=0.3

# Inicializar la matriz de solución
w = np.zeros((M + 1, N + 1))

def f(x):
    return 10*x*(b-x)

def g(x):
    return 0

# Condiciones de contorno
for i in range(1, N):
    w[0][i] = f(h * i)
    w[1][i] = (250/4)-f(h*i)

for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

# Método de diferencias finitas
for j in range(1, M):
    for i in range(1, N):
        w[j+1][i] = k**2*v**2*(w[j][i+1]-2*w[j][i]+w[j][i-1])/(h**2) - (- 2*w[j][i]+w[j-1][i])-k**2*v**2*w[j][i]

# Crear coordenadas para el gráfico 3D
X = np.linspace(0, b, N+1)
Y = np.linspace(0, d, M+1)
X, Y = np.meshgrid(X, Y)

# Crear gráfico 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la solución en 3D
ax.plot_surface(X, Y, w, cmap='viridis')

# Configuraciones adicionales del gráfico
ax.set_xlabel('Posición a lo largo de la cuerda (m)')
ax.set_ylabel('Tiempo (s)')
ax.set_zlabel('Desplazamiento de la cuerda (m)')

# Mostrar el gráfico
plt.show()
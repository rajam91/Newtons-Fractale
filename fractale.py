import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.image as mpimg

colors = ['b', 'r', 'g', 'y']

p = np.poly1d([1,3,-4,5,-2]) #création d'un polynome de degré 4
print(p)

#évaluation de p en un point 
r = p(1)
print(r)

#calcul des racines du polynome

racines = p.roots
print('Le polynome à ', len(racines), 'racines.')
print(racines)


ordre = p.o
print("Le polynome est d'ordre",ordre,".")

q = p.deriv() #dérivé dy polynome
print(q)

Tol = 1.e-4

def Newton(x0, f, df, tol): #methodes de Newton
    x = x0 - f(x0)/df(x0)
    while abs(x-x0) < tol:
        x0 = x
    return x


#appliaction de la méthode de newton
x0 = 1.5
x = Newton(x0,p, q, Tol)
print(x)


#afficher le graphe de la fonction polynomiale
X = np.linspace(-3, 3, 256) 
Y = [p(x) for x in X] 
plt.plot(X, Y)
plt.grid()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

def plot_newton_fractal(f, fprime, n=200, domain=(-1, 1, -1, 1)):
    xmin, xmax, ymin, ymax = domain
    x_vals = np.linspace(xmin, xmax, n)
    y_vals = np.linspace(ymin, ymax, n)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = X + 1j * Y

    for _ in range(30):  # Iteration de la méthode de newton
        Z = Z - f(Z) / fprime(Z)

    plt.imshow(np.angle(Z), extent=domain, cmap='twilight')
    plt.colorbar()
    plt.show()


X = np.linspace(-2, 2, 500)
colors = ['r', 'g', 'b']

plot_newton_fractal(p, q, n=500)

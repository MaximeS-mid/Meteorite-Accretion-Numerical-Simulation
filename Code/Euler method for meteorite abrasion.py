import matplotlib.pyplot as plt
import numpy as np
from math import *

##Initialisation des variables

pas = 0.001 #pas temporel de la simulation
theta_0 = 70 #degres
H = 20000 #m
rho_air = 1.2 #masse volumique de l'air supposée ici constante
X_impact = H/np.cos(radians(theta_0))
v0 = 19000.0 #vitesse initiale
m0 = 13000000.0 #masse initiale
Cd = 0.3 #coefficient de trainée
A = np.pi/2 * ((3/(4*np.pi))**(2/3)) #facteur de forme
rho_m = m0/ ((4/3)*np.pi*(8.5**3)) #masse volumique de la météorite
Delta_subH = 10**7

##Définition des fonctions utilisées

def X_i(H):
    return H/np.cos(radians(theta_0))

def v_lim(m, Cd):
    S = np.pi * ((3*m)/(4*np.pi*rho_m))**(2/3)
    return np.sqrt((2*m*9.8)/(rho_air*S*Cd))

def listes_abscisses_vitesses_masses(Cd, H):
    X = [0]
    v = [v0]
    m = [m0]
    i = 0
    while X[i] < X_i(H) and v[i] >= 10*v_lim(m[i], Cd):
        dX = v[i]*pas
        dv = - (Cd * A * rho_air *dX * v[i])/(m[i]**(1/3) * rho_m**(2/3))
        dm = - (Cd * A * rho_air * dX * (v[i])**(2) * m[i]**(2/3))/(2* Delta_subH * rho_m**(2/3))
        X.append(X[i]+dX)
        v.append(v[i]+dv)
        m.append(m[i]+dm)
        i += 1
    if v[i] <= 10*v_lim(m[i], Cd):
        print("Vitesse limite dépassée.")
    return X, v, m

##Calcul des masses et des vitesses finales

X1, v1, m1 = listes_abscisses_vitesses_masses(0.25, 20000)
X2, v2, m2 = listes_abscisses_vitesses_masses(0.3, 20000)
X3, v3, m3 = listes_abscisses_vitesses_masses(0.35, 20000)
X4, v4, m4 = listes_abscisses_vitesses_masses(0.4, 20000)
X5, v5, m5 = listes_abscisses_vitesses_masses(0.45, 20000)


##Graphiques des masses ou des vitesses
plt.plot(X1, m1, label = "Cd = 0.25")
plt.plot(X2, m2, label = "Cd = 0.30")
plt.plot(X3, m3, label = "Cd = 0.35")
plt.plot(X4, m4, label = "Cd = 0.40")
plt.plot(X5, m5, label = "Cd = 0.45")

plt.legend()
plt.ylabel("masse m (kg)")
plt.xlabel("position X (m)")
plt.grid()

plt.show()

##Graphique pour H variable

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(X1, v1)
axs[0, 0].legend(['H = 5km'])
axs[0, 1].plot(X2, v2, 'tab:orange')
axs[0,1].legend(['H = 10km'])
axs[1, 0].plot(X3, v3, 'tab:green')
axs[1, 0].legend(['H = 20km'])
axs[1, 1].plot(X5, v5, 'tab:red')
axs[1, 1].legend(['H = 30km'])


for ax in axs.flat:
    ax.set(xlabel='position X (m)', ylabel='vitesse (m/s)')

plt.show()


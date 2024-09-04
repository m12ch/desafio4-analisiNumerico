import sympy as sp
print('----------------------------------')
print('MARCELO ALVARO Chambi Chillo')
print('----------------------------------')
#VALORES
A=0.15
E=0.9
T=650
O=5.67*10**-8
#ERRORES
ea=0.01
ee=0.01
et=20
H=A*E*O*T**4
print('H = AeoT**4')
print('H: ', H)
a, e, o, t = sp.symbols('a e o t')
fH = a * e * o * t**4
dH_dA = sp.diff(fH, a)
print("La derivada de H respecto de A es:", dH_dA)
dha=E*O*T**4
print(dha)
dH_dE = sp.diff(fH, e)
print("La derivada de H respecto de E es:", dH_dE)
dhe=A*O*T**4
print(dhe)
dH_dT = sp.diff(fH, t)
print("La derivada de H respecto de T es:", dH_dT)
dht=4*A*E*O*T**3
print(dht)
eH=(dha*ea)+(dhe*ee)+(dht*et)
print('eH: ', eH)
print('H-eh: ', H-eH)
print('H+eh: ',H+eH)
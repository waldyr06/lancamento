# Alunos: Christian Mateus e Waldyr Felype
import math
import time

# Velocidade Inicial

m = float(input("Digite a massa da bala de canhão: "))
f = float(input("Digite uma força em Newtons: "))
         
v0 = (f * 1) / m

print (f"A velocidade Inicial é de: {v0}")

#------------------------------------------------------------------------------#

# Sobre o Ângulo

a = float(input(f"Digite um Ângulo: "))
g = float(input("Digite a Força da Gravidade: (Recomeda-se 10 ou 9,81) "))
angulo_rad = math.radians(a)

#------------------------------------------------------------------------------#

# Velocidade Inicial Horizontal

def velocidade_inicial_x(v0, angulo_rad):
    vx =  v0 * math.cos(angulo_rad)
    return vx

print (f"A velocidade Inicial Horizontal é de: {velocidade_inicial_x(v0, angulo_rad)}m/s")

# Velocidade Inicial Vertical

def velociodade_inicial_y(v0, angulo_rad):
    vy = v0 * math.sin(angulo_rad)
    return vy

print (f"A velocidade Inicial Vertical é de: {velociodade_inicial_y(v0, angulo_rad)}m/s")

# Velocidade Horizontal
def velocidade_x(v0, angulo_rad, f, m, g):
    if(tempo() >= tempo_voo(v0, g)): return 0
    v0x = velocidade_inicial_x(v0, angulo_rad)
    vx = v0x
    return v0x

def velocidade_y(v0, angulo_rad, f, m, g):
    if(tempo() >= tempo_voo(v0, g)): return 0
    v0y = velociodade_inicial_y(v0, angulo_rad)
    vy = v0y - (g * tempo())
    return vy

#------------------------------------------------------------------------------#

# Tempo Maximo 

def tempo_max():
    tmax = 2 * (velocidade_inicial_x(v0, angulo_rad) / g)
    return tmax

print (f"O Tempo máximo foi de: {tempo_max()} Segundos")

# Tempo Até o Limite Maximo de Altura

def tempo():
    t = (tempo_max() / 2)
    return t

def tempo_voo(v0, g):
    t_voo = (2 * v0) / g
    return t_voo

print (f"O tempo de voo foi de: {tempo_voo(v0, g)} Segundos")

# Alcance Maximo Horizontal

def alcance_horizontal(v0, angulo_rad, g):
    return velocidade_inicial_x(v0, angulo_rad) * tempo_max()

print (f"O alcance horizontal foi de: {alcance_horizontal(v0, angulo_rad, g):.1f}")

for t in range(15):
    i = t/10 
    t = tempo_voo(v0, g) * i
    vx = velocidade_x(v0, angulo_rad, f, m, g)
    vy = velocidade_y(v0, angulo_rad, f, m, g)
    print(f"A Velocidade no instante {t:.2f} foi:")
    print(f"\tHorizontal: {vx:.2f} m/s")
    print(f"\tVertical: {vy:.2f} m/s")
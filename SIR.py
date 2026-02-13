import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
N = 1000        # População total
beta = 1.96     # Taxa de transmissão
gamma = 1/7     # Taxa de recuperação
dias = 150      # Duração da simulação

dt = 0.01       # Passo de tempo (cálculo a cada fração de dia)
steps = int(dias / dt) # Número total de passos de cálculo
t_arr = np.linspace(0, dias, steps) # Lista de tempo para o gráfico

# Condições iniciais
S = np.zeros(steps)
I = np.zeros(steps)
R = np.zeros(steps)

S[0] = N - 1
I[0] = 1
R[0] = 0

# Simulação
for t in range(steps - 1):
    dS = -beta * S[t] * I[t] / N
    dI = beta * S[t] * I[t] / N - gamma * I[t]
    dR = gamma * I[t]

    # Atualiza os valores: Novo = Velho + (Taxa * dt)
    S[t+1] = S[t] + dS * dt
    I[t+1] = I[t] + dI * dt
    R[t+1] = R[t] + dR * dt

plt.figure(figsize=(10,6))
plt.plot(S, label='Suscetíveis', color='blue')
plt.plot(I, label='Infectados', color='red')
plt.plot(R, label='Recuperados', color='green')
plt.xlabel('Dias')
plt.ylabel('Número de indivíduos')
plt.title('Modelo SIR para Sarampo (Simulação)')
plt.legend()
plt.grid(True)
plt.show()

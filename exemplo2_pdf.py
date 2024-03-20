from scipy.optimize import linprog

# Coeficientes da função objetivo a ser minimizada
f = [-8, -4]

# Coeficientes das restrições lineares do tipo <=
A = [[4, 2], [1, 1]]

# Vetor das constantes das restrições lineares do tipo <=
b = [16, 6]

# Limites inferiores das variáveis de decisão
LB = [0, 0]

# Limites superiores das variáveis de decisão
UB = [float('inf'), float('inf')]  # Usando float('inf') para representar infinito em Python

# Chamando a função linprog para resolver o problema
res = linprog(f, A_ub=A, b_ub=b, bounds=(LB, UB))

# Extraindo os resultados
X = res.x
FVAL = res.fun
EXITFLAG = res.status

# Imprimindo os resultados
print("Solução ótima encontrada:")
print("Valor ótimo:", FVAL)
print("Variáveis de decisão ótimas:", X)
print("Código de saída:", EXITFLAG)

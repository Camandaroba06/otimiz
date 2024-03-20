from scipy.optimize import linprog

# Coeficientes da função objetivo a ser minimizada
c = [-4, -3]  # Note que estamos minimizando o oposto da função objetivo original

# Matriz dos coeficientes das restrições lineares do tipo <=
A = [[2, 1], [4, 3]]

# Vetor das constantes das restrições lineares do tipo <=
b = [20, 60]

# Limites das variáveis de decisão (x1 e x2 >= 0)
x0_bounds = (0, None)
x1_bounds = (0, None)

# Chamando a função linprog para resolver o problema
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])

# Verificando se a otimização foi bem sucedida
if res.success:
    print("Solução ótima encontrada:")
    print("Valor ótimo:", -res.fun)  # Note que estamos negando o valor ótimo para obter o valor da função objetivo original
    print("Variáveis de decisão ótimas:", res.x)
else:
    print("A otimização não foi bem sucedida. Mensagem de erro:", res.message)

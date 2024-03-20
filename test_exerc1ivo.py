from scipy.optimize import linprog


# https://realpython.com/linear-programming-python/

obj = [-5, -3]  # z = x + 2y .(-1) já q só ocorre minimização
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

lhs_ineq = [
    [1, 1.8],
]

rhs_ineq = [
    8,
]

# lhs_eq = [[-1, 5]]
# rhs_eq = [15]


bnd = [(0, 3), (0, 4)]  # Bounds of x  # Bounds of y

opt = linprog(
    c=obj,
    A_ub=lhs_ineq,
    b_ub=rhs_ineq,
    # A_eq=lhs_eq,
    # b_eq=rhs_eq,
    bounds=bnd,
    method="highs",
)
print(opt)
# opt
#      con: array([0.])
#      fun: -16.818181818181817
#  message: 'Optimization terminated successfully.'
#      nit: 3
#    slack: array([ 0.        , 18.18181818,  3.36363636])
#   status: 0
#  success: True
#        x: array([7.72727273, 4.54545455])

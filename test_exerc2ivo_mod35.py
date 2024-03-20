from scipy.optimize import linprog


# https://realpython.com/linear-programming-python/


# gt def va vt vv
obj = [150, 2000, 0, 0, 0]  # n precisa multiplicar por -1 já q só ocorre minimização
#      ─┬      ─┬
#       │       └┤ Coefficient for y
#       └────┤ Coefficient for x

# n tem ineq nesse problema
# lhs_ineq = [
#     [1, 1, 0, 0.95, 0],
# ]

# rhs_ineq = [
#     8,
# ]

lhs_eq = [[1, 1, 0, 0.95, 0], [0, 0, 1, 1, 1]]
rhs_eq = [68, 35 + 0]


bnd = [(0, 50), (0, 68), (0, 100), (0, 100), (0, 100)]  # Bounds of x  # Bounds of y

opt = linprog(
    c=obj,
    # A_ub=lhs_ineq,
    # b_ub=rhs_ineq,
    A_eq=lhs_eq,
    b_eq=rhs_eq,
    bounds=bnd,
    method="highs",
)
print(opt)
#         message: Optimization terminated successfully. (HiGHS Status 7: Optimal)
#         success: True
#          status: 0
#             fun: 5212.5
#               x: [ 3.475e+01  0.000e+00  0.000e+00  3.500e+01  0.000e+00]
#             nit: 1
#           lower:  residual: [ 3.475e+01  0.000e+00  0.000e+00  3.500e+01
#                               0.000e+00]
#                  marginals: [ 0.000e+00  1.850e+03  1.425e+02  0.000e+00
#                               1.425e+02]
#           upper:  residual: [ 1.525e+01  6.800e+01  1.000e+02  6.500e+01
#                               1.000e+02]
#                  marginals: [ 0.000e+00  0.000e+00  0.000e+00  0.000e+00
#                               0.000e+00]
#           eqlin:  residual: [ 0.000e+00  0.000e+00]
#                  marginals: [ 1.500e+02 -1.425e+02]
#         ineqlin:  residual: []
#                  marginals: []
#  mip_node_count: 0
#  mip_dual_bound: 0.0
#         mip_gap: 0.0

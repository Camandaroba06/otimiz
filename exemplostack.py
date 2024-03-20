from scipy import optimize

optimize.linprog(
    c = [-1, -2], 
    A_ub=[[1, 1]], 
    b_ub=[6],
    bounds=(1, 5),
    method='simplex'
)
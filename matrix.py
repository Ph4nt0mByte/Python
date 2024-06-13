import numpy as np

# Defining the augmented matrix
augmented_matrix = np.array([
    [1, 2, -2, 2, -1, 3, 0],
    [2, -1, 3, 1, -3, 2, 17],
    [1, 3, -2, 1, -2, 3, -5],
    [3, -2, 1, -1, 3, -2, -1],
    [-1, -2, 1, 2, -2, 3, 10],
    [1, -3, 1, 3, -2, 1, 11]
])

# Separate the coefficient matrix (left side of the equations) and the constants vector (right
# side of the equations)
coefficient_matrix = augmented_matrix[:, :-1]
constants_vector = augmented_matrix[:, -1]

# Solve the system of linear equations
solution = np.linalg.solve(coefficient_matrix, constants_vector)

# Round the solution values to the nearest whole number
rounded_solution = np.round(solution, decimals=0)

# Print the rounded solution
print("Rounded Solution:")
print("x1 =", rounded_solution[0])
print("x2 =", rounded_solution[1])
print("x3 =", rounded_solution[2])
print("x4 =", rounded_solution[3])
print("x5 =", rounded_solution[4])
print("x6 =", rounded_solution[5])
# Demonstrating the built-in-routines in NumPy module for solving Linear algebra

import numpy

# Determinant

A = [[1.1, 1.1], [1.1, 1.1]]
B = [[1, 2], [2, 1]]

print("Determinant of A :",numpy.linalg.det(A))

# Eigenvalues and eigenvectors

vals, vecs = numpy.linalg.eig(A)

print("Eigenvalue :", vals)
print("Eigenvector :", vecs)

# Multiplicative inverse of a matrix

print("Multiplicative inverse of A :", numpy.linalg.inv(B))


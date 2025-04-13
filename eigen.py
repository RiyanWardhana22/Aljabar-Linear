import numpy as np
from numpy.linalg import eig
matrix_data = [
    [1, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 3, -1, -1, 1],
    [1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 1, 1, 1, -1, -1, 3, 3, 3, 3],
    [1, 3, 1, 1, 1, 1, 1, -1, 3, 1, 1, 1, 1, -1, -1, -1, 2, -1, 1, 1],
    [1, 3, 1, 1, 3, 2, 3, 1, 3, -1, 1, 3, 1, 2, 3, 1, 1, -1, 2, 1],
    [2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 3, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 3, 2, 1, 1],
    [3, 1, 3, 1, 3, 3, 1, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 1, 1, 3],
    [3, -1, 1, 1, 3, 3, 3, 1, 1, 3, 1, 3, 1, -1, 3, 1, 1, -1, -1, -1],
    [1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, -1, -1, -1, 3, 1, 3, 3],
    [3, 3, 1, 1, 1, 1, 3, 1, 3, 1, 3, 3, 1, -1, -1, -1, -1, 1, 1, 1],
    [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 3, 1, -1, -1, -1, -1, 1, 1, 1],
    [3, -1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 1, 1, -1, 1, 1, 1, -1, -1, 1],
    [3, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, -1, -1, -1],
    [1, 1, 1, 3, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 3, 3, 3],
    [1, -1, -1, -1, 1, 1, 3, 3, -1, -1, -1, 1, 1, -1, 1, 3, 3, -1, -1, 1],
    [-1, -1, -1, -1, -1, -1, 3, 1, -1, -1, -1, -1, -1, -1, 3, 1, -1, -1, -1, -1],
    [3, 3, 1, 3, 3, 3, 3, 1, 3, -1, -1, 1, 1, 1, 3, 3, 1, 3, 1, 3],
    [-1, 3, 1, 2, 3, 3, 3, -1, 1, 1, 1, -1, -1, 3, -1, -1, 1, 1, 3, 3],
    [1, 3, 3, 3, 3, 3, 1, -1, 3, 3, 3, -1, -1, 3, -1, -1, 3, 3, 1, 3],
    [-1, 2, -1, -1, 3, -1, 3, -1, -1, -1, -1, -1, -1, 3, 3, -1, 3, 3, 3, 1]
]

matrix = np.array(matrix_data, dtype=float)
eigenvalues, eigenvectors = eig(matrix)

print("\nRingkasan Nilai Eigen dan Vektor Eigen:")
for i in range(len(eigenvalues)):
    print(f"\nNilai Eigen {i+1}: {eigenvalues[i]:.4f}")
    print("Bagian Real Vektor Eigen:")
    print(np.real(eigenvectors[:, i]))
    print("Bagian Imajiner Vektor Eigen:")
    print(np.imag(eigenvectors[:, i]))
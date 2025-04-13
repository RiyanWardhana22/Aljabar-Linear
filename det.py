import numpy as np
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
try:
    det = np.linalg.det(matrix)
    print(f"Determinan matriks: {det:.4f}")
except np.linalg.LinAlgError:
    print("Matriks singular, determinan = 0")

try:
    inv_matrix = np.linalg.inv(matrix)
    print("\nInvers matriks:")
    np.set_printoptions(precision=4, suppress=True)
    print(inv_matrix)
    identity = np.eye(20)
    verification = np.allclose(np.dot(matrix, inv_matrix), identity)
    print(f"\nVerifikasi (A × A⁻¹ ≈ I): {'Berhasil' if verification else 'Gagal'}")
    
except np.linalg.LinAlgError:
    print("\nMatriks singular, tidak memiliki invers (determinan = 0)")
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
def basisBaris(A):
    rref_A, pivots = A.copy(), []
    rows, cols = A.shape
    rank = 0
    for c in range(cols):
        pivot = -1
        for r in range(rank, rows):
            if abs(rref_A[r,c]) > 1e-10:
                pivot = r
                break
        if pivot == -1:
            continue
        if pivot != rank:
            rref_A[[rank, pivot]] = rref_A[[pivot, rank]]
        rref_A[rank] = rref_A[rank] / rref_A[rank,c]
        for r in range(rows):
            if r != rank and abs(rref_A[r,c]) > 1e-10:
                rref_A[r] -= rref_A[r,c] * rref_A[rank]
        pivots.append(c)
        rank += 1
        if rank == rows:
            break
    basis = rref_A[:rank]
    return basis

def colomBasis(A):
    return basisBaris(A.T).T

print("Basis Baris :")
row_space = basisBaris(matrix)
np.set_printoptions(precision=4, suppress=True)
print(row_space)
print(f"\nDimensi Ruang Baris: {len(row_space)}")

print("\nBasis Kolom :")
col_space = colomBasis(matrix)
print(col_space)
print(f"\nDimensi Ruang Kolom: {len(col_space.T)}")

print("\nVerifikasi:")
print(f"Rank dari matriks: {np.linalg.matrix_rank(matrix)}")
print(f"Dimensi Ruang baris: {len(row_space)}")
print(f"Dimensi Ruang kolom: {len(col_space.T)}")

def is_linearly_independent(vectors):
    if np.linalg.matrix_rank(vectors) == len(vectors):
        return True
    return False

print("\nAnalisis Linear Independen:")
print("Basis baris bebas linear?", is_linearly_independent(row_space))
print("Basis kolom bebas linear?", is_linearly_independent(col_space.T))
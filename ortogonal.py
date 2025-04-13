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
def ortogonal(v1, v2, tolerance=1e-6):
    return abs(np.dot(v1, v2)) < tolerance

def ortonormal(v, tolerance=1e-6):
    return abs(np.linalg.norm(v) - 1) < tolerance

print("Analisis Ortogonalitas:")
psngan_ortogonal = []
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        if ortogonal(matrix[i], matrix[j]):
            psngan_ortogonal.append((i, j))
            print(f"Vektor {i} dan vektor {j} ortogonal")
if not psngan_ortogonal:
    print("Tidak ada pasangan vektor yang ortogonal")
else:
    print(f"Total pasangan ortogonal: {len(psngan_ortogonal)}")

print("\nAnalisis Ortonormalitas:")
vektor_ortonormal = []
for i, v in enumerate(matrix):
    if ortonormal(v):
        vektor_ortonormal.append(i)
        print(f"Vektor {i} ortonormal (panjang = 1)")
if not vektor_ortonormal:
    print("Tidak ada vektor yang ortonormal")
else:
    print(f"Total vektor ortonormal: {len(vektor_ortonormal)}")

print("\nMatriks setelah normalisasi (ortonormalisasi):")
normalized_matrix = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)
np.set_printoptions(precision=4, suppress=True)
print(normalized_matrix)

print("\nVerifikasi matriks ortonormal:")
dot_product = np.dot(normalized_matrix, normalized_matrix.T)
print("A × Aᵀ (harus mendekati matriks identitas):")
print(dot_product)

ortonormal_matrix = np.allclose(dot_product, np.eye(len(matrix)), atol=1e-6)
print(f"\nApakah matriks ternormalisasi ortonormal? {'Ya' if ortonormal_matrix else 'Tidak'}")
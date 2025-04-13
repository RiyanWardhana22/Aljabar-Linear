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
vector1 = matrix[0]  
vector2 = matrix[1] 

print("Vektor 1 (Baris pertama matriks):")
print(vector1)
print("\nVektor 2 (Baris kedua matriks):")
print(vector2)

def vector_length(v):
    return np.sqrt(np.sum(v**2))
length1 = vector_length(vector1)
length2 = vector_length(vector2)

print("\nPanjang Vektor 1:", round(length1, 4))
print("Panjang Vektor 2:", round(length2, 4))

dot_product = np.dot(vector1, vector2)
print("\nPerkalian dot vektor1 dan vektor2:", dot_product)

cos_theta = dot_product / (length1 * length2)
angle = np.arccos(cos_theta) * 180 / np.pi  
print("Sudut antara vektor (derajat):", round(angle, 2))

print("\nMatriks hasil perkalian dot (dot product matrix):")
dot_matrix = np.dot(matrix, matrix.T)  
np.set_printoptions(precision=2, suppress=True)
print(dot_matrix)

normalized_v1 = vector1 / length1
normalized_v2 = vector2 / length2
print("\nVektor 1 ternormalisasi:")
print(normalized_v1)
print("\nVektor 2 ternormalisasi:")
print(normalized_v2)
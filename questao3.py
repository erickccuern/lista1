mat1 = [[8, 3, 4, 0],[0, 2, -1, 8],[9, -1, 20, 6],[5, 8, 8, 8]]
mat2 = [[-2, -0, 25, 1],[5, 30, 40, 23],[-10, 0, -9, 1],[5, 55, 24, 3]]
print('Matriz 1: ',mat1)
print('Matriz 2: ',mat2)
result = []
for i in range(4):
    result.append([])
    for j in range(4):
        result[i].append(mat1[i][j]+mat2[i][j])

print('Soma das Matrizes: ',result)

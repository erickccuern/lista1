mat1 = [[5, 4, 3, 1],[0, 2, 3, 5],[1, -1, 3, 0],[2, 8, 6, 1]]
mat2 = [[0, -2, 40, 1],[5, -3, 15, 2],[-1, 0, 9, 4],[0, 8, 4, 30]]

result = []
for i in range(4):
    result.append([])
    for j in range(4):
        result[i].append(mat1[i][j]+mat2[i][j])

print(result)

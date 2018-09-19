matrix = [[1,2,3],[4,3,5],[3,8,5]]
new_mat = []
for row in matrix:
    for value in row:
        if value%2 ==0:
            new_mat.append(value)

print(new_mat)

new_mat2 = [[value for value in row] for row in matrix]

print(new_mat2)

new_mat3 = [value for row in matrix for value in row]
print(new_mat3)
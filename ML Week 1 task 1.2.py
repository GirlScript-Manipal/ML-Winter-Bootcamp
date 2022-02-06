mat1 = [[6,2,6],[9,6,9],[7,9,6],[1,2,9]]
print("Original matrix:\n")
for row in mat1 :
    print(row)
mat11 = [[mat1[j][i] for j in range(len(mat1))] for i in range(len(mat1[0]))]
print("\n\n")
print("Transpose Matrix:\n")
for row in mat11:
    print(row)
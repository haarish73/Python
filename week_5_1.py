# Input number of rows and columns
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))


a = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter the value: ")))
    a.append(row)
b = []
print("Enter the elements of the second matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter the value: ")))
    b.append(row)
result = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        result[i][j] = a[i][j] + b[i][j]
for i in range(r):
    for j in range(c):
        print(result[i][j], end=" ")
    print()

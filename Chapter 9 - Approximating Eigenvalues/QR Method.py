

# INPUT
n = int(input("Enter n: "))
matrix = [[0] * n] * n
for i in range(0, n):  # ROWS
	print("Enter values of row {}".format(i+1))
	for j in range(0, n):  # COLUMNS
		matrix[i][j] = input("Column {}: ".format(j+1))

# OUTPUT

for i in range(0, n):
	line = ""
	line += "["
	for j in range(0, n):
		line += " {}".format(matrix[i][j])
	line += " ]"
	print(line)

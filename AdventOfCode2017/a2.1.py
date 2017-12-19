with open("a2input.txt", "r") as file:
    lines = file.read().split("\n")
table = []
checkSum = 0
for line in lines:
    row = line.split("\t")
    min = 9999999999
    max = -9999999999
    for cell in row:
        if int(cell) > max:
            max = int(cell)
        if int(cell) < min:
            min = int(cell)
    checkSum += max-min
print(checkSum)

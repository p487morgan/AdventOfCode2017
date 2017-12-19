with open("a2input.txt", "r") as file:
    lines = file.read().split("\n")
table = []
checkSum = 0
for line in lines:
    row = line.split("\t")
    for cell in range(len(row)):
        for c in range(len(row)):
            if c != cell:
                if (int(row[cell]) % int(row[c])) == 0:
                    checkSum += int(int(row[cell]) / int(row[c]))
print(checkSum)

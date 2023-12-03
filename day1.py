inputRaw = open("input.txt", encoding="utf8")

input = []
result = []

for line in inputRaw:
    input.append(line.rstrip())

for line in input:
    for char in line:
        if char.isnumeric() == True:
            result.append(char)
            break
    for char in line[::-1]:
        if char.isnumeric() == True:
            result.append(char)
            break

sum = []

for x in range(int(len(result)/2)):
    sum.append(result[0] + result[1])
    for i in range(2):
        result.pop(0)

total = 0

for x in sum:
    total += int(x)

print
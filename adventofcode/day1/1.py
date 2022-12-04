name = "inputt.txt"
summer = []
temp = 0

with open(name) as file:
        for line in file:
            if line != "\n":
                temp = temp + int(line)
            else:
                summer.append(temp)
                temp = 0

summer.sort(reverse = True)

final = 0
for i in range(0,3):
    final = final + summer[i]

print(final)
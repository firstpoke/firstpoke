sum = 0

with open("input3.txt") as file:
        for line in file:
            length = int(len(line.strip()))
            half = int((length)/2)

            p1 = line[0:half]
            p2 = line[half:length]

            similar = '!'
            for x in range(0,len(p1)):
              for y in range(0,len(p2)):
                if p1[x] == p2[y]:
                  similar = p2[y]


            if ord(similar) >= 97:
              sum = sum + ord(similar) - 96
            else:
              sum = sum + ord(similar) - 38


print(sum)
name = "input2.txt"

outcome = 0
final = 0
value = 0

with open(name) as file:
        for line in file:

            first = line[0]
            second = line[2]

            if first == 'A' and second == 'X':
                second = 'C'
                value = 3
            elif first == 'A' and second == 'Y':
                second = 'A'
                value = 1
            elif first == 'A' and second == 'Z':
                second = 'B'
                value = 2
            elif first == 'B' and second == 'X':
                second = 'A'
                value = 1
            elif first == 'B' and second == 'Y':
                second = 'B'
                value = 2
            elif first == 'B' and second == 'Z':
                second = 'C'
                value = 3
            elif first == 'C' and second == 'X':
                second = 'B'
                value = 2
            elif first == 'C' and second == 'Y':
                second = 'C'
                value = 3
            elif first == 'C' and second == 'Z':
                second = 'A'
                value = 1

            ## if they're the same, 3; if it's a win, 6; otherwise, nothing bc it's a loss worth 0
            if first == second:
                outcome = 3
            elif first == 'A' and second == 'B':
                outcome = 6
            elif first == 'B' and second == 'C':
                outcome = 6
            elif first == 'C' and second == 'A':
                outcome = 6
            else:
                outcome = 0

            final = final + outcome + value

print(final)

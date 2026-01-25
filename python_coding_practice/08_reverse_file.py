
lines = []
with open("abc.txt", "r") as f:
    for line in f:
        if line[-1] != '\n':
            line += '\n'
        lines.append(line)
    print(lines)

with open("abc.txt", "w") as f:
    for index in range(len(lines) - 1, -1, -1):
        f.write(lines[index])

scores = []
with open("sample.txt", "r") as f:
    for line in f:
        scores.append(int(line))

total = 0
average = 0

for score in scores:
    total += score

average = total / len(scores)

with open("result.txt", "w") as f:
    f.write(str(average))


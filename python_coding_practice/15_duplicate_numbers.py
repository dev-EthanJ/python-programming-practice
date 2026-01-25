def DuplicateNumbers(data):
    count_list = []
    for i in range(10):
        count_list.append(0)

    for number in data:
        count_list[int(number)] += 1

    flag = True
    for count in count_list:
        if count != 1:
            flag = False

    return flag

print(DuplicateNumbers("0123456789"))
print(DuplicateNumbers("01234"))
print(DuplicateNumbers("01234567890"))
print(DuplicateNumbers("6789012345"))
print(DuplicateNumbers("01234567779"))
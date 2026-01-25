def CompressStr(data):
    before_char = ""
    count = 1
    new_str = ""
    data = data + "\n"
    for i in range(0, len(data)):
        if i == 0: 
            before_char = data[0]
            continue
        if before_char == data[i]:
            count += 1    
        else: # before_char != data[i]
            new_str = new_str + before_char + str(count)
            count = 1
        before_char = data[i]

    return new_str

print(CompressStr("aaabbcccccca"))
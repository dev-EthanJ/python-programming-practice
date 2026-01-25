def DashInsert(data):
    flag_data = []
    for char in data:
        if int(char) % 2 == 0:
            flag_data.append(0)
        else:
            flag_data.append(1)

    new_data = ""
    for i in range(0, len(flag_data)):
        if i == 0: 
            new_data = str(data[0])
            continue
        if flag_data[i] == flag_data[i - 1]:
            if flag_data[i] == 0:
                new_data = new_data + "*" + str(data[i])
            if flag_data[i] == 1:
                new_data = new_data + "-" + str(data[i])
        else:
            new_data += data[i]

    return str(new_data)

if __name__ == "__main__":
    print(DashInsert("4546793"))
    # 454*67-9-3
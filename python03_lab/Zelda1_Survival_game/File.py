

def read_data(filename):
    f = open(filename, "r")
    data = []
    for line in f :
        txt = line.rstrip()
        data.append(txt.rsplit(","))
    for i in range(len(data)) :
        data[i][0] = str(data[i][0])
        data[i][1] = int(data[i][1])
    return data

def write_data(filename, data):
    f = open(filename, "w")
    for line in range(len(data)) :
        f.write(f"{data[line][0]},{data[line][1]}\n")
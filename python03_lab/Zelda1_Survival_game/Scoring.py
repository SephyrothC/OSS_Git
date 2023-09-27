import File

def check_data(data, score) :
    data_score = []
    for i in range(len(data)):
        data_score.append(data[i][1])
    for i in range(len(data_score)):
        if data_score[i] < round(score) :
            data_score.append(round(score))
            data_score = sorted(data_score, reverse=True)
            data_score.pop()
            break
    for i in range(len(data)):
        data[i][1] = data_score[i]
    return data

def score_update(filename, score):
    data = File.read_data(filename)
    data = check_data(data, score)
    File.write_data(filename, data)


def read_data(filename):
    # TODO) Read `filename` as a list of integer numbers
    f = open(filename, "r")
    data = []
    next(f)
    for line in f :
        txt = line.rstrip()
        data.append(txt.rsplit(","))
    for i in range(len(data)) :
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])
    return data

def calc_weighted_average(data_2d, weight):
    # TODO) Calculate the weighted averages of each row of `data_2d`

    average = []
    x1 = 0.0
    for row in range(len(data_2d)) :
        for i in range(len(data_2d[row])) :
            x1 += (float)(data_2d[row][i]) * weight[i]
        average.append(x1)
        x1 = 0

          
    return average


def analyze_data(data_1d):
    # TODO) Derive summary of the given `data_1d`
    # Note) Please don't use NumPy and other libraries. Do it yourself.
    
    mean = 0.0
    for i in range(len(data_1d)) :
        mean += int(data_1d[i])
    mean /= len(data_1d)

    var = 0.0
    for i in range(len(data_1d)) :
        note = float(data_1d[i]) 
        var += (note-mean)*(note-mean)
    var /= len(data_1d)

    median = 0
    data_1d = sorted(data_1d)
    data_len = len(data_1d)
    if (len(data_1d)%2 == 0) :
        n = (data_len - 1) /2
        m = (data_len +1 ) /2
        median = (data_1d[n] + data_1d[m])/2
    else:
        n = int((data_len-1)/2)
        median = data_1d[n]

    return mean, var, median, (min((data_1d))), (max((data_1d)))

if __name__ == '__main__':
    # data = read_data('python02_lab\data\class_score_en.csv')
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        average = calc_weighted_average(data, [40/125, 60/100])

        # Write the analysis report as a markdown file
        # with open('python02_lab\class_score_analysis.md', 'w') as report:
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Total |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')
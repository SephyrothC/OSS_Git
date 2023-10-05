import matplotlib.pyplot as plt


def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'):  # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data


if __name__ == '__main__':
    # Load score data
    class_kr = read_data('math01_lab/data/class_score_kr.csv')
    class_en = read_data('math01_lab/data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    plt.scatter(midterm_kr, final_kr, label="Korean")
    plt.scatter(midterm_en, final_en, label="English")
    plt.title('Plot midterm/final scores as points')
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.xlabel('Midterm')
    plt.ylabel('Final')
    plt.legend()
    plt.grid()
    plt.show()

    # TODO) Plot total scores as a histogram

    plt.hist(total_kr, bins=20, range=(0, 100),
             histtype='barstacked', color='red', alpha=1, label="Korean")
    plt.hist(total_en, bins=20, range=(0, 100),
             histtype='barstacked', color='lightblue', alpha=0.8, label="English")
    plt.title('Plot total scores as a histogram')
    plt.xlabel('Total Score')
    plt.ylabel('The number of students')
    plt.legend()
    plt.xlim([0, 100])
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    midterm_range = np.array([0, 125])
    final_range = np.array([0, 100])

    # MY Load score data
    class_kr = np.loadtxt('math02_lab/data/class_score_kr.csv', delimiter=',')
    class_en = np.loadtxt('math02_lab/data/class_score_en.csv', delimiter=',')
    data = np.vstack((class_kr, class_en))

    # # Load score data
    # class_kr = np.loadtxt('data/class_score_kr.csv', delimiter=',')
    # class_en = np.loadtxt('data/class_score_en.csv', delimiter=',')
    # data = np.vstack((class_kr, class_en))

    # Estimate a line, final = slope * midterm + y_intercept

    # TODO) Please find the best [slope, y_intercept] from 'data'

    # I used the Ordinary least squares
    midterm_values = data[:, 0]
    final_values = data[:, 1]
    n = len(midterm_values)
    midterm_mean = np.mean(midterm_values)
    final_mean = np.mean(final_values)

    # Calculates the sum of cross products and the sum of squares of midterm values
    S_xy = np.sum(np.multiply(final_values, midterm_values)) - \
        n*midterm_mean*final_mean
    S_xx = np.sum(np.multiply(midterm_values, midterm_values)) - \
        n*midterm_mean*midterm_mean

    # Calculation of slope and y-intercept
    slope = S_xy / S_xx
    y_intercept = final_mean - (slope * midterm_mean)

    # create the line
    line = [slope, y_intercept]

    # Predict scores
    def final(midterm): return line[0] * midterm + line[1]
    while True:
        try:
            given = input(
                'Q) Please input your midterm score (Enter or -1: exit)? ')
            if given == '' or float(given) < 0:
                break
            print(
                f'A) Your final score is expected to {final(float(given)):.3f}.')
        except Exception as ex:
            print(f'Cannot answer the question. (message: {ex})')
            break

    # Plot scores and the estimated line
    plt.figure()
    plt.plot(data[:, 0], data[:, 1], 'r.', label='The given data')
    plt.plot(midterm_range, final(midterm_range), 'b-', label='Prediction')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.xlim(midterm_range)
    plt.ylim(final_range)
    plt.grid()
    plt.legend()
    plt.show()

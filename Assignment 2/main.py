import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy import signal

array = []
min_max = []
h1 = np.array([0.2, 0.4, 0.6, 0.8, 1])
h2 = np.array([0.8, 0.6, 0.4, 0.2, 0])


def read_from_file(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                temp = [datetime.datetime.strptime(row[0], "%m/%d/%Y").date(), float(row[1]), float(row[2]),
                        float(row[3]), float(row[4]), float(row[5]), int(row[6])]
                array.append(temp)
                line_count += 1


def standardized_data():
    arr = array[-400:]
    dates = []
    close = []
    std_data = []
    for row in arr:
        dates.append(row[0])
        close.append(row[4])
    window_size = 5
    i = 0
    while i < len(close) - window_size + 1:
        this_window = close[i: i + window_size]
        avg = sum(this_window) / window_size
        std_dev = np.std(this_window)
        j = i
        while j < i + window_size:
            std_data.append((close[j] - avg) / std_dev)
            j += 1
        i += window_size

    fig, ax = plt.subplots()
    ax.plot(dates, std_data)
    ax.set_ylabel('Standardized Values')
    ax.set_xlabel('Date')
    ax.set_title('Standardization of Closing Prices')
    fig.autofmt_xdate()
    plt.show()


def min_max_norm():
    arr = array[-400:]
    dates = []
    close = []
    for row in arr:
        dates.append(row[0])
        close.append(row[4])

    window_size = 5
    i = 0
    while i < len(close) - window_size + 1:
        this_window = close[i: i + window_size]
        j = i
        while j < i + window_size:
            min_max.append((close[j] - min(this_window)) / (max(this_window) - min(this_window)))
            j += 1
        i += window_size

    fig, ax = plt.subplots()
    ax.plot(dates, min_max)
    ax.set_ylabel('Normalized Values')
    ax.set_xlabel('Date')
    ax.set_title('Min-Max Normalization of Closing Prices')
    fig.autofmt_xdate()
    plt.show()


def max_conv():
    arr = array[-400:]
    dates = []
    close = [0, 0, 0, 0]
    max_conv1 = []
    max_conv2 = []
    frame = []
    for row in arr:
        dates.append(row[0])
        close.append(row[4])

    window_size = 5
    i = 0
    while i < len(min_max):
        this_window = min_max[i: i + window_size]
        max_conv1f = max(signal.convolve(h1, this_window))
        max_conv1.append(max_conv1f)
        max_conv2f = max(signal.convolve(h2, this_window))
        max_conv2.append(max_conv2f)
        i += 5
        frame.append(i//5)

    fig, ax = plt.subplots()
    ax.plot(frame, max_conv1)
    ax.set_ylabel('Normalized Values')
    ax.set_xlabel('Frame number')
    ax.set_title('Max Convolution with h = [0.2, 0.4, 0.6, 0.8, 1]')
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(frame, max_conv2)
    ax.set_ylabel('Normalized Values')
    ax.set_xlabel('Frame number')
    ax.set_title('Max Convolution with h = [0.8, 0.6, 0.4, 0.2, 0]')
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: main.py GOOG.csv")
        sys.exit(1)
    else:
        read_from_file(sys.argv[1])
        standardized_data()
        min_max_norm()
        max_conv()

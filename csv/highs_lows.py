import csv
from matplotlib import pyplot as plt
from  datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        low

    # print(highs)
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')

    plt.title("dilay high temperature, 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("temperature(F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()

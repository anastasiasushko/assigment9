import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task1():
    frame = pd.read_csv("titles.csv")
    # print(frame.head())
    show = frame[frame["type"] == "SHOW"]["tmdb_score"].dropna()
    movie = frame[frame["type"] == "MOVIE"]["tmdb_score"].dropna()
    figure = plt.figure(figsize=(9, 4))

    plt.subplot(1, 3, 1)
    plt.hist(show, np.arange(0, 10.2, 0.2))
    plt.axvline(show.mean(), color='r', linestyle='--', linewidth=1)

    plt.subplot(1, 3, 2)
    plt.hist(movie, np.arange(0, 10.2, 0.2))
    plt.axvline(movie.mean(), color='r', linestyle='--', linewidth=1 )

    plt.xlabel('Score')
    plt.ylabel('Num titles')
    plt.show()


if __name__ == '__task1__':
    task1()



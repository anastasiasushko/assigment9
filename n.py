import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def task1():
    frame = pd.read_csv("titles.csv")
    # print(frame.head())
    show = frame[frame["type"] == "SHOW"]["tmdb_score"].dropna()
    movie = frame[frame["type"] == "MOVIE"]["tmdb_score"].dropna()
    plt.figure(figsize=(9, 4))

    plt.subplot(1, 3, 1)
    plt.hist(show, np.arange(0, 10.2, 0.2))
    plt.axvline(show.mean(), color='r', linestyle='--', linewidth=1)

    plt.subplot(1, 3, 2)
    plt.hist(movie, np.arange(0, 10.2, 0.2))
    plt.axvline(movie.mean(), color='r', linestyle='--', linewidth=1 )

    plt.xlabel('Score')
    plt.ylabel('Num titles')
    plt.show()


def task2():
    frame = pd.read_csv("titles.csv")
    age = frame[frame['type'] == 'SHOW']['age_certification'].dropna()

    categories, age = np.unique(age, return_counts=True)
    plt.figure(figsize=(10, 10))
    plt.pie(age, labels=categories)
    plt.show()


# def task3():
#     frame = pd.read_csv("titles.csv")
#     sort_year = frame[frame["release_year"] >= 2000].dropna()
#     sort_score = frame[sort_year["imdb_score"] > 8.0].dropna()
#
#     join = sort_score.groupby()
#
#     plt.plot()
#     plt.figure(figsize=(9, 4))
#     plt.xlabel('year')
#     plt.ylabel('percent')
#     plt.show()





def task4():
    frame = pd.read_csv("titles.csv") #file with films
    frame1 = pd.read_csv("credits.csv") #file with actors

    top_films = frame.sort_values(by="tmdb_score", ascending=False).head(1000)
    actors = frame1[frame1['role'] == 'ACTOR'].dropna()
#   join = top_films.join(actors, on='id', how='inner')
    join = pd.merge(top_films, actors, how='inner', on='id')
    top_actors = join.groupby(by='name')['title'].count().sort_values(ascending=False).head(10)

    # plt.figure(figsize=(9, 4))
    # plt.scatter(top_actors, top_films)
    # plt.show()
    print(top_actors)

# def task5():
#     frame = pd.read_csv("titles.csv") #file with films
#     top_films = frame.sort_values(by="tmdb_score", ascending=False).head(1000)
#     genres = []
#     for film in top_films:
#         films = film.replace("[", "").replace("'", "").replace("]", "").replace(",", "").split(" ")
#         for genre in films:
#             if genre == "":
#                 continue
#             else:
#                 genres.append(genre)


    # plt.figure(figsize=(9, 4))
    # plt.bar(genres,)
    # plt.show()
def task5():
    frame = pd.read_csv("titles.csv")
    top_films = frame.sort_values(by="tmdb_score", ascending=False).head(1000)
    top_films['genres'] = top_films['genres'].str.split(',')
    top_films = top_films.explode('genres')

    counter_for_ganres = top_films['genres'].str.strip('[]').value_counts()
    counter_for_ganres.index = counter_for_ganres.index.str.strip("'")
    counter_for_ganres.index = counter_for_ganres.index.str.strip(" '")
    counter_for_ganres = counter_for_ganres.groupby(counter_for_ganres.index).sum()
    counter_for_ganres = counter_for_ganres.drop_duplicates(keep='first')

    counter_for_ganres.plot(kind = 'bar')
    # print(counter_for_ganres)

    plt.figure(figsize=(9, 4))
    plt.ylabel("Genres")
    plt.xlabel("Genres")
    plt.title("Genres")
    plt.show()


task1()
task2()
task4()
task5()


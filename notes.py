# print(frame.shape) #count
# # type = frame.groupby(["type","id"])
# # print(type.count()) #порахувало фільми і серіали
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# frame = pd.read_csv("titles.csv") #file with films
# frame1 = pd.read_csv("credits.csv") #file with actors
#
# top_films = frame.sort_values(by="tmdb_score", ascending=False).head(1000)
# actors = frame1[frame1['role'] == 'ACTOR'].dropna()
# #   join = top_films.join(actors, on='id', how='inner')
# join = pd.merge(top_films, actors, how='inner', on='id')
# top_actors = join.groupby(by='name')['title'].count().sort_values(ascending=False).head(10)
#
# print(top_actors, join)
    # plt.figure(figsize=(9, 4))
    # plt.scatter(top_actors, top_films)
    # plt.show()
# frame = pd.read_csv("titles.csv") #file with films
# top_films = frame.sort_values(by="tmdb_score", ascending=False).head(1000)
# print(top_films)
# genres = []
# for film in top_films:
#     films = film.replace("[", "").replace("'", "").replace("]", "").replace(",", "").split(" ")
#     for genre in films:
#         if genre == "":
#             continue
#         else:
#             genres.append(genre)
# g = pd.Index(genres).value_counts()

frame = pd.read_csv("titles.csv")
sorted = frame[frame["release_year"] >= 2000].dropna() and [frame["imdb_score"] > 8.0].dropna()
join = sorted.groupby('release_year')['release_year'].count()
# sort_score = frame[frame["imdb_score"] > 8.0].dropna()

# join = sort_score.groupby(['release_year'])["imdb_score"].count()
# join1 = join.reset_index()
# sorted_join1 = join1.count()
print(join)

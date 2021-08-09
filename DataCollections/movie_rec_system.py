dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk","Baahubali",
                "Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user_1 = {"Thor","KGF","The mask","Gravity","Hulk","Baahubali","It","Batman"}

scores = {}

for key in dataset:
    movies = dataset[key]
    movies = set(movies)
    numer = len(user_1.intersection(movies))
    denom = len(user_1.union(movies))
    score = numer / denom
    scores[key] = round(score,2)

print(scores)

max_value = max(scores.values())
for key in scores:
    if scores[key] == max_value:
        category = key
        break

# print(category)
rec_movies = set(dataset[category]) - user_1
print(rec_movies)
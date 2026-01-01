#enter  movies, average rating, movies above the rating and movies below the rating

movies =[]
s_rate =0

movie_input =input("Enter movies and ratings seperated by space (e.g. Movie1-8.5 Movie2-7.0): ")
print(movie_input)
entries=movie_input.split()
print("The movies and ratings you entered:", entries)

for item in entries:
    name, rating = item.split("-")
    rating = float(rating)
    s_rate += rating
    movies.append((name, rating))

print("Entered movies and ratings:",movies)

average_rating = s_rate/len(movies)

h_rate = movies[0]
for movie in movies[1:]:
    if movie[1] > h_rate[1]: 
        h_rate = movie


above_avg = []
below_avg = []

for name, rating in movies:
    if rating > average_rating:
        above_avg.append(name)
    elif rating < average_rating:
        below_avg.append(name)


print(f"Average rating: {average_rating}")
print(f"Highest rated movie: {h_rate[0]}")
print(f"Movies above average: {above_avg}")
print(f"Movies below average: {below_avg}")
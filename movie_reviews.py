# Workshop 4 Practice Problems 2-4
movies = {'Interstellar': 4,
          'Black Widow': 4}
ask_again = True

while ask_again:
  print('Enter a movie:')
  movie = input()
  # 1 is the fallback value if the movie key is NOT already in the dictionary
  duplicate = movies.get(movie, 1)
   # if the movie is not in the dictionary, add it
  if duplicate == 1:
    print('Enter your rating of the movie:')
    rating = input()
    movies[movie] = int(rating)
  else:
    print('Duplicate Movie.')
  
  print('Do you want to input another movie? [Y/N]')
  yes_or_no = input()
  if yes_or_no == 'N':
    ask_again = False

for movie_name, rating in movies.items():
  print('On a scale from 1 to 5, I rate ' + movie_name + ' a ' + str(rating) + '.')
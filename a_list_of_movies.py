keep_on = 'y'
movie_list = []
while keep_on == 'y':
    movie_to_add = input('Enter the name of movie ')

    # avoid duplicating the movie
    if movie_to_add.lower() in [movie[0].lower() for movie in movie_list]:
        print('{0} already existed in the list'.format(movie_to_add))
    else:
        rate = input('Enter a rating of 5 for this movie: ')
        # add the movie to the movie list ans the rate to the movie
        movie_list.append((movie_to_add, rate))
   
    keep_on = input('do you want to add another movie? y/n ')
    print('')

movie_list.sort()
print(movie_list)

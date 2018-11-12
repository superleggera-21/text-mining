
# print(imdb.get_title('tt0111161'))
#
# dicts = imdb.search_for_title("Your Name.")

# movie = imdb.get_title('tt5311514')
#
# reviews = imdb.get_title_user_reviews('tt5311514')
# userscore = imdb.get_title_ratings('tt5311514')
# metareviews = imdb.get_title_metacritic_reviews('tt5311514')
#
# print(reviews)
# print(userscore)
# print(metareviews)
#
#
# print(len(reviews))
# print(len(userscore))
# print(len(metareviews))

# The actual code begins here
# This file is intended to load and dump everything offline, preventing user getting banned from IMDB
# The code is written to see what are some key words of the reviews from critics and normal viewers
# And to see what are some of the differences
# The second task is to asses the people's emotion vs. actual score given

from imdbpie import Imdb
import string
imdb = Imdb()
import pickle

print("Start pulling data from IMDB server. Please wait.")
# import top-rated 250 movies into a list called movies
movies = []

fin = open('it2_titles.csv', 'r')
for line in fin:
    movies.append(line)

# print(movies)

# translate these movies titles to imdb code (ttxxxxxx) for future processing
movienumbers = []

for eachmovies in movies:
    searchresult = imdb.search_for_title(eachmovies)
    movieid = searchresult[0]['imdb_id']
    movienumbers.append(movieid)
    # need to find the value of the 3rd item in each of the dictionaries in the list

print(movienumbers)
# Save data to a file (will be part of your data fetching script)

with open('movienumbers.pickle','wb') as f:
    pickle.dump(movienumbers,f)

print('movienumbers has been saved.')

# create a dictionary of scores, a list or dictionary that
# includes viewers' review and one for metacritic (the professionals)
ratings = {}

for title in movienumbers:
    rat = imdb.get_title_ratings(title)
    # skip movies that don't have ratings
    if 'rating' in rat:
        ratings[title] = rat['rating']

print(ratings)

with open('ratings.pickle','wb') as f:
    pickle.dump(ratings,f)

print('ratings has been saved.')

# create a dictionary that has a list of reviews for each of the titles that have reviews.

userratings = {}

for title in movienumbers:
    rat = imdb.get_title_user_reviews(title)
    # skip movies that don't have reviews
    if 'reviews' in rat:
        dummylist = []
        for entry in rat['reviews']:
            dummylist.append(entry['reviewText'])

        userratings[title] = dummylist

print(userratings)

with open('userratings.pickle','wb') as f:
    pickle.dump(userratings,f)

print('userratings has been saved.')
# create a dictionary that has a list of reviews for each of the titles that have reviews.

metaratings = {}

for title in movienumbers:
    rat = imdb.get_title_metacritic_reviews(title)
    # skip movies that don't have reviews
    if 'reviews' in rat:
        dummylist = []
        for entry in rat['reviews']:
            dummylist.append(entry['quote'])

        metaratings[title] = dummylist

print(metaratings)
with open('metaratings.pickle','wb') as f:
    pickle.dump(metaratings,f)

print('metaratings has been saved.')




# The actual code begins here
# This file is intended to load everything downloaded from loaddata.py, preventing user getting banned from IMDB
# The code is written to see what are some key words of the reviews from critics and normal viewers
# And to see what are some of the differences
# The second task is to asses the people's emotion vs. actual score given

# First, we need to load back everything we dumped to folder via pickle.

import pickle
print('loading data...')

with open('movienumbers.pickle','rb') as input_file:
    movienumbers = pickle.load(input_file)

with open('ratings.pickle','rb') as input_file:
    ratings = pickle.load(input_file)

with open('userratings.pickle','rb') as input_file:
    userratings = pickle.load(input_file)

with open('metaratings.pickle','rb') as input_file:
    metaratings = pickle.load(input_file)

print('Pickled data successfully loaded.')

# then, it's time to use nltp to see the score of the critics vs. viewers on movies

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# print(movienumbers)
# print(ratings)
# print(userratings)
# print(metaratings)

# Userratings is a dictionary in ways like this "ttxxxxxx : [reviews1, reviews2,...]"

# print(userratings['tt0111161'])
#
# print(metaratings['tt0111161'])
# print(ratings['tt0111161'])

userscore = {}
for movieid, reviews in userratings.items():
    score = 0
    for eachreviews in reviews:
        score += SentimentIntensityAnalyzer().polarity_scores(eachreviews)['compound']
    average = score / len(reviews)
    userscore[movieid] = average

print(userscore)

# Meta ratings is a dictionary in ways like this "ttxxxxxx : [reviews1, reviews2,...]"



criticsscore = {}
for movieid, reviews in metaratings.items():
    score_1 = 0
    for eachreviews in reviews:
        score_1 += SentimentIntensityAnalyzer().polarity_scores(eachreviews)['compound']
    average = score_1 / len(reviews)
    criticsscore[movieid] = average

print(criticsscore)


# Question 1: Are critics always more positive than the audience?

counter = 0
for movieid, score in userscore.items():
    if movieid in criticsscore and criticsscore[movieid] > score:
        counter += 1
    else:
        counter += 0

print("Critics overpraise these movies " + str(counter) + " times more than normal viewers out of "
      + str(len(criticsscore)) + " movies in total.")

# Question 2: Is the IMDB score closer to the users' sentiment? Or the critics.

useriscloser = 0
criticiscloser = 0
for movieid, score in criticsscore.items():
    if abs(userscore[movieid] - (ratings[movieid])/10) > abs(score - (ratings[movieid]/10)):
        useriscloser += 1
    else:
        criticiscloser += 1

print("Critics are more closer to the ratings for " + str(criticiscloser) +
      " times, while normal viewers are closer " + str(useriscloser) + " times out of " +
      str(len(criticsscore)) + " movies in total.")
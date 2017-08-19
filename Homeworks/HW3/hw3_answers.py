import tweepy
import time
import pandas as pd

#Get access to API
auth = tweepy.OAuthHandler('your_consumer_key', 'your_consumer_secret')
auth.set_access_token('your_access_token', 'your access_token_secret')
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# Generate a function to dollect the data to answer the first 4 questions.
# It gets the first degree information.
def getfirdegree(twitteruser, relationship):
    names = []
    ntweets = []
    nfollowers = []
    for user in tweepy.Cursor(getattr(api, relationship), screen_name =
    twitteruser, count = 200, include_entities = True).items():
        names.append(user.screen_name)
        ntweets.append(user.statuses_count)
        nfollowers.append(user.followers_count)
    # put everything into a dataset and return it:
    return pd.DataFrame({"names":names, "ntweets": ntweets,
    "nfollowers":nfollowers})

# Generate a function that classify users.
def usertype(nfollowers):
    typeuser = []
    for i in range(0, len(nfollowers)):
        if nfollowers[i] < 101: typeuser.append("layman")
        if nfollowers[i] >= 101 and nfollowers[i] < \
        1000: typeuser.append("expert")
        if nfollowers[i] >= 1000: typeuser.append("celebrity")
    return typeuser

# Generate a function to dollect the data to answer the last 2 questions.
# It gets the second degree information.
def getsecdegree(listusers, relationship, progress = True):
    names = []
    ntweets = []
    nonauthorized = []
    n = 0.00
    for i in listusers:
        if progress:
            print round(n/float(len(listusers)), 2)
            n += 1.00
        try:
            for user in tweepy.Cursor(getattr(api, relationship),
            screen_name = i, count = 200, include_entities = True).items():
                names.append(user.screen_name)
                ntweets.append(user.statuses_count)
        except tweepy.TweepError:
            nonauthorized.append(i)
    # put everything in a dataset:
    data = pd.DataFrame({"names":names, "ntweets": ntweets})
    # put the dataframe and the nonauthorized list into a single list.
    output = [data, nonauthorized]
    # return the list.
    return output

# Generate a function to answer the questions.
# It can be used to find the most popular and the
# most active user.
def answerquestions(data, variable, usertype = None):
    df = data
    if usertype == None: return df.loc[df[variable].idxmax()].names
    if usertype == "layman": return df[df.type == 'layman'].loc[df[df.type ==
    'layman']['ntweets'].idxmax()].names
    if usertype == "expert": return df[df.type == 'expert'].loc[df[df.type ==
    'expert']['ntweets'].idxmax()].names
    if usertype == "celebrity": return df[df.type == 'celebrity'].loc[df[df.type ==
    'celebrity']['ntweets'].idxmax()].names
    if usertype not in ("layman", "expert", "celebrity"):
        raise ValueError("Please, choose a valid user type.")

# Get all the data that is needed to answer the questions.
# Get followers data:
datafollowers = getfirdegree('NYUpolitics', 'followers')
# Get friends data:
datafriends = getfirdegree('NYUpolitics', 'friends')
# Classify followers and add the collunm
typefollowers = usertype(datafollowers['nfollowers'])
datafollowers["type"] = typefollowers
# Classify friends and add the collunm
typefriend = usertype(datafriends['nfollowers'])
datafriends["type"] = typefriend
# Subset the data to collect the second degree followers and friends
subdatafollowers = datafollowers[['names', 'type']].query('type != "celebrity"')
subdatafriends = datafriends[['names', 'type']].query('type != "celebrity"')
# Get Followers of Followers
datafollowersOf = getsecdegree(subdatafollowers['names'], 'followers')
# Get Friends of Friends
datafriendsOf = getsecdegree(subdatafriends['names'], 'friends')
# Concatenate the Followers dataset and the Followers Of dataset
dataframes = [datafollowers, datafollowersOf[0]]
datafollowersUn = pd.concat(dataframes)
# Concatenate the Friends dataset and the Friends Of dataset
dataframes = [datafriends, datafriendsOf[0]]
datafriendsUn = pd.concat(dataframes)
# Export the data to .csv
datafollowers.to_csv("datafollowers.csv")
datafriends.to_csv("datafriends.csv")
datafollowersUn.to_csv("datafollowersUn.csv")
datafriendsUn.to_csv("datafriendsUn.csv")

# Question 1
print """Most active user is defined as the user with largest number of
total tweets."""
print """Among the followers of your target who is the most active?
(Most active: Total number of tweets.)"""
print "The most active is %s." % answerquestions(datafollowers, 'ntweets')
# Question 2
print """Among the followers of your target who is the most popular, i.e. has
the greatest number of followers?"""
print "The most popular is %s." % answerquestions(datafollowers, 'nfollowers')
# Question 3
print """Among the friends of your target, i.e. the users she is following, who
are the most active layman, expert and celebrity?"""
print """The most active layman is %s, most active expert is %s,
and the most active celebrity is %s.""" % (answerquestions(datafriends, 'ntweets',
'layman'), answerquestions(datafriends, 'ntweets', 'expert'),
answerquestions(datafriends, 'ntweets', 'celebrity'))
# Question 4
print "Among the friends of your target who is the most popular?"
print "The most popular is %s." % answerquestions(datafriends, 'nfollowers')
# Question 5:
print """Among the followers of your target and their followers,
who is the most active?"""
print "The most active is %s." % answerquestions(datafollowersUn, 'ntweets')
print """PS: Data from %s users were not collected because their accounts have
privacy locks or are suspended by Twitter.""" % len(datafollowersOf[1])
# Question 6:
print """Among the friends of your target and their friends,
who is the most active?"""
print "The most active is %s." % answerquestions(datafriendsUn, 'ntweets')

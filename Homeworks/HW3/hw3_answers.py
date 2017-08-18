import tweepy
import time

#Get access to API
auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret')
auth.set_access_token('your access token', 'your access token secret')
api = tweepy.API(auth, wait_on_rate_limit = True)

#Create user objects
nyupolitics = api.get_user('NYUpolitics')

# Collect the data to answer the first 4 questions:
follower_names = []
follower_ntweets = []
follower_nfollowers = []
for user in tweepy.Cursor(api.followers, screen_name = 'NYUpolitics', count = 200, include_entities = True).items():
    try:
        follower_names.append(user.screen_name)
        follower_ntweets.append(user.statuses_count)
        follower_nfollowers.append(user.followers_count)
    except tweepy.TweepError:
        time.sleep(900)
        continue

friend_names = []
friend_ntweets = []
friend_nfollowers = []
for user in tweepy.Cursor(api.friends, screen_name = 'NYUpolitics', count = 200, include_entities = True).items():
    try:
        friend_names.append(user.screen_name)
        friend_ntweets.append(user.statuses_count)
        friend_nfollowers.append(user.followers_count)
    except tweepy.TweepError:
        time.sleep(900)
        continue

# Question 1
print """Among the followers of your target who is the most active?
(Most active: Total number of tweets.)"""
print follower_names[follower_ntweets.index(max(follower_ntweets))]
# Question 2
print """Among the followers of your target who is the most popular, i.e. has the
greatest number of followers?"""
print follower_names[follower_nfollowers.index(max(follower_nfollowers))]
# Question 3
print """Among the friends of your target, i.e. the users she is following, who are the
most active layman, expert and celebrity?"""
# Find the ids of all laymen, experts, celebrities followers
idlaymen = []
idexperts = []
idcelebrities = []
for i in range(0, len(friend_nfollowers)):
    if friend_nfollowers[i] < 101: idlaymen.append(i)
    if friend_nfollowers[i] >= 101 and friend_nfollowers[i] < 1000: idexperts.append(i)
    if friend_nfollowers[i] >= 1000: idcelebrities.append(i)
# Find the names and the number of tweets for each leyman
laymen_names = [friend_names[i] for i in idlaymen]
laymen_tweets = [friend_ntweets[i] for i in idlaymen]
print "The most active layman is: %s" % laymen_names[laymen_tweets.index(max(laymen_tweets))]
# Find the names and the number of tweets for each expert
experts_names = [friend_names[i] for i in idexperts]
experts_tweets = [friend_ntweets[i] for i in idexperts]
print "The most active expert is: %s" % experts_names[experts_tweets.index(max(experts_tweets))]
# Find the names and the number of tweets for each celebrity
celebrities_names = [friend_names[i] for i in idcelebrities]
celebrities_tweets = [friend_ntweets[i] for i in idcelebrities]
print "The most active celebrity is: %s" % celebrities_names[celebrities_tweets.index(max(celebrities_tweets))]
# Question 4
print "Among the friends of your target who is the most popular?"
print "The most popular friend is: %s" %  friend_names[friend_nfollowers.index(max(friend_nfollowers))]

# Collect the data to answer the last 2 questions:
# Find the laymen and experts among followers
follower_layexp_names = []
total = 0
for i in range(0, len(follower_nfollowers)):
    if follower_nfollowers[i] < 1000:
        follower_layexp_names.append(follower_names[i])
        total += follower_nfollowers[i]
# Collect the necessary information about the followers of the followers of NYUpolitics
followerOf_names = []
followerOf_ntweets = []
for i in follower_layexp_names:
    try:
        for user in tweepy.Cursor(api.followers, screen_name = i, count = 200, include_entities = True).items():
            followerOf_names.append(user.screen_name)
            followerOf_ntweets.append(user.statuses_count)
    except tweepy.TweepError:
        print """Failed to collect the information from %s.
        Next...""" % i
    except RateLimitError:
        time.sleep(915)
#oldlen it contains where the loop was stoping

# Unify the experts and laymen friends:
friend_layexp_names = experts_names + laymen_names
# Collect the necessary information about the friends of the friends of NYUpolitics
friendOf_names = []
friendOf_ntweets = []
for i in friend_layexp_names:
    try:
        for user in tweepy.Cursor(api.friends, screen_name = i, count = 200, include_entities = True).items():
            friendOf_names.append(user.screen_name)
            friendOf_ntweets.append(user.statuses_count)
    except tweepy.TweepError:
        print """Failed to collect the information from %s.
        Next...""" % i
    except RateLimitError:
        time.sleep(915)

# Question 5:
print """Among the followers of your target and their followers,
who is the most active?"""
# Unify the number of tweets between followers and followers of followers
ffnames = followerOf_names + follower_names
ffntweets = followerOf_ntweets + follower_ntweets
print """The most active user among followers and followers of followers
is: %s""" % ffnames[ffntweets.index(max(ffntweets))]

# Question 6:
print """Among the friends of your target and their friends,
who is the most active?"""
# Unify the number of tweets between followers and followers of followers
frfrnames = friend_names + friendOf_names
frfrntweets = friend_ntweets + friendOf_ntweets
print """The most active user among friends and friends of friends
is: %s""" % frfrnames[frfrntweets.index(max(frfrntweets))]
import GetOldTweets3 as got
username = 'Dadsaysjokes'
count = 3000
user_tweets=[]
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
for w in range (0,count):
	try:
		
			user_tweets.append(tweets[w].text)
	except :
		pass

for x in range (0,count):
	try:
		
		f= open("Dadsaysjokes/Dadsaysjokes"+str(x)+".txt","w+")
		f.write(user_tweets[x])
	except :
		pass



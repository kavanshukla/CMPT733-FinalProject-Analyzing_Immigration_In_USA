import tweepy
from textblob import TextBlob
import csv

#Authentication to access Twitter API
consumer_key= 'Use your Consumer Key'
consumer_secret= 'Use your Consumer Secret'

access_token='Use your Access Token'
access_token_secret='Use your Access Token Secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Topics to be searched for, on Twitter
search_topics=['H-1B', 'H1B', 'USVISA', 'USImmigration', 'Travelban']

#Deciding sentiment label based on polarity score
def sentiment_label(analysis):
	if analysis.sentiment.polarity>0:
		return 'Positive'
	elif analysis.sentiment.polarity == 0:
            return 'Neutral'
	else:
		return 'Negative'
		
for search_item in search_topics:

#Retrieving Tweets
	if(search_item=='H-1B' or search_item=='H1B'):
		public_tweets = api.search(q=search_item, count=100, since='2017-03-16' ,until='2017-04-07', lang='en')
	if(search_item=='Travelban'):
		public_tweets = api.search(q=search_item, count=100, lang='en')
	if(search_item=='USVISA' or search_item=='USImmigration'):
		public_tweets = api.search(q=search_item, count=100, since='2017-01-16' ,until='2017-04-07', lang='en')
	csvFile = open('%s_tweets.csv' % search_item, 'wb')
	csvWriter = csv.writer(csvFile)

	csvWriter.writerow(['tweet','sentiment_label'])
	for tweet in public_tweets:
		text = tweet.text
		#Performing Sentiment Analysis on Tweets
		analysis = TextBlob(tweet.text)
		label = sentiment_label(analysis)
		#Writing Tweet and its label to .CSV file
		csvWriter.writerow([text.encode('utf8'), label])
	csvFile.close()
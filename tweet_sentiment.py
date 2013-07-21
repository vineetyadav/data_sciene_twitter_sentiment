import csv
import sys
import json
sentiment_file = open(sys.argv[1],'r')
tweet_file = open(sys.argv[2],'r')
sentiment_dict = {}
for each_sentiment in sentiment_file:
    sentiment_tuple = each_sentiment.split()
    sentiment_dict.setdefault(" ".join(sentiment_tuple[0:-1]), sentiment_tuple[-1])
for each_tweet in tweet_file:
    each_tweet_json = json.loads(each_tweet)
    tweet_tokens = each_tweet_json['text'].encode('utf-8').split()
    tweet_score = 0
    
    for each_token in tweet_tokens:
        
        tweet_score = tweet_score+ int(sentiment_dict.get(each_token,0))
    print float(tweet_score) 
   
            

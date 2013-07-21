import csv
import sys
import json
sentiment_file = open(sys.argv[1],'r')
tweet_file_list = open(sys.argv[2],'r')
sentiment_dict = {}
for each_sentiment in sentiment_file:
    sentiment_tuple = each_sentiment.split()
    sentiment_dict.setdefault(" ".join(sentiment_tuple[0:-1]), sentiment_tuple[-1])
max_score = 0
country_code = ""
place = ""
for each_tweet_file in tweet_file_list:
    #each_tweet_json_file = open('output/'+each_tweet_file.strip(),'r')
    #print each_tweet_file.strip()
    each_tweet_json = json.loads(each_tweet_file)
    #max_score = 0
    #country_code = ""
    #print each_tweet_file
    if each_tweet_json.get('place') and each_tweet_json['user']['lang'] =='en' and each_tweet_json['place']['country_code']:                            
        tweet_tokens = each_tweet_json['text'].split()
        tweet_score = 0
    
        for each_token in tweet_tokens:
        
            tweet_score = tweet_score+ int(sentiment_dict.get(each_token,0))
        if tweet_score > max_score:
            country_code = each_tweet_json['place']['country_code']
            max_score = tweet_score
            place = each_tweet_json["place"]
        
            

print place['full_name'].split(",")[-1].strip()

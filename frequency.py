import json

def compute_frequency(infile):
    tweet_dict = {}
    frequency_dict = {}
    total_count = 0 
    for each_tweet in infile:
        each_tweet_json = json.loads(each_tweet)
        
        tweet_token = each_tweet_json['text'].encode('utf').split()
        for each_token in tweet_token:
            tweet_dict.setdefault(each_token,0)
            tweet_dict[each_token] = tweet_dict[each_token]+1
            total_count = total_count +1
    for each_token in tweet_dict:
        frequency_dict[each_token] = float(1.0*tweet_dict[each_token]/float(total_count))
    return frequency_dict

if __name__=='__main__':
    import sys
    infile = open(sys.argv[1],'r')
    frequency_dict = compute_frequency(infile)
    #print frequency_dict
    for each in frequency_dict:
        fq = frequency_dict[each]
        #fq = '{4:f}'.format(fq)
        print("%s %f" %(each, fq))

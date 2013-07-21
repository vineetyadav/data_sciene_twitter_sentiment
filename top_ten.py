import sys
import re
import operator
import json
file = open(sys.argv[1],'r')
hash_tag_dict = {}
for s in file:
    s_json = json.loads(s)
    hashtags = s_json['entities']['hashtags'] 
    #hastags  = re.findall(r"#(\w+)", s)
    for eachh in hashtags:
        #print eachh
        hash_tag_dict.setdefault(eachh["text"], 0.0)
        hash_tag_dict[eachh["text"]] = hash_tag_dict[eachh["text"]] + 1.0
hash_tag_dict = sorted(hash_tag_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
count = 0
#print hash_tag_dict
for each in hash_tag_dict:
    if count<10:
        print each[0].encode("utf-8"), each[1]
    count = count +1

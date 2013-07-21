Twitter_sentiment module is used to find sentiment of twitter 
Modules uses two input files 
AIFNN-111.txt and input.txt 
AIFFN-111.txt is sentiment dict. and input.txt contains tweet input. 
Modules has following parts 

1)tweet_sentiment.py:- tweet_sentiment compute sentiment of tweet. 
        Command to run:- python tweet_sentiment.py AIFNN-111.txt input.txt
 
2)term_sentiment.py:- term_sentiment compute sentiment of unknown words.
        Command to run:- python term_sentiment.py AIFNN-111.txt input.txt

3)top_ten.py:- top_ten.py finds top ten hashtags in tweets. 
	Command to run:- python top_ten.py input.txt
4)happiest_state.py:- happiest_state.py is used to find happiest state from tweet
        Command to run:- python happiest_state.py input.txt

5)frequency:- frequency.py used to compute frequency for words of tweet 
	Command to run:- python frequency.py input.txt  
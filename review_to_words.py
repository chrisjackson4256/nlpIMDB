from bs4 import BeautifulSoup
import re

def review_to_words( raw_review ):
	''' function to convert raw IMDB review 
		to list of words'''
	# remove markup and tags
	bs_review = BeautifulSoup( raw_review )
	# remove numbers and punctuation
	letters_only = re.sub(r'[^a-zA-Z]', ' ', bs_review.get_text())
	# convert to lower case
	lower_case = letters_only.lower()
	# split string into list
	words_only = lower_case.split()
	# define the stop words
	stops = set(stopwords.words("english"))
	# remove stop words from review
	words = [w for w in words_only if w not in stops]

	return " ".join(words)
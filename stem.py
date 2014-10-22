#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-10-22 21:51:00
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-10-22 21:58:27
from nltk.stem.porter  import PorterStemmer

class Stemmer:

    def __init__(self):
        self.worker = PorterStemmer()

    def stemming(self, word):
        return self.worker.stem(word)

    def stem_sent(self, words):
        return [unicode(self.stemming(word)) for word in words]

    def stem(self, wordslist, ):
        return [self.stem_sent(words) for words in wordslist]
    


if __name__=="__main__":
	import tokenizer
	s = tokenizer.Tokenizer()
	#w = s.tokenize('I\'m studying computers science.')
	with open("test") as fin:
		#text = [l.strip().lower().split() for l in fin]
		text = fin.read()
	w = s.tokenize(text)
	stemmer = Stemmer()
	print stemmer.stem(w)

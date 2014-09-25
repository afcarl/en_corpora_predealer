#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-25 14:20:13
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-25 15:12:21

import nltk
from nltk.stem.wordnet import wordnet

class Postagger:
	def __init__(self):
		self.convertmap = { 'J' : wordnet.ADJ,
							'V' : wordnet.VERB,
							'N' : wordnet.NOUN,
							'R' : wordnet.ADV}

	def tags(self, wordlist):
		result = nltk.pos_tag(wordlist)
		return [item[1] for item in result]

	def tags2lemma(self, tag):
		for (captital, result) in self.convertmap.items():
			if tag.startswith(captital):
				return result
		return ''

	def tags2lemmatags(self, taglist):
		return [self.tags2lemma(item) for item in taglist]

if __name__=="__main__":
	import tokenizer
	s = tokenizer.Tokenizer()
	w = s.tokenize('I\'m a student form tsinghua University')
	pos = Postagger()
	tags = pos.tags(w)
	print pos.tags2lemmatags(tags)
	#poslist = [get_wordnet_pos(item[1]) for item in pos.tags(w)]
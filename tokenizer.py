#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-25 13:33:50
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-25 14:00:49
import string, nltk

class Tokenizer:
	def __init__(self, lower=True, punctuation=True, digits=True):
		self.symbols = string.punctuation.replace('-','')
		self.digits = string.digits
		self.switch_lower = lower
		self.switch_punctuation = punctuation
		self.switch_digits = digits

	def clean_line(self, line):
		if self.switch_lower:
			line = line.lower()
		if self.switch_punctuation:
			for t in self.symbols:
				line = line.replace(t, ' ')
		if self.switch_digits:
			for t in self.digits:
				line = line.replace(t, ' ')
		
		return line

	def tokenize(self, line):
		line = self.clean_line(line)
		return nltk.word_tokenize(line)

if __name__=="__main__":
	sentence = "I am a student from Tsinghua University"
	s = Tokenizer()
	print s.tokenize(sentence)

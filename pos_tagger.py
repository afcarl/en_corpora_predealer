#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-25 14:20:13
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-25 19:41:58

import nltk
from nltk.stem.wordnet import wordnet


class Postagger:

    def __init__(self):
        self.convertmap = {'J': wordnet.ADJ,
                           'V': wordnet.VERB,
                           'N': wordnet.NOUN,
                           'R': wordnet.ADV}

    def __tags__(self, wordlist):
        result = nltk.pos_tag(wordlist)
        return [item[1] for item in result]

    def tags2lemma(self, tag):
        for (captital, result) in self.convertmap.items():
            if tag.startswith(captital):
                return result
        return ''

    def __tags2lemmatags__(self, taglist):
        return [self.tags2lemma(item) for item in taglist]

    def batch_tags2lemmatags(self, taglistlist):
    	return [self.__tags2lemmatags__(item) for item in taglistlist]

    def batch_tags(self, wordlistlist):
		return [self.__tags__(wordlist) for wordlist in wordlistlist]
if __name__ == "__main__":
    import tokenizer
    s = tokenizer.Tokenizer()
    w = s.tokenize('I\'m a student form tsinghua University')
    pos = Postagger()
    print dir(pos)
    #poslist = [get_wordnet_pos(item[1]) for item in pos.tags(w)]

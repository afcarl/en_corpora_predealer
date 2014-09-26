#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-25 14:20:13
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-26 18:46:32

import nltk
from nltk.stem.wordnet import wordnet


class Postagger:

    def __init__(self):
        self.convertmap = {'J': wordnet.ADJ,
                           'V': wordnet.VERB,
                           'N': wordnet.NOUN,
                           'R': wordnet.ADV}

    def tags_sent(self, wordlist):
        result = nltk.pos_tag(wordlist)
        return [item[1] for item in result]

    def tags2lemma(self, tag):
        for (captital, result) in self.convertmap.items():
            if tag.startswith(captital):
                return result
        return ''

    def tags2lemmatags_sent(self, taglist):
        return [self.tags2lemma(item) for item in taglist]

    def tags2lemmatags(self, taglistlist):
    	return [self.tags2lemmatags_sent(item) for item in taglistlist]

    def tags(self, wordlistlist):
		return [self.tags_sent(wordlist) for wordlist in wordlistlist]
if __name__ == "__main__":
    import tokenizer
    s = tokenizer.Tokenizer()
    w = s.tokenize('I\'m a student form tsinghua University')
    print w
    pos = Postagger()
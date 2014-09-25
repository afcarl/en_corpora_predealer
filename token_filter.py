#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-25 13:51:05
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-25 19:24:11
import nltk


class TokenFilter:

    def __init__(self, stop=True, min_length=3):
        self.switch_stop = stop
        self.switch_min_length = min_length
        if self.switch_stop:
            self.stoplist = nltk.corpus.stopwords.words('english')

    def check(self, word):
        if self.switch_stop:
            if word in self.stoplist:
                return False
        if self.switch_min_length:
            if len(word) < self.switch_min_length:
                return False

        return True

    def filter(self, wordlist):
        return [item for item in wordlist if self.check(item)]

    def batch_filter(self, wordlistlist):
        return [self.filter(wordlistlist) for wordlist in wordlistlist]

if __name__ == "__main__":
    import tokenizer
    line = "I am a student from Tsinghua University"
    s = TokenFilter()
    t = tokenizer.Tokenizer()

    print s.filter(t.tokenize(line))

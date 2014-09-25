#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-24 21:52:46
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-25 19:42:24
from pos_tagger import Postagger
from lemma import Lemmatizer
from token_filter import TokenFilter
from tokenizer import Tokenizer


class Preprocesser:

    def __init__(self, lower=True, punctuation=True, digits=True, stop=True, min_length=3,
                 pos_tag=False, lemmatization=True):

        self.lemma = lemmatization
        self.pos_tag = pos_tag

        self.tokenizer = Tokenizer(lower, punctuation, digits)
        self.token_filter = TokenFilter(stop, min_length)
        if pos_tag or lemmatization:
            self.postagger = Postagger()
            print dir(self.postagger)
        if lemmatization:
            self.Lemmatizer = Lemmatizer()

    def process(self, text):
        words = self.tokenizer.tokenize(text)
        print words
        if self.lemma:
            tags = self.postagger.batch_tags2lemmatags(self.postagger.batch_tags(words))
            result = self.Lemmatizer.batch_lemma(words, tags)
        if self.pos_tag:
            tags = self.postagger.batch_tags(words)
            result = tags
        return result
if __name__ == "__main__":
    text = "I'm a student in Tsinghua University. I'm studying computer science"
    processer = Preprocesser()
    print processer.process(text)

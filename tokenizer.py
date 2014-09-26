#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-25 13:33:50
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-26 15:49:40
import string
import nltk


class Tokenizer:

    def __init__(self, lower=True, punctuation=True, digits=True):
        self.symbols = string.punctuation.replace('-', '')
        self.symbols = self.symbols.replace('\'', '')
        self.sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
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

    def tokenize(self, text):
        sents = self.sentence_tokenize(text)
        lines = [self.clean_line(line) for line in sents]
        result = [nltk.word_tokenize(line) for line in lines]
        return result
        # return nltk.word_tokenize(line)

    def sentence_tokenize(self, text):
        return self.sent_tokenizer.tokenize(text)


if __name__ == "__main__":
    sentence = "I'm a student from Tsinghua University. I'm an undergraduate student."
    s = Tokenizer()
    print s.tokenize(sentence)

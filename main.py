#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-24 21:52:46
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-26 18:56:28
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
        words = self.token_filter.filter(words)
        if self.lemma:
            tags = self.postagger.tags2lemmatags(self.postagger.tags(words))
            result = self.Lemmatizer.lemma(words, tags)
        if self.pos_tag:
            tags = self.postagger.tags(words)
            result = tags
        return result

class TextPreProcessor(object):
    def __init__(self, input_filename=None, output_filename=None):
        self.input = input_filename
        self.output = output_filename

    def format(self, input_filename=None, output_filename=None):
        if input_filename is not None:
            self.input= input_filename
        if output_filename is not None:
            self.output = output_filename
        processer = Preprocesser()
        with open(self.input) as input, open(self.output,"w") as output:
            for l in input:
                result = processer.process(l.strip())
                result = [" ".join(item) for item in result]
                for item in result:
                    print >>output, item,
                print >>output
                
if __name__ == "__main__":
    text = "I'm a student in Tsinghua University. I'm studying computer science"
    text = TextPreProcessor()
    text.format("test.data","test.data.out")
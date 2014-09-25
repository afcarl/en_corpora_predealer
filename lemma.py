#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: largelymfs
# @Date:   2014-09-25 15:26:03
# @Last Modified by:   largelymfs
# @Last Modified time: 2014-09-25 19:31:43
from nltk.stem.wordnet import WordNetLemmatizer


class Lemmatizer:

    def __init__(self):
        self.worker = WordNetLemmatizer()

    def lemmazation(self, word, tag):
        if tag == '':
            return word
        else:
            return self.worker.lemmatize(word, tag)

    def lemma(self, words, lemmatags):
        return [self.lemmazation(word, tag) for (word, tag) in zip(words, lemmatags)]

    def batch_lemma(self, wordslist, lemmatagslist):
        return [self.lemma(words, lemmatags) for (words, lemmatags) in zip(wordslist, lemmatagslist)]
    
if __name__ == "__main__":
    import pos_tagger
    import tokenizer
    s = tokenizer.Tokenizer()
    w = s.tokenize('I\'m studying computers science')
    pos = pos_tagger.Postagger()
    tags = pos.tags(w)
    tags = pos.tags2lemmatags(tags)
    lemma = Lemmatizer()
    print w
    print lemma.lemma(w, tags)

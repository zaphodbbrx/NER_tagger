#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:45:17 2018

@author: lsm
"""
from polyglot.text import Text
from polyglot.detect import Detector

class LanguageNotAvailableError(Exception):
    pass

class LanguageNotRecognisedError(Exception):
    pass 

class NER_tagger():
    def __init__(self):
        self.__langs = ['en', 'de', 'ru','cn', 'jp', 'es']
        
    def lang_detect(self, text, threshold = 0.9):
        detector = Detector(text,quiet = True)
        if detector.language.confidence>threshold:
            return detector.language.code
        else:
            raise LanguageNotRecognisedError('Could not recognize the language')
    def find_entites(self,input_text):
        lang = self.lang_detect(input_text)
        
        def get_tagged_tuple(word, entities):
            for e in entities:
                if word in list(e):
                    return (' '.join(e),e.tag)
            return (word, None)
        
        def remove_duplicates(l):
            seen = set()
            result = []
            for item in l:
                if item not in seen:
                    seen.add(item)
                    result.append(item)
            return result
        if lang in self.__langs:
            text = Text(input_text)
            sents_res = []
            for sent in text.sentences:
                word_tags = []
                for wrd in sent.words:
                    tagged_tuple = get_tagged_tuple(wrd, text.entities)
                    word_tags.append(tagged_tuple)
                sents_res.append(remove_duplicates(word_tags))
            res = {
                    'lang': lang,
                    'ner_result': sents_res
                    }
            return res
        else:
            raise LanguageNotAvailableError('Language is not available')

if __name__ == '__main__':
    ner = NER_tagger()
    while True:
        text = input()
        print('Language: '+ ner.lang_detect(text))
        print('Result: \n')
        print(ner.find_entites(text))

        
        
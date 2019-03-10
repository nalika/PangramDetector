# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:57:56 2019

@author: akilan
"""

import string


class PangramDetector:
    def __init__(self, String):
        self.String = String
  

    def findMissingLetters(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        findMissingLetters = ""
        
        phrase = self.String
        
        phrase = phrase.lower()
    
        for char in alphabet:
            if char in phrase:
                #phraseLetters += char
                continue
            else:
                findMissingLetters += char
      
        return findMissingLetters
        

# Test cases        
p1 = PangramDetector("The quick brown fox jumps over the lazy dog")
print(p1.findMissingLetters())

p1 = PangramDetector("The slow purple oryx meanders past the quiescent canine")
print(p1.findMissingLetters())

p1 = PangramDetector("We hates Bagginses!")
print(p1.findMissingLetters())

p1 = PangramDetector("abcdefghijklmnopqrstuvwxyz")
print(p1.findMissingLetters())
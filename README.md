# PangramDetector

The sentence "The quick brown fox jumps over the lazy dog" contains every single letter in the alphabet. Such sentences are called pangrams.
You are to write a function getMissingLetters, which takes a String, sentence, and returns all the letters it is missing (which prevent it from being a pangram). You should ignore the case of the letters in sentence, and your return should be all lower case letters, in alphabetical order.
You should also ignore all non US-ASCII characters.

The code you submit must contain a method that conforms to the expected function definition:

Java Definition
Public Class: PangramDetector
Method signature: public String findMissingLetters(String sentence)

Examples:

(Note that in the examples below, the double quotes should not be considered part of the input or output strings.)

0)  "The quick brown fox jumps over the lazy dog"

Returns: ""
(This sentence contains every letter)

1)  "The slow purple oryx meanders past the quiescent canine"
Returns: "bfgjkvz"

2)  "We hates Bagginses!"
Returns: "cdfjklmopqruvxyz"

3)  ""
Returns: "abcdefghijklmnopqrstuvwxyz"

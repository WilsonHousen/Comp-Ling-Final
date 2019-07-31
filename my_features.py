"""Example of a feature function file."""


from __future__ import division

import arff_writer


@arff_writer.feature()
def word_count(text):
    """Total number of words in the text."""
    return len(text.split())


@arff_writer.feature()
def lexical_diversity(text):
    """Total number of words in the text divided by the number of
    distinct words in the text.
    """
    words = [word.lower() for word in text.split()]
    distinct_words = set(words)
    return len(distinct_words) / len(words)
    
@arff_writer.feature()
def unique_words(text):
    """just the distinct words"""
    words = [word.lower() for word in text.split()]
    distinct_words = set(words)
    return len(distinct_words)

## new features

@arff_writer.feature()
    ## average sentence length, assuming that only periods, exclamation points
    ## and question marks are the only delimiter of sentences, and that they do
    ## nothing else in a text
def avSentenceLength(text):
    acSentLength = 0
    sentcount = 0
    lengthAcc = 0
    listOfSents = []
    for sent in text.split('.'):
        for sent2 in sent.split('?'):
            for sent3 in sent2.split('!'):
                listOfSents.append(sent3)
    sentcount = len(listOfSents)
    for sentc in listOfSents:
        lengthAcc = lengthAcc + len(sentc)
    avSentLength = lengthAcc / sentcount
    return avSentLength

@arff_writer.feature()
    ## number of pronouns in a text; just subject or object ones
def numPronouns(text):
    pronouncount = 0
    for word in text.split():
        if word == "i" or "you" or "he" or "she" or "it" or "we" or "they" or "me" or "him" or "her" or "us" or "them":
            pronouncount = pronouncount + 1
        if word == "I" or "You" or "He" or "She" or "It" or "We" or "They" or "Me" or "Him" or "Her" or "Us" or "Them":
            pronouncount = pronouncount + 1
    return pronouncount

@arff_writer.feature()
    ## average length of each word
def avWordLength(text):
    wordcount = len(text.split())
    wordlenacc = 0
    for word in text.split():
        wordlenacc = wordlenacc + len(word)
    return wordlenacc / wordcount






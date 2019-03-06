#!/usr/bin/env python3

"""The Drama Generator!

Be an active member of your favourite community or fandom
and start talking about how a person is causing drama!

Public domain, i don't give a fuck if you use this/steal it or whatever.

"""
import random

files = ["people.txt","verbs.txt","nouns.txt","afternoun.txt",
         "endings.txt","starts.txt"]

def getRandomFrom(lst):

    """Literally just returns a pseudo-random entry from list 'lst'"""

    if len(lst)==0:
        return ""

    return lst[random.randint(0,len(lst)-1)]

def getVocab(listoffiles):

    """Puts the files into a list of vocab. Really I should have
    used a dict, but I'm lazy. Takes in a list of filenames. 

    Returns the list of vocab, or 1 if it fails. 

    """
    
    vocab = []
    for file in files:

        try:
            f = open(file,'r')
        except IOError as e:
            print("Couldn't open file!",e)
            return 1

        vocab+=[[w.strip("\n") for w in f]]
    return vocab

def createDramalib(listoffiles):

    """The main do-er of the bunch, takes in a list of files,
    and it shits out a mangled together string. 
    returns 1 otherwise, though I don't have much use for that
    now.

    """


    vocab = getVocab(listoffiles)
    if vocab==1:
        return 1

    person = getRandomFrom(vocab[0])
    verb = getRandomFrom(vocab[1])
    noun = getRandomFrom(vocab[2])
    #afternoun = getRandomFrom(vocab[3]) todo: reimplement
    ending = getRandomFrom(vocab[4])
    person2 = getRandomFrom(vocab[0])
    starts = getRandomFrom(vocab[5])

    rnd = random.randint(0,4)

    if rnd>2:
        resultstart = starts + person 
    else:
        resultstart = person + " is"

    result = resultstart + " " + verb + " " + noun + ", " + ending

    result = result.replace("is is","is")
    result = result.replace("without " + person + " is","without "+person)
    result = result.replace("of " + person + " is","of "+person)
    result = result.replace("is " + person + " is","is "+person)
    result = result.replace("with " + person + " is","with "+person)

    return result



if __name__ == "__main__":

    """This is just to test it, in my experience, it works."""

    for i in range(10):
        print(createDramalib(files))
    

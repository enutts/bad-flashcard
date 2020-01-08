import sys
from random import shuffle

helpstr = """
Usage: sfc [directory of deck] 

sfc or simple flash card is a minimum compliant command line flashcard tool that reads deck files
and acts like a helpful friend helping you study by holding your flashcards and shuffling them for you

Decks:
    save decks in text files with questions and answers on one line seperated by '::'
    example: 
        test question 1 :: answer 1
        test question 2 :: answer 2
"""

def main():
    try:
        deck = sys.argv[1]
        print(deck)
    except:
        print(helpstr)

    with open(deck, 'r') as f:
        deck = list(f)
    
    print('\n\t--hit enter to flip cards--\n')
    
    shuffle(deck)

    for qa in deck:
        q, a = qa.split('::')
        input(q)
        print(a)

if __name__ == '__main__':
    main()

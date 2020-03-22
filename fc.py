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
def study(deck):
    print('\n\t--hit enter to flip cards--\n')
    
    for qa in deck:
        q, a = qa.split('::')
        input(q)
        print(a)
    
def main():
    # Options
    Shuffle = True

    if len(sys.argv) == 1:
        print(helpstr)
        return
    elif len(sys.argv) >= 2:
        if '-h' in sys.argv or '--help' in sys.argv:
            print(helpstr)
            return
        if '-s' in sys.argv:
            Shuffle = False
            sys.argv.pop(sys.argv.index('-s'))
    else:
        print('something went wrong')
    
    # refactor --from here --
    sys.argv.pop(0)
    decks = []
    for arg in sys.argv:
        try:
            with open(arg, 'r') as deckfile:
                decks.append(deckfile.readlines())
        except:
            print('it doesn\'t seem that deck exists')
    
    new = []
    for deck in decks:
        for card in deck:
            new.append(card)
    # -- to here --
    
    if Shuffle == True:
        shuffle(new)
        study(new)
    else:
        study(new)

if __name__ == '__main__':
    main()

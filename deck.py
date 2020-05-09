import sys
import json
from collections import namedtuple
from random import shuffle

helpstr = """ lol """

class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.size = 0

    def from_file(self, filenames):
        decks = []
        for file in filenames:
            try:
                with open(file, 'r') as deckfile:
                    decks.append(deckfile.readlines())
            except IOError:
                print("{} does not appear to exist", file)
                break
        
        self.cards = []
        for deck in decks:
            for card in deck:
                self.cards.append(card)

    def to_string(self):
        pass

    def to_json(self):
        pass
    
    def study(self):
        print('\n\t--hit enter to flip cards--\n')

        for card in self.cards:
            input(card[0])
            input(card[1])

def main():
    # Options
    Shuffle = True

    if len(sys.argv) == 1:
        print(helpstr)

    elif len(sys.argv) >= 2:
        if '-h' in sys.argv or '--help' in sys.argv:
            print(helpstr)
            return
        if '-s' in sys.argv:
            Shuffle = False
            sys.argv.pop(sys.argv.index('-s'))
    else:
        print('something went wrong')
    
    sys.argv.pop(0)

    try:
        new = get_decks(sys.argv)
    except:
        print('{} don\'t seem to exist', sys.argv)

    if Shuffle == True:
        shuffle(new)
        study(new)
    else:
        study(new)

if __name__ == '__main__':
        main()
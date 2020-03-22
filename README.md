# bad-flashcard
braindead simple flash card program in python

## Things it will do
Shows you the front of your flashcard, then the back
Shuffles Decks
Interlieves half of 2 decks together to assist studying
Easily Scriptable

## Things it won't do
Manage your decks of cards

## Usage
./bf /location/of/deck
or 
./bf -i /location/of/deck1 /location/of/deck2

Decks should be plain text files formatted as such: 
SOF
question 1 :: answer 
question 2 :: answer
question 3 :: answer
question 4 :: answer
EOF

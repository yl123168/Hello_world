from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    max_score = 0
    best_word = None
    for e in wordList:
        if is_valid(e, hand):
            e_score = getWordScore(e, n)
            if e_score > max_score:
                max_score = e_score
                best_word = e
    return best_word

def is_valid(word, hand):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    new_hand = hand.copy()
    for i in word:
        new_hand[i] = new_hand.get(i, 0) - 1
    return min(new_hand.values()) >= 0


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    comp_total_sc = 0
    while calculateHandlen(hand) > 0:
        print "Current Hand:  ",
        displayHand(hand)
        comp_word = compChooseWord(hand, wordList, n)
        if comp_word:
            comp_word_sc = getWordScore(comp_word, n)
            comp_total_sc += comp_word_sc
            print('''"%s" earned %d points. Total: %d points'''%(comp_word, comp_word_sc, comp_total_sc))
            hand = updateHand(hand, comp_word)
        else:
            print("Total: %d points"%comp_total_sc)
            break

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    while True:
        user_input = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if user_input == 'n':
            hand = dealHand(HAND_SIZE)
            game_play(hand,wordList,HAND_SIZE)
        elif user_input == 'r' and hand != {}:
            game_play(hand,wordList,HAND_SIZE)
        elif user_input == 'r' and hand == {}:
            print("You have not played a hand yet. Please play a new hand first!\n")
        elif user_input == 'e':
            break
        else:
            print("Invalid command.\n")

def game_play(hand,wordList,HAND_SIZE):
        while True:
            uc_choise = raw_input("Enter u to have yourself play, c to have the computer play:  ")
            if uc_choise == 'u':
                playHand(hand, wordList, HAND_SIZE)
                break
            elif uc_choise == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
                break
            else:
                print("Invalid command.\n")


 
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



import random
full_deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6",
             "7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10",
             "J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
card_deck = full_deck.copy()
random.shuffle(card_deck)

"""
dealer_hand = [card_deck.pop(0)]
player_hand = [card_deck.pop(0)]
dealer_hand.append(card_deck.pop(0))
player_hand.append(card_deck.pop(0))
"""

value = 0
score = 0
countHits = 0

# stateArr = [player_hand,dealer_hand]

def get_card_value(card):
    try:
        card_value = int(card)
    except:
        if card == "J" or card == "Q" or card == "K":
            card_value = 10
        else:
            card_value = 11

    return card_value



def score(stateArr):
    if stateArr[0] > stateArr[1]:
        return 1
    elif stateArr[0] < stateArr[1]:
        return 0
    else:
        return 0.5



def calculateTotal(handArr):
    total = 0
    numAces = 0
    for card in handArr:
        total += get_card_value(card)
        if card == "A":
            numAces += 1

    for i in range(numAces):
        if total > 21:
            total -= 10

    return total

def startAlgorithm(stateArr):
    hit_return = placeOfBattle(stateArr, "hit")
    print(hit_return[0])
    print("\n")
    stand_return = placeOfBattle(stateArr, "stand")
    print(stand_return[0])
    if hit_return[0] > stand_return[0]:
        return hit_return
    else:
        return stand_return


def chanceOfLoss(hand):
    deck = ["2","2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6",
                 "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10",
                 "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
    for card in hand:
        deck.remove(card)

    moreThan = 0

    for card in deck:
        tempHand = hand.copy()
        tempHand.append(card)
        tots = calculateTotal(tempHand)
        if tots > 21:
            moreThan += 1

    return moreThan / len(deck)

def placeOfBattle(stateArr, action):
    # if countHits == 2:  # if terminal
    #    return score(stateArr), []
    # figure out the chance of each option
    # if max(% * placeOfBattle(stateArr), )

    if action == "hit":
        print("hit")
        chanceOfContinuing = 1 - chanceOfLoss(stateArr[0])
        return_value = placeOfBattle(stateArr, "stand")
        return return_value[0] * chanceOfContinuing, ["hit"] + return_value[1]


    else:
        print("stand")
        if calculateTotal(stateArr[1]) >= 17:
            print("dealer stand")
            return score(stateArr), ["stand","stand"]
        else:
            print("dealer hit")
            chanceOfLosing = chanceOfLoss(stateArr[1])
            return max((1 - chanceOfLosing) * score(stateArr), chanceOfLosing * 1), ["stand","hit"]









print(startAlgorithm([["8","6"], ["4","10"]]))

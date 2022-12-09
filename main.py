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

# stateArr = [player_hand,dealer_hand]
#get the value of the card, from string value
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
    player_total = calculateTotal(stateArr[0])
    dealer_total = calculateTotal(stateArr[1])
    if len(stateArr[0]) == 2 and len(stateArr[1]) == 2:  # we both stand
        if player_total > dealer_total:
            return 1
        elif player_total < dealer_total:
            return 0
        else:
            return 0.5
    elif len(stateArr[0]) == 3 and len(stateArr[1]) == 2:  # we hit, they stand
        highCardToWin = 21 - player_total
        pointsToWin = dealer_total - player_total
        if pointsToWin <= 0:
            return 1
        return 1 * toWin(highCardToWin, pointsToWin, False)
    elif len(stateArr[0]) == 2 and len(stateArr[1]) == 3:  # we stand, they hit
        highCardToWin = 21 - dealer_total
        pointsToWin = player_total - dealer_total
        if pointsToWin <= 0:
            return 0
        return 1 * (1 - toWin(highCardToWin, pointsToWin, True))
    else:  # we hit, they hit

        if player_total == dealer_total:
            return 0.5
        elif player_total > dealer_total:
            difference = player_total - dealer_total
            percent = 1 - (difference / (21 - dealer_total))
            return 1 - 0.5 * percent
        else:
            difference = dealer_total - player_total
            percent = 1 - (difference / (21 - player_total))
            return 0.5 * percent

def toWin(highCardToWin, pointsToWin, includeTie):
    numerator = highCardToWin - pointsToWin
    denominator = highCardToWin
    if includeTie:
        numerator += 1
    if highCardToWin == 10:
        numerator += 3
        denominator += 3

    return numerator / denominator


def calculateTotal(handArr):
    total = 0
    numAces = 0
    for card in handArr:
        if card == "R":
            continue
        total += get_card_value(card)
        if card == "A":
            numAces += 1

    for i in range(numAces):
        if total > 21:
            total -= 10

    return total

def startAlgorithm(stateArr):
    otherStateArr = []
    for hand in stateArr:
        aHand = []
        for card in hand:
            aHand.append(card)
        otherStateArr.append(aHand)
    hit_return = placeOfBattle(stateArr, "hit")
    print(hit_return[0])
    print("\n")
    stand_return = placeOfBattle(otherStateArr, "stand")
    print(stand_return[0])
    if hit_return[0] > stand_return[0]:
        return hit_return
    else:
        return stand_return


def chanceOfLoss(hand):
    deck = ["2","2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6",
                 "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10",
                 "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
    """
    for card in hand:
        if card == "R":
            continue
        deck.remove(card)
    """

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
        stateArr[0].append("R")
        return_value = placeOfBattle(stateArr, "stand")
        return return_value[0] * chanceOfContinuing, ["hit"] + return_value[1]

    else:
        print("stand")
        if calculateTotal(stateArr[1]) >= 17:
            print("dealer stand")
            return score(stateArr), ["stand","stand"]
        else:
            print("dealer hit")
            stateArr[1].append("R")
            chanceOfLosing = chanceOfLoss(stateArr[1])
            chanceDealerWins = (1 - chanceOfLosing) * (1 - score(stateArr))
            return 1 - chanceDealerWins, ["stand", "hit"]



anArray = [["2","10"], ["7","10"]]
print(startAlgorithm(anArray))

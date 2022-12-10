#Our very awesome, amazing, intelligent ai blackjack bot


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

def chanceOfLoss(hand):
    deck = ["2","2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6",
                 "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10",
                 "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]

    moreThan = 0

    for card in deck:
        tempHand = hand.copy()
        tempHand.append(card)
        tots = calculateTotal(tempHand)
        if tots > 21:
            moreThan += 1

    return moreThan / len(deck)


#The score is determined based on the 2 possible options.
def toWin(pointsTo21, pointsToWin, includeTie):
    numerator = pointsTo21 - pointsToWin
    denominator = pointsTo21
    if includeTie:
        numerator += 1
    if pointsTo21 == 10:
        numerator += 3
        denominator += 3

    return numerator / denominator


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
    #seeing how many point we need to beat opponent to get closer to 21
    elif len(stateArr[0]) == 3 and len(stateArr[1]) == 2:  # we hit, they stand
        pointsTo21 = 21 - player_total
        pointsToWin = dealer_total - player_total
        if pointsToWin <= 0:
            return 1
        return 1 * toWin(pointsTo21, pointsToWin, False)
    elif len(stateArr[0]) == 2 and len(stateArr[1]) == 3:  # we stand, they hit
        pointsTo21 = 21 - dealer_total
        pointsToWin = player_total - dealer_total
        if pointsToWin <= 0:
            return 0
        return 1 * (1 - toWin(pointsTo21, pointsToWin, True))
    else:  # we hit, they hit

        if player_total == dealer_total:
            return 0.5
        elif player_total > dealer_total:
            difference = player_total - dealer_total
            percent = 1 - (difference / (21 - dealer_total))
            return 1 - 0.5 * percent
        else:
            #chance of going over the dealer total
            difference = dealer_total - player_total
            percent = 1 - (difference / (21 - player_total))
            return 0.5 * percent


#calculating the player's chance of winning based on the state and first action
def placeOfBattle(stateArr, action):
    if action == "hit":
        chanceOfContinuing = 1 - chanceOfLoss(stateArr[0])
        stateArr[0].append("R")
        return_value = placeOfBattle(stateArr, "stand")
        return return_value[0] * chanceOfContinuing, ["hit"] + return_value[1]

    else:
        if calculateTotal(stateArr[1]) >= 17:
            return score(stateArr), ["stand","stand"]
        else:
            stateArr[1].append("R")
            chanceOfDealerGoingOver21 = chanceOfLoss(stateArr[1])
            chanceDealerWins = (1 - chanceOfDealerGoingOver21) * (1 - score(stateArr))
            return 1 - chanceDealerWins, ["stand", "hit"]

def startAlgorithm(stateArr):
    otherStateArr = []
    for hand in stateArr:
        aHand = []
        for card in hand:
            aHand.append(card)
        otherStateArr.append(aHand)

    hit_return = placeOfBattle(stateArr, "hit")
    stand_return = placeOfBattle(otherStateArr, "stand")

    if hit_return[0] > stand_return[0]:
        return hit_return
    else:
        return stand_return


#we hit, they stand 
anArray = [["10","8"], ["10","R"]]
print(startAlgorithm(anArray))

"""
#we both stand
anArray = [["9","10"], ["7","10"]]
print(startAlgorithm(anArray))

#we stand, they hit
anArray = [["9","10"], ["3","10"]]
print(startAlgorithm(anArray))

#we both hit
anArray = [["4","8"], ["3","9"]]
print(startAlgorithm(anArray))

#testCases

"""


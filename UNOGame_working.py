#UNO Game from beginning

#Make a Deck Creator and compiler - DONE[X] Tested[X] Approved[X]
#Create a player class - DONE[X] Tested[X] Approved[X]
#Create a game class - DONE[] Tested[] Approved[]
#Colocar error handling nos inputs de utilizador - DONE[] Tested[] Approved[]

#1 -create deck - ok
#2 - create player - ok
#3 - give cards to players - ok
#4 - put first card on table - ok
#5 - starts the game player index0 (later will be player with lowest age)
#6 - Starts While Loop
#7 - Shows Table Card
#8 - Check card on table if it is actionCard and its effect
#9 - Say who is the player turn
#10 - Create a Players Turn Management based with the Movimntation (Reverse, skip) and considering the Index Out Of Range error since this is a list.
#10 - Show player Hand
#11 - Start Player Move
    #11.1 - check if move is possible against the table card.
#12 - in the end of each round, calculate the index with the playingOrder[-1] to calculate the index of the next player

import time  # use only for debugging
from random import shuffle
from operator import attrgetter

#Global Lists: - Approved []
Deck_Specials = ["Draw Two", "Reverse", "Skip", "Wild", "Wild Draw Four"]  # Implement maybe later...
Deck_Colors = ["|Red", "|Blu", "|Yel", "|Gre"]
ActionCard = ["|Gre Skip|", "|Blu Skip|", "|Red Skip|", "|Yel Skip|", "|Gre Reverse|", "|Blu Reverse|", "|Red Reverse|", "|Yel Reverse|", "|Gre Draw Two|", "|Blu Draw Two|", "|Red Draw Two|", "|Yel Draw Two|"]
WildCards = ["|Wild Draw Four|", "|Wild|"] #is Card Wild ??!!

#List of Decks:
Deck_CurrentGame = []
Deck_CurrentGame_Obj = []
Deck_TableDeck_Obj = []

#List Of Players and increments
Players_List = []
increment = [0]

#Global Variables:
playingOrder = 1
wildColor = "Undefined"
penaltySumDraw2 = 2
penaltySumDraw4 = 4

#Create Deck:
def createDeck():
    def createNumbersOnDeck(RangeMin, RangeMax, Ammount):  # Create Deck with numbers
        for i in range(RangeMin, RangeMax):
            for j in range(Ammount):
                for k in range(4):
                    Deck_CurrentGame.append(Deck_Colors[k] + "  " + str(i) + "|")
    def createActionCardsOnDeck(ACName, Ammount):  # Create Deck with Action Cards
        for i in range(Ammount):
            for k in range(4):
                Deck_CurrentGame.append(Deck_Colors[k] + " " + ACName + "|")
    def createWildCardsOnDeck(WCName, Ammount):  # Create Deck with Wild Cards
        for i in range(Ammount):
            Deck_CurrentGame.append("|" + WCName + "|")
    def compileDeck():  # Compiles all the previous functions and builds and shuffles a deck
        createNumbersOnDeck(0, 10, 2)  # Create Card "0" to "9" for each color
        createActionCardsOnDeck("Draw Two", 2)  # Create Action Cards
        createActionCardsOnDeck("Reverse", 2)  # Create Action Cards
        createActionCardsOnDeck("Skip", 2)  # Create Action Cards
        createWildCardsOnDeck("Wild", 5)  # Create Wild Cards
        createWildCardsOnDeck("Wild Draw 4", 5)  # Create Wild Cards
        shuffle(Deck_CurrentGame)  # Shuffle the deck
    compileDeck()

class Card:
    def __init__(self, name, color, number, isAction, actionType, isWild, wildType):
        # Card attributes
        self.name = name
        self.color = color
        self.number = number
        self.isAction = isAction
        self.actionType = actionType
        self.isWild = isWild
        self.wildType = wildType

#Define card attributes:
def cardAttrs(card, call_isCardWild=0, call_cardWildType=0, call_isCardAction=0, call_cardActionType=0, call_getCardColor=0, call_getCardNumber=0):
    def isCardWild(card):
        if card in WildCards:
            return True
        else:
            return False
    def cardWildType(card):
        if isCardWild(card) == True:
            if card == "|Wild|":
                type = "Wild"
                return type
            elif card == "|Wild Draw Four|":
                type = "Wild Draw Four"
                return type
        else:
            return False
    def isCardAction(card):
        if card in ActionCard:
            return True
        else:
            return False
    def cardActionType(card):
        if isCardAction(card) == True:
            type = "".join(char for char in card[5:-1:1])
            return type
        else:
            return False
    def getCardColor(card):
        if isCardWild(card) == True:
            color = wildColor
            return color
        else:
            color = "".join(char for char in card[1:4:1])
            return color
    def getCardNumber(card):
        if isCardWild(card) == True:
            return False
        elif isCardAction(card) == True:
            return False
        else:
            number = "".join(char for char in card[6:7:1])
            return number

    if call_isCardWild == 1:
        return isCardWild(card)
    elif call_cardWildType == 1:
        return cardWildType(card)
    elif call_isCardAction == 1:
        return isCardAction(card)
    elif call_cardActionType == 1:
        return cardActionType(card)
    elif call_getCardColor == 1:
        return getCardColor(card)
    elif call_getCardNumber == 1:
        return getCardNumber(card)

#Convert cards to object and append to new List
def convertCardToObject(originalDeck, objectDeck):
    idCount = 0
    for card in originalDeck: #Append each card as an object to a new deck
                                    #Card(name,color,number,isAction,actionType,isWild,wildType)
                                    #(card, call_isCardWild=0, call_cardWildType=0, call_isCardAction=0, call_cardActionType=0, call_getCardColor=0, call_getCardNumber=0)
        objectDeck.append(Card(card,cardAttrs(card, 0, 0, 0, 0, 1, 0),
                                    cardAttrs(card, 0, 0, 0, 0, 0, 1),
                                    cardAttrs(card, 0, 0, 1, 0, 0, 0),
                                    cardAttrs(card, 0, 0, 0, 1, 0, 0),
                                    cardAttrs(card, 1, 0, 0, 0, 0, 0),
                                    cardAttrs(card, 0, 1, 0, 0, 0, 0)))
        idCount += 1

#Class Player (Create Player):
class Player(Card):  # Define Players and Player Hand
    def __init__(self, playerID, playerName, playerAge, playerScore, mainDeck):
        self.playerID = playerID
        self.playerName = playerName
        self.playerAge = playerAge
        self.playerScore = playerScore
        self.mainDeck = mainDeck
        self.playerHand = []

    def setPlayerHand(self, Ammount):
        for i in range(Ammount):
            self.playerHand.append(self.mainDeck.pop(0))
    def showPlayerHand(self):
        count = 0
        time.sleep(1)
        print(self.playerName, "'s Hand:")
        for i in self.playerHand:
            print(count, " - ", i.name)
            count += 1
    def setPlayerID(self, playerID):
        self.playerID = playerID
    def setPlayerScore(self, score):
        self.playerScore = score

def createPlayer(mainDeck, playerlist):
    playersCount = int(input("Choose how many players will be playing (Max. 6): "))
    playerID = 0
    for player in range(playersCount):
        playerName = str(input("Player's Name: "))
        playerAge = int(input("Player's Age: "))
        playerlist.append(Player(playerID, playerName, playerAge, 0, mainDeck))
        playerID += 1

def lowestAge():
    Players_List.sort(key=lambda x: x.playerAge, reverse=False)
    x = 0
    for players in Players_List:
        players.playerID = x
        x += 1
    print("------ Player Starting the Round by Lowest age ------------------------")
    print(f"------------------- {Players_List[0].playerName} -----------------------------")
    print(" ----------------------------------------------------------------------")

#Moves
def playerHandToTable(move, playerIndex):
    actualPlayer = Players_List[playerIndex]
    Deck_TableDeck_Obj.insert(0, actualPlayer.playerHand[move])
    actualPlayer.playerHand.pop(move)
    print(f"{actualPlayer.playerName} played the card: {Deck_TableDeck_Obj[0].name}")

def deckToTable():
    Deck_TableDeck_Obj.insert(0, Deck_CurrentGame_Obj[-1])
    Deck_CurrentGame_Obj.pop(-1)

def seeCardOnTable():
    print("------------------------------------------------------")
    if Deck_TableDeck_Obj[0].name == "|Wild|":
        print(f"Card on the table is:\n{Deck_TableDeck_Obj[0].name} and the color choosed by last player is {Deck_TableDeck_Obj[0].color}\n")
    elif Deck_TableDeck_Obj[0].name == "|Wild Draw Four|":
        print(f"Card on the table is:\n{Deck_TableDeck_Obj[0].name} and the color choosed by last player is {Deck_TableDeck_Obj[0].color}\n")
    else:
        print(f"Card on the table is:\n{Deck_TableDeck_Obj[0].name}\n")

def chooseNewColor(playerIndex):
    global wildColor
    count = 0
    actualPlayer = Players_List[playerIndex]

    print(f"\n{actualPlayer.playerName} choose the color to next card: ")
    for color in Deck_Colors:
        print(count, " - ", color)
        count += 1
    userChoise = int(input("Color: "))
    wildColor = Deck_Colors[userChoise]
    Deck_TableDeck_Obj[0].color = wildColor
    print(f"Color choosed by {actualPlayer.playerName} for next round is {wildColor}")
    return wildColor

#Checks cards eligible play:
def checkActionCardsStartOfRound(playerIndex):
    actualPlayer = Players_List[playerIndex]
    global penaltySumDraw2
    global penaltySumDraw4

    if Deck_TableDeck_Obj[0].name == "Draw Two":
        #check if player has the Draw Two card present in hand and plays it.
        if Deck_TableDeck_Obj[0] in actualPlayer.playerHand:
            print("You have one 'Draw Two' card that you can play.")
            penaltySumDraw2 +=2
        else:
            print(f"OOPS!! Card on table is {Deck_TableDeck_Obj[0].name}, pick up {penaltySumDraw2} cards from the main deck!")
            actualPlayer.setPlayerHand(penaltySumDraw2)
            Deck_TableDeck_Obj[0].name == wildColor #This way, the next player wont end up in this function again...
            penaltySumDraw2 = 2
            return True #if return true, will move to next player in while loop. cant do it here.
    elif Deck_TableDeck_Obj[0].name == "Wild Draw Four":
        if Deck_TableDeck_Obj[0] in actualPlayer.playerHand:
            print("You have one 'Wild Draw Four' that you can play.")
            penaltySumDraw4 +=  4
        else:
            print(f"Someone is unlucky! {actualPlayer.playerName} pick up {penaltySumDraw4} cards from the main deck!")
            actualPlayer.setPlayerHand(penaltySumDraw4)
            Deck_TableDeck_Obj[0].name == wildColor #This way, the next player wont end up in this function again...
            penaltySumDraw4 = 4
            return True #if return true, will move to next player in while loop. cant do it here.

def checkActionCardsEndOfRound(playerIndex):
    global playingOrder

    if Deck_TableDeck_Obj[0].isAction == True:
        if Deck_TableDeck_Obj[0].actionType == "Skip":
            print("Will skip to the next Player!")
            nextPlayer(playerIndex, increment, playingOrder, True)
        elif Deck_TableDeck_Obj[0].actionType == "Reverse":
            if playingOrder == 1:
                print("Will Reverse the Playing Order.")
                playingOrder = -1
                nextPlayer(playerIndex, increment, playingOrder)
            elif playingOrder == -1:
                print("Will Reverse the Playing Order.")
                playingOrder = 1
                nextPlayer(playerIndex, increment, playingOrder)
    elif Deck_TableDeck_Obj[0].isWild == True:
        if Deck_TableDeck_Obj[0].wildType == "Wild":
            chooseNewColor(playerIndex)
        elif Deck_TableDeck_Obj[0].wildType == "Wild Draw Four":
            chooseNewColor(playerIndex)

def checkCardPlay(playerIndex, move):
    actualPlayer = Players_List[playerIndex]

    if actualPlayer.playerHand[move].color == Deck_TableDeck_Obj[0].color:
        playerHandToTable(move, playerIndex)
        time.sleep(2)
    elif actualPlayer.playerHand[move].number == Deck_TableDeck_Obj[0].number:
        playerHandToTable(move, playerIndex)
        time.sleep(2)
    elif actualPlayer.playerHand[move].isWild:
        playerHandToTable(move, playerIndex)
        time.sleep(2)
    else:
        print("You failed the move, go draw 1 card.")
        time.sleep(2)
        actualPlayer.setPlayerHand(1)
        print(f"You draw 1 card from the deck. Is the card {actualPlayer.playerHand[-1].name}.")
        time.sleep(2)
        if actualPlayer.playerHand[-1].color == Deck_TableDeck_Obj[0].color:
            userChoise = input("You got a compatible card! Want to use it now? (y/n)")
            if userChoise == "y":
                playerHandToTable(-1, playerIndex)
            else:
                print("Moving to next Player")
                nextPlayer(playerIndex, increment, playingOrder)
        elif actualPlayer.playerHand[-1].number == Deck_TableDeck_Obj[0].number:
            userChoise = input("You got a compatible card! Want to use it now? (y/n)")
            if userChoise == "y":
                playerHandToTable(-1, playerIndex)
            else:
                print("Moving to next Player")
                nextPlayer(playerIndex, increment, playingOrder)
        elif actualPlayer.playerHand[-1].isWild == True:
            userChoise = input("You got a compatible card! Want to use it now? (y/n)")
            if userChoise == "y":
                playerHandToTable(-1, playerIndex)
            else:
                print("Moving to next Player")
                nextPlayer(playerIndex, increment, playingOrder)
        else:
            print("The card you picked up is not eligible neither... Moving to Next Player.")
            nextPlayer(playerIndex, increment, playingOrder)

#Player Turns:
def nextPlayer(actualPlayer, increment, playingOrder, skip=False):
    lenOfList = len(Players_List)
    # non reverse
    if playingOrder == 1:
        if skip == True:
            if actualPlayer == len(Players_List)-1:
                actualPlayer = 0
                increment.append(0)
                return actualPlayer
            else:
                increment.append(2)
                print(increment)
                print(Players_List[actualPlayer].playerID)
                print(increment[-1])
                actualPlayer = Players_List[actualPlayer].playerID + increment[-1]
                print(actualPlayer)
                return actualPlayer
        else:
            if actualPlayer == len(Players_List)-1:
                actualPlayer = 0
                increment.append(0)
                return actualPlayer
            else:
                increment.append(1)
                actualPlayer = Players_List[actualPlayer].playerID + increment[-1]
                return actualPlayer
    # reverse order
    elif playingOrder == -1:
        if skip == True:
            if actualPlayer == (lenOfList*-1)+1:
                actualPlayer = 0
                increment.append(0)
                return actualPlayer
            else:
                increment.append(-1)
                actualPlayer = Players_List[actualPlayer].playerID + increment[-1]
                return actualPlayer
        else:
            if actualPlayer == (lenOfList * -1) + 1:
                actualPlayer = 0
                increment.append(0)
                return actualPlayer
            else:
                increment.append(-1)
                actualPlayer = Players_List[actualPlayer].playerID + increment[-1]
                return actualPlayer
    #actualPlayer não está a ser devolvido. Verificar Porque

def setUpGame(): #Setup the Decks, players, etc
    #First - Deck Build:
    createDeck()
    convertCardToObject(Deck_CurrentGame, Deck_CurrentGame_Obj)
    #Second - Create Players:
    createPlayer(Deck_CurrentGame_Obj, Players_List)
    #Third - Give Cards to Players:
    for player in Players_List: player.setPlayerHand(7)
    #Fourth - Put card on table:
    deckToTable()
    #Seventh - Select first player to play by Age
    lowestAge() # = index[0]
    #Fifth - See card on table:
    seeCardOnTable() #Setup

def firstMove():
    global actualPlayer

    Players_List[actualPlayer].showPlayerHand()
    move = int(input("Make your move: "))
    if checkActionCardsStartOfRound(actualPlayer) == True:
        nextPlayer(actualPlayer, increment, playingOrder)
    checkCardPlay(actualPlayer, move)
    checkActionCardsEndOfRound(actualPlayer)
    actualPlayer = nextPlayer(actualPlayer, increment, playingOrder)
    seeCardOnTable()
#--------------------------------------------------------------------------------------------------------------------
actualPlayer = 0
setUpGame()
firstMove()

while(True):
    print(f"Player's Turn: {Players_List[actualPlayer].playerName}")
    Players_List[actualPlayer].showPlayerHand()
    move = int(input("Select a card to Play: "))
    if checkActionCardsStartOfRound(actualPlayer) == True:
        actualPlayer = nextPlayer(actualPlayer, increment, playingOrder)
        continue
    checkCardPlay(actualPlayer, move)
    checkActionCardsEndOfRound(actualPlayer)

    actualPlayer = nextPlayer(actualPlayer, increment, playingOrder)
    seeCardOnTable()

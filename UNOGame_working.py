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

# ----------- Global Lists: - Approved []
Deck_Specials = ["Draw Two", "Reverse", "Skip", "Wild", "Wild Draw Four"]  # Implement maybe later...
Deck_Colors = ["|Red", "|Blu", "|Yel", "|Gre"]
ActionCard = ["|Gre Skip|", "|Blu Skip|", "|Red Skip|", "|Yel Skip|", "|Gre Reverse|", "|Blu Reverse|", "|Red Reverse|", "|Yel Reverse|", "|Gre Draw Two|", "|Blu Draw Two|", "|Red Draw Two|", "|Yel Draw Two|"]
WildCards = ["|Wild Draw Four|", "|Wild|"]
Deck_CurrentGame = []
Deck_CurrentGame_Obj = []
Deck_TableDeck_Obj = []
Players_List = []
increment = [0]
playingOrder = 1
wildColor = "Blue"

# ----------- Create Deck:
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
        createActionCardsOnDeck("Draw 2", 2)  # Create Action Cards
        createActionCardsOnDeck("Reverse", 2)  # Create Action Cards
        createActionCardsOnDeck("Skip", 2)  # Create Action Cards
        createWildCardsOnDeck("Wild", 5)  # Create Wild Cards
        createWildCardsOnDeck("Wild Draw 4", 5)  # Create Wild Cards
        shuffle(Deck_CurrentGame)  # Shuffle the deck
    compileDeck()

class Card:
    def __init__(self, name, cardID, color, number, isAction, actionType, isWild, wildType):
        # Card attributes
        self.cardID = cardID
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
    def isCardAction(card):
        if card in ActionCard:
            return True
        else:
            return False
    def cardActionType(card):
        if isCardAction(card) == True:
            type = "".join(char for char in card[5:-1:1])
            return type
    def getCardColor(card):
        if isCardWild(card) == True:
            color = wildColor
            return color
        else:
            color = "".join(char for char in card[1:4:1])
            return color
    def getCardNumber(card):
        if isCardWild(card) or isCardAction(card):
            number = None
            return number
        else:
            number = "".join(char for char in card[5:6:1])
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
                                    #Card(name,cardID,color,number,isAction,actionType,isWild,wilsType)
                                    #(card, call_isCardWild=0, call_cardWildType=0, call_isCardAction=0, call_cardActionType=0, call_getCardColor=0, call_getCardNumber=0)
        objectDeck.append(Card(card, idCount,
                                    cardAttrs(card, 0, 0, 0, 0, 1, 0),
                                    cardAttrs(card, 0, 0, 0, 0, 0, 1),
                                    cardAttrs(card, 0, 0, 1, 0, 0, 0),
                                    cardAttrs(card, 0, 0, 0, 1, 0, 0),
                                    cardAttrs(card, 1, 0, 0, 0, 0, 0),
                                    cardAttrs(card, 0, 1, 0, 0, 0, 0)))
        idCount += 1

# ----------- Class Player (Create Player):
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
            self.playerHand[i].cardID = i #set the card with the cardID = to the index in this list.
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

# --------- Moves
def playerHandToTable(move, playerIndex):
    actualPlayer = Players_List[playerIndex]
    Deck_TableDeck_Obj.insert(0, actualPlayer.playerHand[move])
    actualPlayer.playerHand.pop(move)
    print(f"{actualPlayer.playerName} played the card: {Deck_TableDeck_Obj[0].name}")

def deckToTable():
    Deck_TableDeck_Obj.insert(0, Deck_CurrentGame_Obj[-1])
    Deck_CurrentGame_Obj.pop(-1)

def seeCardOnTable():
    print(f"Card on the table is:\n{Deck_TableDeck_Obj[0].name}")

def chooseNewColor(playerIndex):
    global wildColor
    count = 0
    actualPlayer = Players_List[playerIndex]
    print(f"{actualPlayer.playerName} choose the color for the next round:")
    for color in Deck_Colors:
        print(count, " - ", color)
        count += 1
    userChoise = input("Choose the color to next card: ")
    wildColor = Deck_Colors[userChoise]

#---------- Checks cards eligible play:
def checkActionCardsStartOfRound(playerIndex):
    actualPlayer = Players_List[playerIndex]
    if Deck_TableDeck_Obj[0].name == "Draw Two":
        print(f"OOPS!! Card on table is {Deck_TableDeck_Obj[0].name}, pick up 2 cards from the main deck! :p")
        actualPlayer.setPlayerHand(2)
        Deck_TableDeck_Obj[0].name == wildColor #This way, the next player wont end up in this function again...
        return True #if return true, will move to next player in while loop. cant do it here.

    elif Deck_TableDeck_Obj[0].name == "Wild Draw Four":
        print(f"Someone is unlucky! {actualPlayer.playerName} pick up 4 cards from the main deck!")
        actualPlayer.setPlayerHand(4)
        Deck_TableDeck_Obj[0].name == wildColor #This way, the next player wont end up in this function again...
        return True #if return true, will move to next player in while loop. cant do it here.

def checkActionCardsEndOfRound(playerIndex):
    if Deck_TableDeck_Obj[0].isAction == True:
        if Deck_TableDeck_Obj[0].actionType == "Skip":
            print("Will skip to the next Player!")
            nextPlayer(playerIndex, increment)
        elif Deck_TableDeck_Obj[0].actionType == "Reverse":
            print("Will Reverse the Playing Order.")
            playingOrder = -1
            nextPlayer(playerIndex, increment, playingOrder)
        elif Deck_TableDeck_Obj[0].actionType == "Wild":
            chooseNewColor(playerIndex)
        elif Deck_TableDeck_Obj[0].actionType == "Wild Draw Four":
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
        print("You don't have cards to play, go draw 1.")
        time.sleep(2)
        actualPlayer.setPlayerHand(1)
        print(f"You draw 1 card from the deck. Is the card {actualPlayer.playerHand[-1].name}.")
        time.sleep(2)
        move = actualPlayer.playerHand[-1].cardID
        if actualPlayer.playerHand[move].color == Deck_TableDeck_Obj[0].color:
            playerHandToTable(move, playerIndex)
        elif actualPlayer.playerHand[move].number == Deck_TableDeck_Obj[0].number:
            playerHandToTable(move, playerIndex)
        elif actualPlayer.playerHand[move].isWild:
            playerHandToTable(move, playerIndex)
        else:
            print("The card you picked up is not eligible neither... Moving to Next Player.")
            nextPlayer(playerIndex, increment)

#---------- Player Turns:
def nextPlayer(actualPlayer, increment, playingOrder):
    if playingOrder == 1: #non reverse
        if actualPlayer == len(Players_List)-1:
            actualPlayer = 0
            increment.append(0)
            return actualPlayer
        else:
            increment.append(1)
            actualPlayer = Players_List[actualPlayer].playerID + increment[-1]
            return actualPlayer
    elif playingOrder == -1: #reverse order
        lenOfList = len(Players_List)
        if actualPlayer == (lenOfList*-1)+1:
            actualPlayer = 0
            increment.append(0)
            return actualPlayer
        else:
            increment.append(-1)
            actualPlayer += increment[-1]
            return actualPlayer

#-----------------------------------------------------------------------------------------------------------------------
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
seeCardOnTable()

#--------------------------------------------------------------------------------------------------------------------
actualPlayer = 0
count = 0

#First Move:
Players_List[actualPlayer].showPlayerHand()
move = int(input("Make your move: "))
if checkActionCardsStartOfRound(actualPlayer) == True:
    nextPlayer(actualPlayer, increment, playingOrder)
checkCardPlay(actualPlayer, move)
checkActionCardsEndOfRound(actualPlayer)

actualPlayer = nextPlayer(actualPlayer, increment, playingOrder)

while(count < 10):
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

    #Não está a mudar de player n tinha a variavel actualplayer associada á função: CORRECTED!
    #caso a carta jogada não cumpra com os requisitos ela é jogada a mesma
    #skip n funciona

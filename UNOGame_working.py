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

# ----------- Create Deck: - Approved []
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
            color = None
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

# ----------- Class Player (Create Player): - Approved []
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
    y = 100
    z = 0
    for player in range(len(Players_List)):
        if Players_List[player].playerAge < y:
            y = Players_List[player].playerAge
            z = Players_List[player]
    print(f"{z.playerName}, starts the game because has the lowest age.")
    return z

# --------- Moves
def playerHandToTable(move, Player):
    Deck_TableDeck_Obj.insert(0, Player.playerHand[move])
    Player.playerHand.pop(move)
    print(f"{Player.playerName} played the card: {Deck_TableDeck_Obj[0].name}")

def deckToTable():
    Deck_TableDeck_Obj.insert(0, Deck_CurrentGame_Obj[-1])
    Deck_CurrentGame_Obj.pop(-1)

def seeCardOnTable():
    print(f"\nCard on table is:\n{Deck_TableDeck_Obj[0].name}\n")

#---------- Checks cards eligible play:
def checkActionCardsStartOfRound(Player):
    if Deck_TableDeck_Obj[0].name == "Draw Two":
        print(Player.playerName, " pick up 2 cards from the main deck! :p")
        Player.setPlayerHand(2)
        return True


def checkActionCardsEndOfRound(Player, turn):
    if Deck_TableDeck_Obj[0].isAction == True:
        if Deck_TableDeck_Obj[0].actionType == "Skip":
            print("Will skip the next Player!")
            playerTurn += 1
        elif Deck_TableDeck_Obj[0].actionType == "Reverse":
            print("Will Reverse the Playing Order.")
            playingOrder.append[-1]


def checkCardPlay(Player, move):
    if Player.playerHand[move].color == Deck_TableDeck_Obj[0].color:
        playerHandToTable(move, Player)
        print(f"{Player.playerName} played the card {Deck_TableDeck_Obj[0].name}")
        time.sleep(2)
    elif Player.playerHand[move].number == Deck_TableDeck_Obj[0].number:
        playerHandToTable(move, Player)
        print(f"{Player.playerName} played the card {Deck_TableDeck_Obj[0].name}")
        time.sleep(2)
    elif Player.playerHand[move].isWild:
        playerHandToTable(move, Player)
        print(f"{Player.playerName} played the card {Deck_TableDeck_Obj[0].name}")
        time.sleep(2)
    else:
        print("You don't have cards to play, go draw 1.")
        time.sleep(2)
        Player.setPlayerHand(1)
        print(f"You draw 1 card from the deck. Is the card {Player.playerHand[-1].name}.")
        time.sleep(2)
        move = Player.playerHand[-1].cardID
        if Player.playerHand[move].color == Deck_TableDeck_Obj[0].color:
            playerHandToTable(move, Player)
            print(f"{Player.playerName} played the card {Deck_TableDeck_Obj[0].name}")
        elif Player.playerHand[move].number == Deck_TableDeck_Obj[0].number:
            playerHandToTable(move, Player)
            print(f"{Player.playerName} played the card {Deck_TableDeck_Obj[0].name}")
        elif Player.playerHand[move].isWild:
            playerHandToTable(move, Player)
            print(f"{Player.playerName} played the card {Deck_TableDeck_Obj[0].name}")
        else:
            print("The card you picked up is not eligible neither... Moving to Next Player.")

#---------- PlayingOrder & Turns:
def game(actualPlayer, increment):
    if playingOrder == 1:
        try:
            increment.append(1)
            actualPlayer = Players_List[actualPlayer.playerID + increment[-1]]
            return actualPlayer
        except IndexError:
            indexError(increment, actualPlayer)
    elif playingOrder == -1:
        try:
            increment.append(-1)
            actualPlayer += increment[-1]
            return actualPlayer
        except IndexError:
            indexError(increment, actualPlayer)

def indexError(increment,actualPlayer):
    lenOfList = len(Players_List)
    #check if it is in reverse mode:
    if increment[-1] == -1:
        print(lenOfList*-1)
        if actualPlayer == (lenOfList*-1)-1:
            actualPlayer = lenOfList-1
            increment.append(0)
            game(actualPlayer, increment)
    elif increment[-1] == 1:
        if actualPlayer == lenOfList:
            actualPlayer = 0
            increment.append(0)
            game(actualPlayer, increment)

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
#Fifth - See card on table:
seeCardOnTable()
#Seventh - Select first player to play by Age
lowestAge()

#-----------------------------------------------------------------------------------------------------------------------
actualPlayer = lowestAge()#atualplayer will be an int number only to make the index.
while(True):
    if checkActionCardsStartOfRound(actualPlayer) == True:
        checkActionCardsStartOfRound(actualPlayer)
        #move to next round
        game(actualPlayer, increment)
    else:
        actualPlayer.showPlayerHand()
        #Change player (Missing a way of turning back to this loop)
        move = int(input("Select a card to Play: "))
        #Check if move is valid:
        checkCardPlay(actualPlayer, move)
        game(actualPlayer, increment)



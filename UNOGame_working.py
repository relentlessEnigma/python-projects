#UNO Game from beginning


#Make a Deck Creator and compiler - DONE[X] Tested[X] Approved[X]
#Create a player class - DONE[X] Tested[X] Approved[X]
#Create a game class - DONE[] Tested[] Approved[]
#Colocar error handling nos inputs de utilizador - DONE[] Tested[] Approved[]

from random import shuffle
import time  # use only for debugging

# ----------- Global Lists: - Approved []
Deck_Specials = ["Draw Two", "Reverse", "Skip", "Wild", "Wild Draw Four"]  # Implement maybe later...
Deck_Colors = ["|Red", "|Blu", "|Yel", "|Gre"]
Deck_CurrentGame = []
Deck_TableDeck = []
Players_List = []
playingOrder = [1]
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

# ----------- Class Player (Create Player): - Approved []
class Player:  # Define Players and Player Hand
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
        count = 1
        time.sleep(1)
        print(self.playerName, "'s Hand:")
        for i in self.playerHand:
            print(count, " - ", i)
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
    Deck_TableDeck.insert(0, Player.playerHand[move])
    Player.playerHand.pop(move)
    print(Player.playerName, " played the card: ", Deck_TableDeck[0])

def deckToTable():
    Deck_TableDeck.insert(0, Deck_CurrentGame[-1])
    Deck_CurrentGame.pop(-1)

def seeCardOnTable():
    print("\nCard on table is:\n", Deck_TableDeck[0], "\n")

#---------- Checks cards eligible play:
def checkActionCardsStartOfRound(Player):
    if Deck_TableDeck[0] == "Wild Draw Four":
        print(f"{Player.playerName} picked up 4 cards from the main deck. Cant play this turn, sorry!")
        Player.setPlayerHand(4)
        return True
    elif Deck_TableDeck[0] == "Draw Two":
        print(Player.playerName, " pick up 2 cards from the main deck! :p")
        Player.setPlayerHand(2)
        return True

def checkActionCardsEndOfRound(): #Check first special cards
    if Deck_TableDeck[0] == "Reverse":
        if playingOrder[-1] == -1:
            playingOrder.append(1)
        else:
            playingOrder.append(-1)
    elif Deck_TableDeck[0] == "Skip":
        if playingOrder[-1] == -1:
            playingOrder[-1] == -2
        else:
            playingOrder[-1] == 2

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def checkCardNumber(Player):
    for tableCard in Deck_TableDeck[0]:
        if has_numbers(tableCard) == True:
            cardNumberOnTable = tableCard
            for playerCard in Player.playerHand:
                if has_numbers(playerCard) == True:
                    cardNumberOnPlayerHand = playerCard
                    if cardNumberOnPlayerHand == cardNumberOnTable:
                        return True

def checkCardColor(Player):
    for color in Deck_Colors:
        if color in Deck_TableDeck[0]:
            tableCardColor = color
    for playerCard in Player.playerHand:
        for color in Deck_Colors:
            if color in playerCard:
                if color == tableCardColor:
                    return True

def playerMove():
    playerTurn.showPlayerHand()
    move = input("Select the card you want to play: ")
    if checkCardNumber() == True:
        #Falta check para confirmar a carta q o jogador quer jogar vs a que esta na mesa.

    return move


#1 -create deck - ok
#2 - create player - ok
#3 - give cards to players - ok
#4 - put first card on table - ok
#5 - starts the game player index0 (later will be player with lowest age)
#6 - Starts While Loop
#7 - Shows Table Card
#8 - Check card on table if it is actionCard and its effect
#9 - Say who is the player turn
#10 - Show player Hand
#11 - Start Player Move
    #11.1 - check if move is possible against the table card.
#12 - in the end of each round, calculate the index with the playingOrder[-1] to calculate the index of the next player

createDeck() #1
createPlayer(Deck_CurrentGame, Players_List) #2
for player in Players_List: player.setPlayerHand(7) #3
deckToTable() #4
lowestAge() #5

startingPlayer = 0
playerTurn = Players_List[startingPlayer]

while(True):
    seeCardOnTable()
    print(f"Player Turn: {playerTurn.playerName}")
    if checkActionCardsStartOfRound(playerTurn) == True:
        playerTurn += playingOrder[-1]
        playerMove()
        continue
    playerMove()
    checkActionCardsEndOfRound()

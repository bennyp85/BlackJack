import random

class Game:
  def __init__(self, playerScore=None, dealerScore=None):
    self.playerScore = playerScore
    self.dealerScore = dealerScore

  def WhoWon(self):
    if self.playerScore > self.dealerScore and self.playerScore <= 21:
      return "Player Won"
    else:
      return "Dealer Won"

class Player:
  def __init__(self, score=None):
    self.score = score

  def PlayerScore(self):
    score = input("Player Card Count: ")
    return int(score)

  def GetScore(self):
    pass

  def SetScore(self, deck):
    self.score = deck.GetCard()
    return self.score[1]
    
class Dealer:
  def __init__(self, score=None):
    self.score = score

  def DealerScore(self):
    score = input("Dealer Card Count: ")
    return int(score)

  def GetScore(self):
    pass

  def SetScore(self, deck):
    self.score = deck.GetCard()
    return self.score[1]

class Deck:
  cards = {
    "AceH": [1, 11],
    "AceD": [1, 11],
    "AceC": [1, 11],
    "AceS": [1, 11],
    "KingH": 10,
    "KingD": 10,
    "KingC": 10,
    "KingS": 10,
    "QueenH": 10,
    "QueenD": 10,
    "QueenC": 10,
    "QueenS": 10,
    "JackH": 10,
    "JackD": 10,
    "JackS": 10,
    "JackC": 10,
    "9H": 9, 
    "9D": 9, 
    "9S": 9, 
    "9C": 9, 
    "8H": 8,
    "8D": 8, 
    "8S": 8, 
    "8C": 8,
    "7H": 7,
    "7D": 7,
    "7S": 7,
    "7C": 7,
    "6H": 6,
    "6D": 6,
    "6S": 6,
    "6C": 6,
    "5H": 5,
    "5D": 5,
    "5S": 5,
    "5C": 5,
    "4H": 4,
    "4D": 4,
    "4S": 4,
    "4C": 4,
    "3H": 3,
    "3D": 3,
    "3S": 3,
    "3C": 3,
    "2H": 2, 
    "2D": 2, 
    "2S": 2, 
    "2C": 2
  }

  def GetCard(self):
    card = random.choice(list(Deck.cards.items()))
    Deck.cards.pop(card[0])
    return card
    
deck = Deck()

player = Player()
pScore = player.SetScore(deck)
print("Player Card: " + str(pScore))

dealer = Dealer()
dScore = dealer.SetScore(deck)
print("Dealer Card: " + str(dScore))

game = Game(pScore, dScore)
print(game.WhoWon())
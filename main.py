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
    
class Dealer:
  def __init__(self, score=None):
    self.score = score

  def DealerScore(self):
    score = input("Dealer Card Count: ")
    return int(score)

class Deck:
  pass

player = Player()
pScore = player.PlayerScore()

dealer = Dealer()
dScore = dealer.DealerScore()

game = Game(pScore, dScore)
print(game.WhoWon())
import random
from square import SquareAbstract
from square import Square

class Game(SquareAbstract):
              
  def __init__(self):
    SquareAbstract.__init__(self)
    
    #add count square to gmae
    for sqc in xrange(0,9):
      x,y = self.getFreeSlot()
      square = Square(self,x,y)
      self.set(x,y,square)
  
  #calculate count of all possible numbers, which may be entered in a certian field
  def calculatePossible(self):
    for x in xrange(0,3):
      for y in xrange(0,3):
        self.fields[x][y].calculatePossible()
  
  #solve that current state (is it even solvable?)
  def solve(self):
    pass
  
  #print out representation of square
  def __repr__(self):
    repr = ""
    for x in xrange(0,3):
      for xSquare in xrange(0,3):
        for y in xrange(0,3):
          square = self.fields[x][y]
          for ySquare in xrange(0,3):
            if square is None:
              repr += "- (-)"
            else:
              number = square.fields[xSquare][ySquare]
              if number is not None:
                repr += str(number)
              else:
                repr += "-"
              possible = square.possible[xSquare][ySquare]
              if possible is not None:
                repr += " (" + str(possible) + ")"
              else:
                repr += " (-)"
            repr += " "
          repr += " "
        repr += "\n"
      repr += "\n"
    return repr
            
      
if __name__ == '__main__':
  game = Game()
  
  #play it :)
  item = game.fields[0][0]
  item.set(0,0,1)
  item.set(0,1,1) #will not be succesfull
  item.set(0,1,2)
  
  item = game.fields[2][2]
  item.set(2,2,2)

  item = game.fields[0][2]
  item.set(2,2,6)
  
  item = game.fields[1][1]
  item.set(1,1,7)
  
  game.calculatePossible()
  
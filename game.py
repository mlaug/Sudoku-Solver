import random
import sys
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

  def solve(self):
  
    while not self.solved():
      next = {0 : None, 1 : None, 2 : None, 3 : None}
      currentPossible = 0
      for x in xrange(0,3):
        for y in xrange(0,3):
          square = self.fields[x][y]
          for xf in xrange(0,3):
            for yf in xrange(0,3):
              if square.fields[xf][yf] is None: #field should
                possible = square.possible[xf][yf]
                if possible is not None and possible > currentPossible:
                  next[0] = x
                  next[1] = y
                  next[2] = xf
                  next[3] = yf
      
      if next[0] is None:
        print "running in deadlock"
        print repr(self)
        sys.exit(1)
      
      item = self.fields[next[0]][next[1]]
      bestsol = 0
      bestnum = None
      for testnumber in xrange(1,10):
        if item.set(next[2],next[3],testnumber): #must be true, so that this move is allowed
          testsol = self.weighting()
          if testsol > bestsol:
            bestsol = testsol
            bestnum = testnumber
          item.set(next[2],next[3],None) #reset for next loop
          print repr(self)
      
      if bestnum is None:
        print "running in deadlock"
        print repr(self)
        sys.exit(1)
      
      #set found number
      item.set(next[2],next[3],bestnum)
    
    print "solved"
    repr(self)

  def solved(self):
    for x in xrange(0,3):
      for y in xrange(0,3):
        square = self.fields[x][y]
        for xf in xrange(0,3):
          for yf in xrange(0,3):
            if square.fields[xf][yf] is None:
              return False
    return True

  def weighting(self):
    weight = 0
    for x in xrange(0,3):
      for y in xrange(0,3):
        square = self.fields[x][y]
        for xf in xrange(0,3):
          for yf in xrange(0,3):
            possible = square.possible[xf][yf]
            if possible is None:
              weight += 9
            else:
              weight += possible
    return weight
  
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
  game.calculatePossible()
  game.solve()
  
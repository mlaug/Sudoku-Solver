#solver
import random

class SquareAbstract(object):
  
  def __init__(self):
    self.fields = {0 : {0 : None, 1 : None, 2 : None}, 
                   1 : {0 : None, 1 : None, 2 : None}, 
                   2 : {0 : None, 1 : None, 2 : None}}
  
  #get a random free slot in fields
  def getFreeSlot(self):
    x = 0
    y = 0
    while self.fields[x][y] is not None:
      x = random.randrange(0,3);
      y = random.randrange(0,3);
    return x,y
  
  #set an item
  def set(self,x,y,item):
    #must be a valid range
    if x > 2 or x < 0 or y > 2 or y < 0:
      return False
    self.fields[x][y] = item
    return True
    
class Square(SquareAbstract):

  setItems = 0
  
  #create first set
  def __init__(self, game, x, y):
    self.possible = {0 : {0 : None, 1 : None, 2 : None}, 
                     1 : {0 : None, 1 : None, 2 : None}, 
                     2 : {0 : None, 1 : None, 2 : None}}
    SquareAbstract.__init__(self)
    self.needToSet = set([1,2,3,4,5,6,6,7,8,9])
    self.alreadySet = set()
    self.game = game
    
    #position on the game field
    self.x = x
    self.y = y
    
  #set an item
  def set(self,x,y,number):
    #must be a valid range
    if x > 2 or x < 0 or y > 2 or y < 0:
      return False
    if not self.validate(x,y,number):
      return False
    
    if self.fields[x][y] is not None:
      self.alreadySet.remove(self.fields[x][y])
      self.needToSet.add(self.fields[x][y])
      
    self.fields[x][y] = number
    self.alreadySet.add(number)
    self.needToSet.remove(number)
    
    self.game.calculatePossible()
    return True
  
  #is this move allowed
  def validate(self,x,y,number):
    return set([number]).issubset(self.getPossibleNumbers(x,y))
  
  #get possible numbers for this field
  def getPossibleNumbers(self,x,y):
    #lookup x and y axis
    possible = self.needToSet.copy()
    
    #x axis
    for xSquare in xrange(0,3):
      #get neightbour square field
      square = self.game.fields[xSquare][self.y]
      for xField in xrange(0,3):
        number = square.fields[xField][y]
        if number is not None:
          try:
            possible.remove(number)
          except KeyError:
            pass
            
    #y axis
    for ySquare in xrange(0,3):
      #get neightbour square field
      square = self.game.fields[self.x][ySquare]
      for yField in xrange(0,3):
        number = square.fields[x][yField]
        if number is not None:
          try:
            possible.remove(number)
          except KeyError:
            pass
    
    return possible
  
  #calculate all fields
  def calculatePossible(self):
    for x in xrange(0,3):
      for y in xrange(0,3):
        self.possible[x][y] = len(self.getPossibleNumbers(x,y))
      
        
    
  
  
  
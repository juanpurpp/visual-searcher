import copy

class Node:
  def __init__(self, state, father, last_branch):
    self.state = state[:]
    self.father = father
    self.last_branch = last_branch
  def getState(self):
    return copy.deepcopy(self.state)
  
  def getFather(self):
    return self.father
  
  def getPositionCoords(self):
    for i, row in enumerate(self.state):
      for j, value in enumerate(row):
        if value == 'i': return [i,j]
    return 0
  
  def movementDoesntBreakRules(self, newRow, newCol):
    if newRow < 0: return False
    if newCol < 0: return False
    if newRow >= len(self.state): return False
    if newCol >= len(self.state[0]): return False
    if self.state[newRow][newCol] == 0: return False
    return True
  
  def getNewStateFromMovement(self, newRow, newCol):
    row, col = self.getPositionCoords() # coords of current position
    new_state = copy.deepcopy(self.state)
    new_state[row][col] = 1 #free block
    new_state[newRow][newCol] = 'i'
    return new_state

  def getChoices(self):
    row, col = self.getPositionCoords()
    children = []
    #up
    if self.movementDoesntBreakRules(row - 1, col):
      children.append(self.getNewStateFromMovement(row -1, col))
    #right
    if self.movementDoesntBreakRules(row, col+1):
      children.append(self.getNewStateFromMovement(row, col+1))
    #down
    if self.movementDoesntBreakRules(row + 1, col):
      children.append(self.getNewStateFromMovement(row + 1, col))
    #left
    if self.movementDoesntBreakRules(row, col-1):
      children.append(self.getNewStateFromMovement(row, col-1))
    return children
  
  def isGoal(self, goal_coords):
    goal_row, goal_col = goal_coords
    if self.state[goal_row][goal_col] == 'i': return True
    else: return False

  def getLastBranch(self):
    return self.last_branch
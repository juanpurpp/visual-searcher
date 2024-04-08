from searcher.Node import Node
import time
import sys
import asyncio
from searcher.Event import Event
from reactpy import hooks, component
class Searcher:
  def __init__(self, problem):
    sys.setrecursionlimit(2500)
    self.iteration = Event()
    def getGoalCoords():
      for i, row in enumerate(problem):
        for j, value in enumerate(row):
          if value == 'g': return [i,j]
      return 0

    self.current = Node(problem[:], None, None)
    self.goal_coords = getGoalCoords()

  async def startRecursiveDepth(self,node):
    await self.iteration.trigger([node.getState()])
    if node.isGoal(self.goal_coords): return node
    choices = node.getChoices()
    for choice in choices:
      result = await self.startRecursiveDepth(Node(choice, node, node if len(choices)>1 else None))
      if result != 0 : return result
    return 0
  
  def isIdentical(self,A,B):
    for i, row in enumerate(A):
      for j, val in enumerate(row):
        if A[i][j] != B[i][j]: return False
    return True
  
  def isSaved(self,saved, B):
    for A in saved:
      if self.isIdentical(A,B): return True
    return False
  
  async def startLinearDepth(self,node):
    stack = []
    saved = []
    current = Node(node.getState(), None, None)
    while not current.isGoal(self.goal_coords):
      await self.iteration.trigger([current.getState()])
      print('save1')
      print(saved)
      print('to saves')
      print(current.getState())
      saved.append(current.getState().copy())
      print('sav2e')
      print(saved)
      choices = current.getChoices()
      print('sav3e')
      print(saved)
      print('choices len')
      print(len(choices))
 
      for choice in choices:
        print('save')
        print(saved)
        print(self.isSaved(saved,choice))
        if not self.isSaved(saved,choice) : stack.append(choice)
      current = Node(stack.pop(), current, current if len(choices)>1 else current.getLastBranch())
    await self.iteration.trigger([current.getState()])
    return current

  async def startDepth(self):
    return await self.startLinearDepth(self.current)

  
  def useAgent(self, onIteration):
    def effect():
      self.iteration.addListener(onIteration)
      return self.iteration.removeListener(onIteration)
    return hooks.use_effect(effect, onIteration)
  
  def getIterationEvent(self):
    return self.iteration
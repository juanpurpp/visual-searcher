from searcher.Node import Node
import json
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
  
  async def startLinearDepth(self,node, delay=0.2):
    stack = []
    saved = []
    current = Node(node.getState(), None, None)
    while not current.isGoal(self.goal_coords):
      row,col = current.getPositionCoords()
      old = current.getFather()
      if old != None : oldRow, oldCol = old.getPositionCoords()
      else: 
        oldRow = None
        oldCol = None
      await self.iteration.trigger([json.dumps({"col":col, "row": row, "oldRow": oldRow , "oldCol": oldCol})])
      
      saved.append(current.getState().copy())

      choices = current.getChoices()

      await asyncio.sleep(delay)
      for choice in choices:
        if not self.isSaved(saved,choice) : stack.append(choice)
      current = Node(stack.pop(), current, current if len(choices)>1 else current.getLastBranch())
    row,col = current.getPositionCoords()
    old = current.getFather()
    if old != None : oldRow, oldCol = old.getPositionCoords()
    else: 
      oldRow = None
      oldCol = None
    await self.iteration.trigger([json.dumps({"col":col, "row": row, "oldRow": oldRow , "oldCol": oldCol, "finished": True})])
    return current

  async def startDepth(self, delay):
    return await self.startLinearDepth(self.current, delay)
  
  def useAgent(self, onIteration):
    def effect():
      self.iteration.addListener(onIteration)
      return self.iteration.removeListener(onIteration)
    return hooks.use_effect(effect, onIteration)
  
  def getIterationEvent(self):
    return self.iteration
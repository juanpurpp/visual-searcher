from searcher.Node import Node
import time
import sys

class Searcher:
  def __init__(self, problem):
    sys.setrecursionlimit(2500)
    def getGoalCoords():
      for i, row in enumerate(problem):
        for j, value in enumerate(row):
          if value == 'g': return [i,j]
      return 0

    self.current = Node(problem, None, None)
    self.goal_coords = getGoalCoords()

  def startRecursiveDepth(self,node, onIteration):
    for i, row in enumerate(node.getState()):
      for j, value in enumerate(row): print(value,end='')
      print('\n')
    print('----------------------------------------------------------------')
    onIteration(node.getState())

    if node.isGoal(self.goal_coords): return 1
    choices = node.getChoices()
    time.sleep(0.25)
    for choice in choices:
      if self.startRecursiveDepth(Node(choice, node, node if len(choices)>1 else None), onIteration) == 1 : return 1
    return 0

  def startDepth(self, onIteration):
    self.startRecursiveDepth(self.current, onIteration)
    return 1
  
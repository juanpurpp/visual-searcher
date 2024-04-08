from fastapi import FastAPI
from reactpy import component, html, run, hooks
from reactpy.backend.fastapi import configure

from components.Maze import Maze
from components.Options import Options

from searcher.Searcher import Searcher

import asyncio
app = FastAPI()

problem = [
    ['i', 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 'g']
]

problem2 = [
  ['i', 0, 1, 0, 1, 0, 1, 1, 1, 'g'],
  [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
  [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

agent = Searcher(problem)

@component
def App():
  problemState, setProblemState = hooks.use_state(problem)
  
  def onIteration(new_problem_state):
      setProblemState(new_problem_state)

      print('iter')
  
  def onStart(e):
    agent.startDepth(onIteration)
    print('termina')
  return html._(
    html.link(
      {
        "href": "https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css",
        "rel": "stylesheet",
      }
    ),
    html.div(
      {"className": "flex flex-col justify-start items-center"},
      html.h1({"className": "text-2xl text-slate-800 font-semibold mb-4"},"Bienvenido a Laberinto Seacher"),
      html.div({"className": "w-full flex flex-row justify-center items-start"},
        Maze(problemState),
        Options(onStart),
      )
    )
  )

configure(app, App)
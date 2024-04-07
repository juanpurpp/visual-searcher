from fastapi import FastAPI
from reactpy import component, html, run
from reactpy.backend.fastapi import configure

from components.Lab import Lab
from components.Options import Options
app = FastAPI()
'''
problem = [
    ['i', 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 'g']
]
'''
problem = [
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



@component
def App():
    return html._(
        html.link(
            {
                "href": "https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css",
                "rel": "stylesheet",
            }
        ),
        html.div(
            {"className": "flex flex-col justify-start items-center"},
            html.h1({"className": "text-2xl text-slate-800 font-semibold"},"Bienvenido a Laberinto Seacher"),
            html.div({"className": "w-full flex flex-row justify-center items-start"},
              Lab(problem),
              Options(),
            )
        )
    )

configure(app, App)
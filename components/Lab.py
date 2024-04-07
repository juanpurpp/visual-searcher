from reactpy import html, component
@component
def detectBlock(val):
  if val == 'i':
    return html.div({'className': 'w-6 h-6 border-2 border-slate-200 bg-blue-400'})
  if val == 'g':
    return html.div({'className': 'w-6 h-6 border-2 border-slate-200 bg-green-400'})
  return html.div({"className": "w-6 h-6  border-2 border-slate-200 " + ('bg-gray-700' if val == 0 else 'bg-gray-100')})

@component
def Lab(problem,):
  return html.div({"className": "w-full flex flex-col justify-center items-center"},
    [
      html.div({"className": "flex flex-row"},
        [
          detectBlock(val)
          for val in row
        ]
      ) for row in problem
    ]
  )
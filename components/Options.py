from reactpy import html, component

@component
def Options(onStart):
  return html.div({"className": "w-full flex flex-col justify-center items-center space-y-2"},
    html.h2({"className": "font-medium text-lg"}, 'Options'),
    html.button({"className": "rounded-md bg-blue-200 border-[1px] border-slate-400 px-2 py-1", "onClick":onStart}, "Start")
  )
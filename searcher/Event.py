class Event:
    def __init__(self):
        # Initialise a list of listeners
        self.__listeners = []
    
    # Define a getter for the 'on' property which returns the decorator.
    @property
    def on(self):
        # A declorator to run addListener on the input function.
        def wrapper(func):
            self.addListener(func)
            return func
        return wrapper
    
    # Add and remove functions from the list of listeners.
    def addListener(self,func):
        if func in self.__listeners: return
        self.__listeners.append(func)
    
    def removeListener(self,func):
        if func not in self.__listeners: return
        self.__listeners.remove(func)
    
    # Trigger events.
    async def trigger(self,args = None):
        # Run all the functions that are saved.
        if args is None:
            args = []
        for func in self.__listeners: await func(*args)
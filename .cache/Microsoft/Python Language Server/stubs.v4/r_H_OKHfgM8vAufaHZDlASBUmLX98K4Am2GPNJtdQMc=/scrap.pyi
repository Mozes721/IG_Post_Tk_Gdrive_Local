pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
__doc__ = None
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/scrap.so'
__name__ = 'pygame.scrap'
__package__ = None
def contains(type):
    'contains(type) -> bool\nChecks whether data for a given type is available in the clipboard.'
    return True

def get(type):
    'get(type) -> bytes or str or None\nGets the data for the specified type from the clipboard.'
    pass

def get_init():
    'get_init() -> bool\nReturns True if the scrap module is currently initialized.'
    return True

def get_types():
    'get_types() -> list\nGets a list of the available clipboard types.'
    return list()

def init():
    'init() -> None\nInitializes the scrap module.'
    pass

def lost():
    'lost() -> bool\nIndicates if the clipboard ownership has been lost by the pygame application.'
    return True

def put(type, data):
    'put(type, data) -> None\nPlaces data into the clipboard.'
    pass

def set_mode(mode):
    'set_mode(mode) -> None\nSets the clipboard access mode.'
    pass


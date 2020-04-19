pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
import __builtin__ as _mod___builtin__

def Event(type, **attributes):
    'Event(type, dict) -> EventType instance\nEvent(type, **attributes) -> EventType instance\ncreate a new event object'
    pass

EventType = _mod___builtin__.Event
_PYGAME_C_API = _mod___builtin__.PyCapsule()
__doc__ = 'pygame module for interacting with events and queues'
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/event.so'
__name__ = 'pygame.event'
__package__ = None
def clear(eventtype=None, pump=True):
    'clear(eventtype=None) -> None\nclear(eventtype=None, pump=True) -> None\nremove all events from the queue'
    pass

def event_name(type):
    'event_name(type) -> string\nget the string name from an event id'
    return ''

def get(eventtype=None, pump=True):
    'get(eventtype=None) -> Eventlist\nget(eventtype=None, pump=True) -> Eventlist\nget events from the queue'
    pass

def get_blocked(type):
    'get_blocked(type) -> bool\ntest if a type of event is blocked from the queue'
    return True

def get_grab():
    'get_grab() -> bool\ntest if the program is sharing input devices'
    return True

def peek(eventtype=None, pump=True):
    'peek(eventtype=None) -> bool\npeek(eventtype=None, pump=True) -> bool\ntest if event types are waiting on the queue'
    return True

def poll():
    'poll() -> EventType instance\nget a single event from the queue'
    pass

def post(Event):
    'post(Event) -> None\nplace a new event on the queue'
    pass

def pump():
    'pump() -> None\ninternally process pygame event handlers'
    pass

def set_allowed(typelist):
    'set_allowed(type) -> None\nset_allowed(typelist) -> None\nset_allowed(None) -> None\ncontrol which events are allowed on the queue'
    pass

def set_blocked(typelist):
    'set_blocked(type) -> None\nset_blocked(typelist) -> None\nset_blocked(None) -> None\ncontrol which events are allowed on the queue'
    pass

def set_grab(bool):
    'set_grab(bool) -> None\ncontrol the sharing of input devices with other applications'
    pass

def wait():
    'wait() -> EventType instance\nwait for a single event from the queue'
    pass


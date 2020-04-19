pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
__doc__ = 'pygame module to work with the keyboard'
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/key.so'
__name__ = 'pygame.key'
__package__ = None
def get_focused():
    'get_focused() -> bool\ntrue if the display is receiving keyboard input from the system'
    return True

def get_mods():
    'get_mods() -> int\ndetermine which modifier keys are being held'
    return 1

def get_pressed():
    'get_pressed() -> bools\nget the state of all keyboard buttons'
    return True

def get_repeat():
    'get_repeat() -> (delay, interval)\nsee how held keys are repeated'
    return tuple()

def name(key):
    'name(key) -> string\nget the name of a key identifier'
    return ''

def set_mods(int):
    'set_mods(int) -> None\ntemporarily set which modifier keys are pressed'
    pass

def set_repeat(delay, interval):
    'set_repeat() -> None\nset_repeat(delay, interval) -> None\ncontrol how held keys are repeated'
    pass

def set_text_input_rect(Rect):
    'set_text_input_rect(Rect) -> None\ncontrols the position of the candidate list'
    pass

def start_text_input():
    'start_text_input() -> None\nstart handling IME compositions'
    pass

def stop_text_input():
    'stop_text_input() -> None\nstop handling IME compositions'
    pass


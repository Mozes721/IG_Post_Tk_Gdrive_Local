pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
import __builtin__ as _mod___builtin__

def Info():
    'Info() -> VideoInfo\nCreate a video display information object'
    pass

_PYGAME_C_API = _mod___builtin__.PyCapsule()
def __PYGAMEinit__():
    'auto initialize function for display.'
    pass

__doc__ = 'pygame module to control the display window and screen'
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/display.so'
__name__ = 'pygame.display'
__package__ = None
def flip():
    'flip() -> None\nUpdate the full display Surface to the screen'
    pass

def get_active():
    'get_active() -> bool\nReturns True when the display is active on the display'
    return True

def get_caption():
    'get_caption() -> (title, icontitle)\nGet the current window caption'
    return tuple()

def get_driver():
    'get_driver() -> name\nGet the name of the pygame display backend'
    pass

def get_init():
    'get_init() -> bool\nReturns True if the display module has been initialized'
    return True

def get_num_displays():
    'get_num_displays() -> int\nReturn the number of displays'
    return 1

def get_surface():
    'get_surface() -> Surface\nGet a reference to the currently set display surface'
    pass

def get_wm_info():
    'get_wm_info() -> dict\nGet information about the current windowing system'
    return dict()

def gl_get_attribute(flag):
    'gl_get_attribute(flag) -> value\nGet the value for an OpenGL flag for the current display'
    pass

def gl_set_attribute(flag, value):
    'gl_set_attribute(flag, value) -> None\nRequest an OpenGL display attribute for the display mode'
    pass

def iconify():
    'iconify() -> bool\nIconify the display surface'
    return True

def init():
    'init() -> None\nInitialize the display module'
    pass

def list_modes(depth=0, flags=pygame.FULLSCREEN, display=0):
    'list_modes(depth=0, flags=pygame.FULLSCREEN, display=0) -> list\nGet list of available fullscreen modes'
    return list()

def mode_ok(size, flags=0, depth=0, display=0):
    'mode_ok(size, flags=0, depth=0, display=0) -> depth\nPick the best color depth for a display mode'
    pass

def quit():
    'quit() -> None\nUninitialize the display module'
    pass

def set_caption(title, icontitle=None):
    'set_caption(title, icontitle=None) -> None\nSet the current window caption'
    pass

def set_gamma(red, green=None, blue=None):
    'set_gamma(red, green=None, blue=None) -> bool\nChange the hardware gamma ramps'
    return True

def set_gamma_ramp(red, green, blue):
    'set_gamma_ramp(red, green, blue) -> bool\nChange the hardware gamma ramps with a custom lookup'
    return True

def set_icon(Surface):
    'set_icon(Surface) -> None\nChange the system image for the display window'
    pass

def set_mode(size=(0,0), flags=0, depth=0, display=0):
    'set_mode(size=(0, 0), flags=0, depth=0, display=0) -> Surface\nInitialize a window or screen for display'
    pass

def set_palette(palette=None):
    'set_palette(palette=None) -> None\nSet the display color palette for indexed displays'
    pass

def toggle_fullscreen():
    'toggle_fullscreen() -> bool\nSwitch between fullscreen and windowed displays'
    return True

def update(rectangle_list):
    'update(rectangle=None) -> None\nupdate(rectangle_list) -> None\nUpdate portions of the screen for software displays'
    pass


pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
import __builtin__ as _mod___builtin__
import pygame as _mod_pygame

BufferError = _mod_pygame.BufferError
HAVE_NEWBUF = 1
_PYGAME_C_API = _mod___builtin__.PyCapsule()
__doc__ = 'the top level pygame package'
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/base.so'
__name__ = 'pygame.base'
__package__ = None
error = _mod_pygame.error
def get_array_interface():
    'return an array struct interface as an interface dictionary'
    pass

def get_error():
    'get_error() -> errorstr\nget the current error message'
    pass

def get_init():
    'get_init() -> bool\nreturns True if pygame is currently initialized'
    return True

def get_sdl_byteorder():
    'get_sdl_byteorder() -> int\nget the byte order of SDL'
    return 1

def get_sdl_version():
    'get_sdl_version() -> major, minor, patch\nget the version number of SDL'
    pass

def init():
    'init() -> (numpass, numfail)\ninitialize all imported pygame modules'
    return tuple()

def quit():
    'quit() -> None\nuninitialize all pygame modules'
    pass

def register_quit(callable):
    'register_quit(callable) -> None\nregister a function to be called when pygame quits'
    pass

def segfault():
    'crash'
    pass

def set_error(error_msg):
    'set_error(error_msg) -> None\nset the current error message'
    pass


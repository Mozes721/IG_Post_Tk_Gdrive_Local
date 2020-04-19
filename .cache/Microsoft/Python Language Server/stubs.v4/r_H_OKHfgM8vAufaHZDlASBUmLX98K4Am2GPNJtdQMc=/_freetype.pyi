pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
import __builtin__ as _mod___builtin__
import _freetype as _mod__freetype

BBOX_EXACT = 0
BBOX_EXACT_GRIDFIT = 1
BBOX_PIXEL = 2
BBOX_PIXEL_GRIDFIT = 3
Font = _mod__freetype.Font
STYLE_DEFAULT = 255
STYLE_NORMAL = 0
STYLE_OBLIQUE = 2
STYLE_STRONG = 1
STYLE_UNDERLINE = 4
STYLE_WIDE = 8
_PYGAME_C_API = _mod___builtin__.PyCapsule()
def __PYGAMEinit__():
    'auto initialize function for _freetype'
    pass

__doc__ = 'Enhanced pygame module for loading and rendering computer fonts'
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/_freetype.so'
__name__ = 'pygame._freetype'
__package__ = None
def get_cache_size():
    'get_cache_size() -> long\nReturn the glyph case size'
    return 1L

def get_default_font():
    'get_default_font() -> string\nGet the filename of the default font'
    return ''

def get_default_resolution():
    'get_default_resolution() -> long\nReturn the default pixel size in dots per inch'
    return 1L

def get_error():
    'get_error() -> str\nReturn the latest FreeType error'
    return ''

def get_init():
    'get_init() -> bool\nReturns True if the FreeType module is currently initialized.'
    return True

def get_version():
    'get_version() -> (int, int, int)\nReturn the FreeType version'
    return tuple()

def init(cache_size=64, resolution=72):
    'init(cache_size=64, resolution=72)\nInitialize the underlying FreeType library.'
    pass

def quit():
    'quit()\nShut down the underlying FreeType library.'
    pass

def set_default_resolution(resolution=None):
    'set_default_resolution([resolution])\nSet the default pixel size in dots per inch for the module'
    pass

def was_init():
    'was_init() -> bool\nDEPRECATED: Use get_init() instead.'
    return True


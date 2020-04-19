pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
import __builtin__ as _mod___builtin__

def Channel(id):
    'Channel(id) -> Channel\nCreate a Channel object for controlling playback'
    pass

ChannelType = _mod___builtin__.Channel
Sound = _mod___builtin__.Sound
SoundType = _mod___builtin__.Sound
_PYGAME_C_API = _mod___builtin__.PyCapsule()
def __PYGAMEinit__():
    'auto initialize for mixer'
    pass

__doc__ = 'pygame module for loading and playing sounds'
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/mixer.so'
__name__ = 'pygame.mixer'
__package__ = None
def fadeout(time):
    'fadeout(time) -> None\nfade out the volume on all sounds before stopping'
    pass

def find_channel(force=False):
    'find_channel(force=False) -> Channel\nfind an unused channel'
    pass

def get_busy():
    'get_busy() -> bool\ntest if any sound is being mixed'
    return True

def get_init():
    'get_init() -> (frequency, format, channels)\ntest if the mixer is initialized'
    return tuple()

def get_num_channels():
    'get_num_channels() -> count\nget the total number of playback channels'
    pass

def init(frequency=22050, size=-16, channels=2, buffer=4096, devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE|AUDIO_ALLOW_CHANNELS_CHANGE):
    'init(frequency=22050, size=-16, channels=2, buffer=4096, devicename=None, allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE) -> None\ninitialize the mixer module'
    pass

def pause():
    'pause() -> None\ntemporarily stop playback of all sound channels'
    pass

def pre_init(frequency=22050, size=-16, channels=2, buffersize=4096, devicename=None):
    'pre_init(frequency=22050, size=-16, channels=2, buffersize=4096, devicename=None) -> None\npreset the mixer init arguments'
    pass

def quit():
    'quit() -> None\nuninitialize the mixer'
    pass

def set_num_channels(count):
    'set_num_channels(count) -> None\nset the total number of playback channels'
    pass

def set_reserved(count):
    'set_reserved(count) -> None\nreserve channels from being automatically used'
    pass

def stop():
    'stop() -> None\nstop playback of all sound channels'
    pass

def unpause():
    'unpause() -> None\nresume paused playback of sound channels'
    pass


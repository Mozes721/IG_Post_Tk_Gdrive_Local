import __builtin__ as _mod___builtin__
import exceptions as _mod_exceptions

ACCESS_COPY = 3
ACCESS_READ = 1
ACCESS_WRITE = 2
ALLOCATIONGRANULARITY = 4096
MAP_ANON = 32
MAP_ANONYMOUS = 32
MAP_DENYWRITE = 2048
MAP_EXECUTABLE = 4096
MAP_PRIVATE = 2
MAP_SHARED = 1
PAGESIZE = 4096
PROT_EXEC = 4
PROT_READ = 1
PROT_WRITE = 2
__doc__ = None
__file__ = '/usr/lib/python2.7/lib-dynload/mmap.x86_64-linux-gnu.so'
__name__ = 'mmap'
__package__ = None
class error(_mod_exceptions.EnvironmentError):
    __class__ = error
    __dict__ = {}
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    __module__ = 'mmap'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class mmap(_mod___builtin__.object):
    "Windows: mmap(fileno, length[, tagname[, access[, offset]]])\n\nMaps length bytes from the file specified by the file handle fileno,\nand returns a mmap object.  If length is larger than the current size\nof the file, the file is extended to contain length bytes.  If length\nis 0, the maximum length of the map is the current size of the file,\nexcept that if the file is empty Windows raises an exception (you cannot\ncreate an empty mapping on Windows).\n\nUnix: mmap(fileno, length[, flags[, prot[, access[, offset]]]])\n\nMaps length bytes from the file specified by the file descriptor fileno,\nand returns a mmap object.  If length is 0, the maximum length of the map\nwill be the current size of the file when mmap is called.\nflags specifies the nature of the mapping. MAP_PRIVATE creates a\nprivate copy-on-write mapping, so changes to the contents of the mmap\nobject will be private to this process, and MAP_SHARED creates a mapping\nthat's shared with all other processes mapping the same areas of the file.\nThe default value is MAP_SHARED.\n\nTo map anonymous memory, pass -1 as the fileno (both versions)."
    __class__ = mmap
    def __delitem__(self):
        'x.__delitem__(y) <==> del x[y]'
        return None
    
    def __delslice__(self):
        'x.__delslice__(i, j) <==> del x[i:j]\n           \n           Use of negative indices is not supported.'
        pass
    
    def __getattribute__(self):
        "x.__getattribute__('name') <==> x.name"
        pass
    
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    
    def __getslice__(self):
        'x.__getslice__(i, j) <==> x[i:j]\n           \n           Use of negative indices is not supported.'
        return mmap()
    
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    def __len__(self):
        'x.__len__() <==> len(x)'
        return 0
    
    def __setitem__(self, index, value):
        'x.__setitem__(i, y) <==> x[i]=y'
        return None
    
    def __setslice__(self):
        'x.__setslice__(i, j, y) <==> x[i:j]=y\n           \n           Use  of negative indices is not supported.'
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        pass
    
    def find(self):
        pass
    
    def flush(self):
        pass
    
    def move(self):
        pass
    
    def read(self):
        pass
    
    def read_byte(self):
        pass
    
    def readline(self):
        pass
    
    def resize(self):
        pass
    
    def rfind(self):
        pass
    
    def seek(self):
        pass
    
    def size(self):
        pass
    
    def tell(self):
        pass
    
    def write(self):
        pass
    
    def write_byte(self):
        pass
    


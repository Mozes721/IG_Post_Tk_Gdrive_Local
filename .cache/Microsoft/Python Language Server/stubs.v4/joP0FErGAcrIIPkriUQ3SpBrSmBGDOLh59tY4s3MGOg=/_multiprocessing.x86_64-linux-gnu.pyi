import __builtin__ as _mod___builtin__

class Connection(_mod___builtin__.object):
    'Connection type whose constructor signature is\n\n    Connection(handle, readable=True, writable=True).\n\nThe constructor does *not* duplicate the handle.'
    __class__ = Connection
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    def __repr__(self):
        'x.__repr__() <==> repr(x)'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        'close the connection'
        pass
    
    @property
    def closed(self):
        'True if the connection is closed'
        pass
    
    def fileno(self):
        'file descriptor or handle of the connection'
        pass
    
    def poll(self):
        'whether there is any input available to be read'
        pass
    
    @property
    def readable(self):
        'True if the connection is readable'
        pass
    
    def recv(self):
        'receive a (picklable) object'
        pass
    
    def recv_bytes(self):
        'receive byte data as a string'
        pass
    
    def recv_bytes_into(self):
        'receive byte data into a writeable buffer-like object\nreturns the number of bytes read'
        pass
    
    def send(self, picklable):
        'send a (picklable) object'
        pass
    
    def send_bytes(self):
        'send the byte data from a readable buffer-like object'
        pass
    
    @property
    def writable(self):
        'True if the connection is writable'
        pass
    

class SemLock(_mod___builtin__.object):
    'Semaphore/Mutex type'
    SEM_VALUE_MAX = 2147483647L
    __class__ = SemLock
    def __enter__(self):
        'enter the semaphore/lock'
        return self
    
    def __exit__(self):
        'exit the semaphore/lock'
        pass
    
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _after_fork(self):
        'rezero the net acquisition count after fork()'
        pass
    
    def _count(self):
        'num of `acquire()`s minus num of `release()`s for this process'
        pass
    
    def _get_value(self):
        'get the value of the semaphore'
        pass
    
    def _is_mine(self):
        'whether the lock is owned by this thread'
        pass
    
    def _is_zero(self):
        'returns whether semaphore has value zero'
        pass
    
    @classmethod
    def _rebuild(cls):
        pass
    
    def acquire(self):
        'acquire the semaphore/lock'
        pass
    
    @property
    def handle(self):
        pass
    
    @property
    def kind(self):
        pass
    
    @property
    def maxvalue(self):
        pass
    
    def release(self):
        'release the semaphore/lock'
        pass
    

__doc__ = None
__file__ = '/usr/lib/python2.7/lib-dynload/_multiprocessing.x86_64-linux-gnu.so'
__name__ = '_multiprocessing'
__package__ = None
def address_of_buffer(obj):
    'address_of_buffer(obj) -> int\nReturn address of obj assuming obj supports buffer inteface'
    return 1

flags = _mod___builtin__.dict()
def recvfd(sockfd):
    'recvfd(sockfd) -> fd\nReceive a file descriptor over a unix domain socket\nwhose file decriptor is sockfd'
    pass

def sendfd(sockfd, fd):
    'sendfd(sockfd, fd) -> None\nSend file descriptor given by fd over the unix domain socket\nwhose file decriptor is sockfd'
    pass


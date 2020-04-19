pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
import __builtin__ as _mod___builtin__

class Vector2(_mod___builtin__.object):
    'Vector2() -> Vector2\nVector2(int) -> Vector2\nVector2(float) -> Vector2\nVector2(Vector2) -> Vector2\nVector2(x, y) -> Vector2\nVector2((x, y)) -> Vector2\na 2-Dimensional Vector'
    def __add__(self):
        'x.__add__(y) <==> x+y'
        return Vector2()
    
    __class__ = Vector2
    def __delattr__(self):
        "x.__delattr__('name') <==> del x.name"
        return None
    
    def __delitem__(self):
        'x.__delitem__(y) <==> del x[y]'
        return None
    
    def __delslice__(self):
        'x.__delslice__(i, j) <==> del x[i:j]\n           \n           Use of negative indices is not supported.'
        pass
    
    def __div__(self):
        'x.__div__(y) <==> x/y'
        pass
    
    def __eq__(self):
        'x.__eq__(y) <==> x==y'
        return False
    
    def __floordiv__(self):
        'x.__floordiv__(y) <==> x//y'
        return 0
    
    def __ge__(self):
        'x.__ge__(y) <==> x>=y'
        return False
    
    def __getattribute__(self):
        "x.__getattribute__('name') <==> x.name"
        pass
    
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    
    def __getslice__(self):
        'x.__getslice__(i, j) <==> x[i:j]\n           \n           Use of negative indices is not supported.'
        return Vector2()
    
    def __gt__(self):
        'x.__gt__(y) <==> x>y'
        return False
    
    def __iadd__(self):
        'x.__iadd__(y) <==> x+=y'
        return None
    
    def __idiv__(self):
        'x.__idiv__(y) <==> x/=y'
        pass
    
    def __ifloordiv__(self):
        'x.__ifloordiv__(y) <==> x//=y'
        pass
    
    def __imul__(self):
        'x.__imul__(y) <==> x*=y'
        return None
    
    def __init__(self, Vector2):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    def __isub__(self):
        'x.__isub__(y) <==> x-=y'
        return None
    
    def __iter__(self):
        'x.__iter__() <==> iter(x)'
        return Vector2()
    
    def __itruediv__(self):
        'x.__itruediv__(y) <==> x/=y'
        pass
    
    def __le__(self):
        'x.__le__(y) <==> x<=y'
        return False
    
    def __len__(self):
        'x.__len__() <==> len(x)'
        return 0
    
    def __lt__(self):
        'x.__lt__(y) <==> x<y'
        return False
    
    def __mul__(self):
        'x.__mul__(y) <==> x*y'
        return Vector2()
    
    def __ne__(self):
        'x.__ne__(y) <==> x!=y'
        return False
    
    def __neg__(self):
        'x.__neg__() <==> -x'
        return Vector2()
    
    def __nonzero__(self):
        'x.__nonzero__() <==> x != 0'
        pass
    
    def __pos__(self):
        'x.__pos__() <==> +x'
        return Vector2()
    
    def __radd__(self):
        'x.__radd__(y) <==> y+x'
        return Vector2()
    
    def __rdiv__(self):
        'x.__rdiv__(y) <==> y/x'
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'x.__repr__() <==> repr(x)'
        return ''
    
    def __rfloordiv__(self):
        'x.__rfloordiv__(y) <==> y//x'
        return Vector2()
    
    def __rmul__(self):
        'x.__rmul__(y) <==> y*x'
        return Vector2()
    
    def __rsub__(self):
        'x.__rsub__(y) <==> y-x'
        return Vector2()
    
    def __rtruediv__(self):
        'x.__rtruediv__(y) <==> y/x'
        return Vector2()
    
    def __safe_for_unpickling__(self):
        pass
    
    def __setattr__(self):
        "x.__setattr__('name', value) <==> x.name = value"
        return None
    
    def __setitem__(self, index, value):
        'x.__setitem__(i, y) <==> x[i]=y'
        return None
    
    def __setslice__(self):
        'x.__setslice__(i, j, y) <==> x[i:j]=y\n           \n           Use  of negative indices is not supported.'
        pass
    
    def __str__(self):
        'x.__str__() <==> str(x)'
        return ''
    
    def __sub__(self):
        'x.__sub__(y) <==> x-y'
        return Vector2()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self):
        'x.__truediv__(y) <==> x/y'
        return 0.0
    
    def angle_to(self, Vector2):
        'angle_to(Vector2) -> float\ncalculates the angle to a given vector in degrees.'
        return 1.0
    
    def as_polar(self):
        'as_polar() -> (r, phi)\nreturns a tuple with radial distance and azimuthal angle.'
        return tuple()
    
    def cross(self, Vector2):
        'cross(Vector2) -> Vector2\ncalculates the cross- or vector-product'
        pass
    
    def distance_squared_to(self, Vector2):
        'distance_squared_to(Vector2) -> float\ncalculates the squared Euclidean distance to a given vector.'
        return 1.0
    
    def distance_to(self, Vector2):
        'distance_to(Vector2) -> float\ncalculates the Euclidean distance to a given vector.'
        return 1.0
    
    def dot(self, Vector2):
        'dot(Vector2) -> float\ncalculates the dot- or scalar-product with the other vector'
        return 1.0
    
    def elementwise(self):
        'elementwise() -> VectorElementwiseProxy\nThe next operation will be performed elementwise.'
        pass
    
    @property
    def epsilon(self):
        'small value used in comparisons'
        pass
    
    def from_polar(self, r, phi):
        'from_polar((r, phi)) -> None\nSets x and y from a polar coordinates tuple.'
        pass
    
    def is_normalized(self):
        'is_normalized() -> Bool\ntests if the vector is normalized i.e. has length == 1.'
        pass
    
    def length(self):
        'length() -> float\nreturns the Euclidean length of the vector.'
        return 1.0
    
    def length_squared(self):
        'length_squared() -> float\nreturns the squared Euclidean length of the vector.'
        return 1.0
    
    def lerp(self, Vector2, float):
        'lerp(Vector2, float) -> Vector2\nreturns a linear interpolation to the given vector.'
        pass
    
    def magnitude(self):
        'magnitude() -> float\nreturns the Euclidean magnitude of the vector.'
        return 1.0
    
    def magnitude_squared(self):
        'magnitude_squared() -> float\nreturns the squared magnitude of the vector.'
        return 1.0
    
    def normalize(self):
        'normalize() -> Vector2\nreturns a vector with the same direction but length 1.'
        pass
    
    def normalize_ip(self):
        'normalize_ip() -> None\nnormalizes the vector in place so that its length is 1.'
        pass
    
    def reflect(self, Vector2):
        'reflect(Vector2) -> Vector2\nreturns a vector reflected of a given normal.'
        pass
    
    def reflect_ip(self, Vector2):
        'reflect_ip(Vector2) -> None\nreflect the vector of a given normal in place.'
        pass
    
    def rotate(self, float):
        'rotate(float) -> Vector2\nrotates a vector by a given angle in degrees.'
        pass
    
    def rotate_ip(self, float):
        'rotate_ip(float) -> None\nrotates the vector by a given angle in degrees in place.'
        pass
    
    def scale_to_length(self, float):
        'scale_to_length(float) -> None\nscales the vector to a given length.'
        pass
    
    def slerp(self, Vector2, float):
        'slerp(Vector2, float) -> Vector2\nreturns a spherical interpolation to the given vector.'
        pass
    
    def update(self, Vector2):
        'update() -> None\nupdate(int) -> None\nupdate(float) -> None\nupdate(Vector2) -> None\nupdate(x, y) -> None\nupdate((x, y)) -> None\nSets the coordinates of the vector.'
        pass
    
    @property
    def x(self):
        pass
    
    @property
    def y(self):
        pass
    

class Vector3(_mod___builtin__.object):
    'Vector3() -> Vector3\nVector3(int) -> Vector3\nVector3(float) -> Vector3\nVector3(Vector3) -> Vector3\nVector3(x, y, z) -> Vector3\nVector3((x, y, z)) -> Vector3\na 3-Dimensional Vector'
    def __add__(self):
        'x.__add__(y) <==> x+y'
        return Vector3()
    
    __class__ = Vector3
    def __delattr__(self):
        "x.__delattr__('name') <==> del x.name"
        return None
    
    def __delitem__(self):
        'x.__delitem__(y) <==> del x[y]'
        return None
    
    def __delslice__(self):
        'x.__delslice__(i, j) <==> del x[i:j]\n           \n           Use of negative indices is not supported.'
        pass
    
    def __div__(self):
        'x.__div__(y) <==> x/y'
        pass
    
    def __eq__(self):
        'x.__eq__(y) <==> x==y'
        return False
    
    def __floordiv__(self):
        'x.__floordiv__(y) <==> x//y'
        return 0
    
    def __ge__(self):
        'x.__ge__(y) <==> x>=y'
        return False
    
    def __getattribute__(self):
        "x.__getattribute__('name') <==> x.name"
        pass
    
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    
    def __getslice__(self):
        'x.__getslice__(i, j) <==> x[i:j]\n           \n           Use of negative indices is not supported.'
        return Vector3()
    
    def __gt__(self):
        'x.__gt__(y) <==> x>y'
        return False
    
    def __iadd__(self):
        'x.__iadd__(y) <==> x+=y'
        return None
    
    def __idiv__(self):
        'x.__idiv__(y) <==> x/=y'
        pass
    
    def __ifloordiv__(self):
        'x.__ifloordiv__(y) <==> x//=y'
        pass
    
    def __imul__(self):
        'x.__imul__(y) <==> x*=y'
        return None
    
    def __init__(self, x, y, z):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    def __isub__(self):
        'x.__isub__(y) <==> x-=y'
        return None
    
    def __iter__(self):
        'x.__iter__() <==> iter(x)'
        return Vector3()
    
    def __itruediv__(self):
        'x.__itruediv__(y) <==> x/=y'
        pass
    
    def __le__(self):
        'x.__le__(y) <==> x<=y'
        return False
    
    def __len__(self):
        'x.__len__() <==> len(x)'
        return 0
    
    def __lt__(self):
        'x.__lt__(y) <==> x<y'
        return False
    
    def __mul__(self):
        'x.__mul__(y) <==> x*y'
        return Vector3()
    
    def __ne__(self):
        'x.__ne__(y) <==> x!=y'
        return False
    
    def __neg__(self):
        'x.__neg__() <==> -x'
        return Vector3()
    
    def __nonzero__(self):
        'x.__nonzero__() <==> x != 0'
        pass
    
    def __pos__(self):
        'x.__pos__() <==> +x'
        return Vector3()
    
    def __radd__(self):
        'x.__radd__(y) <==> y+x'
        return Vector3()
    
    def __rdiv__(self):
        'x.__rdiv__(y) <==> y/x'
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'x.__repr__() <==> repr(x)'
        return ''
    
    def __rfloordiv__(self):
        'x.__rfloordiv__(y) <==> y//x'
        return Vector3()
    
    def __rmul__(self):
        'x.__rmul__(y) <==> y*x'
        return Vector3()
    
    def __rsub__(self):
        'x.__rsub__(y) <==> y-x'
        return Vector3()
    
    def __rtruediv__(self):
        'x.__rtruediv__(y) <==> y/x'
        return Vector3()
    
    def __safe_for_unpickling__(self):
        pass
    
    def __setattr__(self):
        "x.__setattr__('name', value) <==> x.name = value"
        return None
    
    def __setitem__(self, index, value):
        'x.__setitem__(i, y) <==> x[i]=y'
        return None
    
    def __setslice__(self):
        'x.__setslice__(i, j, y) <==> x[i:j]=y\n           \n           Use  of negative indices is not supported.'
        pass
    
    def __str__(self):
        'x.__str__() <==> str(x)'
        return ''
    
    def __sub__(self):
        'x.__sub__(y) <==> x-y'
        return Vector3()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self):
        'x.__truediv__(y) <==> x/y'
        return 0.0
    
    def angle_to(self, Vector3):
        'angle_to(Vector3) -> float\ncalculates the angle to a given vector in degrees.'
        return 1.0
    
    def as_spherical(self):
        'as_spherical() -> (r, theta, phi)\nreturns a tuple with radial distance, inclination and azimuthal angle.'
        return tuple()
    
    def cross(self, Vector3):
        'cross(Vector3) -> Vector3\ncalculates the cross- or vector-product'
        pass
    
    def distance_squared_to(self, Vector3):
        'distance_squared_to(Vector3) -> float\ncalculates the squared Euclidean distance to a given vector.'
        return 1.0
    
    def distance_to(self, Vector3):
        'distance_to(Vector3) -> float\ncalculates the Euclidean distance to a given vector.'
        return 1.0
    
    def dot(self, Vector3):
        'dot(Vector3) -> float\ncalculates the dot- or scalar-product with the other vector'
        return 1.0
    
    def elementwise(self):
        'elementwise() -> VectorElementwiseProxy\nThe next operation will be performed elementwise.'
        pass
    
    @property
    def epsilon(self):
        'small value used in comparisons'
        pass
    
    def from_spherical(self, r, theta, phi):
        'from_spherical((r, theta, phi)) -> None\nSets x, y and z from a spherical coordinates 3-tuple.'
        pass
    
    def is_normalized(self):
        'is_normalized() -> Bool\ntests if the vector is normalized i.e. has length == 1.'
        pass
    
    def length(self):
        'length() -> float\nreturns the Euclidean length of the vector.'
        return 1.0
    
    def length_squared(self):
        'length_squared() -> float\nreturns the squared Euclidean length of the vector.'
        return 1.0
    
    def lerp(self, Vector3, float):
        'lerp(Vector3, float) -> Vector3\nreturns a linear interpolation to the given vector.'
        pass
    
    def magnitude(self):
        'magnitude() -> float\nreturns the Euclidean magnitude of the vector.'
        return 1.0
    
    def magnitude_squared(self):
        'magnitude_squared() -> float\nreturns the squared Euclidean magnitude of the vector.'
        return 1.0
    
    def normalize(self):
        'normalize() -> Vector3\nreturns a vector with the same direction but length 1.'
        pass
    
    def normalize_ip(self):
        'normalize_ip() -> None\nnormalizes the vector in place so that its length is 1.'
        pass
    
    def reflect(self, Vector3):
        'reflect(Vector3) -> Vector3\nreturns a vector reflected of a given normal.'
        pass
    
    def reflect_ip(self, Vector3):
        'reflect_ip(Vector3) -> None\nreflect the vector of a given normal in place.'
        pass
    
    def rotate(self, Vector3, float):
        'rotate(Vector3, float) -> Vector3\nrotates a vector by a given angle in degrees.'
        pass
    
    def rotate_ip(self, Vector3, float):
        'rotate_ip(Vector3, float) -> None\nrotates the vector by a given angle in degrees in place.'
        pass
    
    def rotate_x(self, float):
        'rotate_x(float) -> Vector3\nrotates a vector around the x-axis by the angle in degrees.'
        pass
    
    def rotate_x_ip(self, float):
        'rotate_x_ip(float) -> None\nrotates the vector around the x-axis by the angle in degrees in place.'
        pass
    
    def rotate_y(self, float):
        'rotate_y(float) -> Vector3\nrotates a vector around the y-axis by the angle in degrees.'
        pass
    
    def rotate_y_ip(self, float):
        'rotate_y_ip(float) -> None\nrotates the vector around the y-axis by the angle in degrees in place.'
        pass
    
    def rotate_z(self, float):
        'rotate_z(float) -> Vector3\nrotates a vector around the z-axis by the angle in degrees.'
        pass
    
    def rotate_z_ip(self, float):
        'rotate_z_ip(float) -> None\nrotates the vector around the z-axis by the angle in degrees in place.'
        pass
    
    def scale_to_length(self, float):
        'scale_to_length(float) -> None\nscales the vector to a given length.'
        pass
    
    def slerp(self, Vector3, float):
        'slerp(Vector3, float) -> Vector3\nreturns a spherical interpolation to the given vector.'
        pass
    
    def update(self, x, y, z):
        'update() -> None\nupdate(int) -> None\nupdate(float) -> None\nupdate(Vector3) -> None\nupdate(x, y, z) -> None\nupdate((x, y, z)) -> None\nSets the coordinates of the vector.'
        pass
    
    @property
    def x(self):
        pass
    
    @property
    def y(self):
        pass
    
    @property
    def z(self):
        pass
    

class VectorElementwiseProxy(_mod___builtin__.object):
    def __abs__(self):
        'x.__abs__() <==> abs(x)'
        return VectorElementwiseProxy()
    
    def __add__(self):
        'x.__add__(y) <==> x+y'
        return VectorElementwiseProxy()
    
    __class__ = VectorElementwiseProxy
    def __div__(self):
        'x.__div__(y) <==> x/y'
        pass
    
    def __eq__(self):
        'x.__eq__(y) <==> x==y'
        return False
    
    def __floordiv__(self):
        'x.__floordiv__(y) <==> x//y'
        return 0
    
    def __ge__(self):
        'x.__ge__(y) <==> x>=y'
        return False
    
    def __gt__(self):
        'x.__gt__(y) <==> x>y'
        return False
    
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    def __le__(self):
        'x.__le__(y) <==> x<=y'
        return False
    
    def __lt__(self):
        'x.__lt__(y) <==> x<y'
        return False
    
    def __mod__(self):
        'x.__mod__(y) <==> x%y'
        return VectorElementwiseProxy()
    
    def __mul__(self):
        'x.__mul__(y) <==> x*y'
        return VectorElementwiseProxy()
    
    def __ne__(self):
        'x.__ne__(y) <==> x!=y'
        return False
    
    def __neg__(self):
        'x.__neg__() <==> -x'
        return VectorElementwiseProxy()
    
    def __nonzero__(self):
        'x.__nonzero__() <==> x != 0'
        pass
    
    def __pos__(self):
        'x.__pos__() <==> +x'
        return VectorElementwiseProxy()
    
    def __pow__(self):
        'x.__pow__(y[, z]) <==> pow(x, y[, z])'
        return VectorElementwiseProxy()
    
    def __radd__(self):
        'x.__radd__(y) <==> y+x'
        return VectorElementwiseProxy()
    
    def __rdiv__(self):
        'x.__rdiv__(y) <==> y/x'
        pass
    
    def __rfloordiv__(self):
        'x.__rfloordiv__(y) <==> y//x'
        return VectorElementwiseProxy()
    
    def __rmod__(self):
        'x.__rmod__(y) <==> y%x'
        return VectorElementwiseProxy()
    
    def __rmul__(self):
        'x.__rmul__(y) <==> y*x'
        return VectorElementwiseProxy()
    
    def __rpow__(self):
        'y.__rpow__(x[, z]) <==> pow(x, y[, z])'
        return VectorElementwiseProxy()
    
    def __rsub__(self):
        'x.__rsub__(y) <==> y-x'
        return VectorElementwiseProxy()
    
    def __rtruediv__(self):
        'x.__rtruediv__(y) <==> y/x'
        return VectorElementwiseProxy()
    
    def __sub__(self):
        'x.__sub__(y) <==> x-y'
        return VectorElementwiseProxy()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self):
        'x.__truediv__(y) <==> x/y'
        return 0.0
    

class VectorIterator(_mod___builtin__.object):
    __class__ = VectorIterator
    def __getattribute__(self):
        "x.__getattribute__('name') <==> x.name"
        pass
    
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    def __iter__(self):
        'x.__iter__() <==> iter(x)'
        return VectorIterator()
    
    def __length_hint__(self):
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def next(self):
        'x.next() -> the next value, or raise StopIteration'
        pass
    

_PYGAME_C_API = _mod___builtin__.PyCapsule()
__doc__ = 'pygame module for vector classes'
__file__ = '/home/mozes721/.local/lib/python2.7/site-packages/pygame/math.so'
__name__ = 'pygame.math'
__package__ = None
def disable_swizzling():
    'disables swizzling.'
    pass

def enable_swizzling():
    'enables swizzling.'
    pass


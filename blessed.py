'''
Blessed library that merges the functional world of Haskell and Python together

Author: megabytesofrem
License: MIT
'''

import builtins
from core import *

from data.Monoid import *
from data.Maybe import *
from data.Either import *
from data.Functor import *

'''
Polyfills for enabling Blessed to modify Python builtin types
'''

@MonoidInt.register
class _IntPolyfill(int, MonoidInt):
    pass

@MonoidStr.register
class _StrPolyfill(str, MonoidStr):
    pass

@MonoidList.register
@FunctorList.register
# Since List is both a Monoid and Functor, it has multiple "subclasses"
class _ListPolyfill(List, MonoidList, FunctorList):
    pass

def polyfill():
    '''
    Register the polyfills by overriding the builtins objects,
    and then registering virtual subclasses for all the Monoid and Functor instances.
    '''

    builtins.int = _IntPolyfill
    builtins.str = _StrPolyfill
    builtins.list = _ListPolyfill

    Monoid.register(_IntPolyfill)
    Monoid.register(_StrPolyfill)
    Monoid.register(_ListPolyfill)
    Functor.register(_ListPolyfill)
    Functor.register(Maybe)
    Functor.register(Either)

    Applicative.register(Maybe)
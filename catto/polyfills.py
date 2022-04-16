'''
Catto extends Python with concepts from category theory, such as functors, applicatives and monads

Author: megabytesofrem
License: MIT
'''

import builtins
from catto.core import *

from catto.data.Monoid import *
from catto.data.Maybe import *
from catto.data.Either import *
from catto.data.Functor import *
from catto.data.Foldable import Foldable, FoldableList

'''
Polyfills for enabling Catto to modify Python builtin types
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
class _ListPolyfill(List, MonoidList, FunctorList, FoldableList):
    pass

def polyfill():
    '''
    Register the polyfills by overriding the builtin objects
    '''

    builtins.int = _IntPolyfill
    builtins.str = _StrPolyfill
    builtins.list = _ListPolyfill

    builtins.list.head = lambda x: x[0]
    builtins.list.tail = lambda x: x[1:]
    builtins.list.init = lambda x: x[:-1]
    builtins.list.last = builtins.list.tail
    builtins.list.fst = builtins.list.head
    builtins.list.snd = builtins.list.tail

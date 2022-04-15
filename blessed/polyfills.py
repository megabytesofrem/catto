'''
Blessed library that merges the functional world of Haskell and Python together

Author: megabytesofrem
License: MIT
'''

import builtins
from blessed.core import *

from blessed.data.Monoid import *
from blessed.data.Maybe import *
from blessed.data.Either import *
from blessed.data.Functor import *
from blessed.data.Foldable import Foldable, FoldableList

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

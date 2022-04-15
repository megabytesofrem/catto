from ..core import *
from ..control.Applicative import Applicative
from ..data.Functor import Functor

class Maybe(Applicative[Generic[A]]):
    '''
    The Maybe type encapsulates an optional value, and is either Just(a) or Nothing().
    '''

    def __init__(self, value: A):
        self.value = value

    def fmap(f, m) -> A:
        if m.value == None:
            return Nothing()
        else:
            return Just(f(m.value))

    # Applicative
    def pure(a) -> A:
        return Just(a)
    
    def ap(f, x) -> A:
        if f == Nothing or x == Nothing:
            return Nothing
        else:
            return Just(f(x))

def Just(a) -> Maybe[A]:
    return Maybe(a)

def Nothing() -> Maybe[A]:
    return Maybe(None)
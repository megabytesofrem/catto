from core import *
from control.Applicative import Applicative
from data.Functor import Functor

class MaybeA(Generic[A]):
    '''
    The Maybe type encapsulates an optional value, and is either Just(a) or Nothing().
    '''
    def __init__(self, value: A):
        self.value = value

def Just(a) -> MaybeA[A]:
    return MaybeA(a)

def Nothing() -> MaybeA[A]:
    return MaybeA(None)

class Maybe(Applicative[MaybeA[A]]):
    '''
    Functor and Applicative instance for Maybe
    '''
    def fmap(f, m) -> MaybeA[A]:
        if m.value == None:
            return Nothing()
        else:
            return Just(f(m.value))

    def pure(a) -> MaybeA[A]:
        return Just(a)
    
    def ap(f, x) -> MaybeA[A]:
        if f == Nothing or x == Nothing:
            return Nothing
        else:
            return Just(f(x))

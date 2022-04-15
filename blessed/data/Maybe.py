from ..core import *
from ..control.Applicative import Applicative
from ..data.Functor import Functor

from ..control.Monad import Monad

@Monad.register
class Maybe(Monad[Generic[A]]):
    '''
    The Maybe type encapsulates an optional value, and is either Just(a) or Nothing().

    It has instances of Functor, Applicative and Monad
    '''

    def fmap(f, m) -> Functor[A]:
        if m.value == None:
            return Nothing()
        else:
            return Just(f(m.value))

    # Applicative
    def pure(a) -> Monad[A]:
        return Just(a)
    
    def ap(f, x) -> Applicative[A]:
        if f == Nothing or x == Nothing:
            return Nothing
        else:
            return Just(f(x))

    def bind(a: Monad[A], f: Callable[[A], Monad[B]]) -> Monad[B]:
        # Nothing >>= f = Nothing
        # (Just x) >>= f = f x
        if a == Nothing:
            return Nothing()
        elif a == Just:
            return f(a)
        else:
            return Nothing()


def Just(a) -> Maybe[A]:
    return Maybe(a)

def Nothing() -> Maybe[A]:
    return Maybe(None)
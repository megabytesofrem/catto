from blessed.control.Applicative import Applicative
from ..core import *
from ..control.Monad import Monad

@Monad.register
class Identity(Monad[A]):
    '''
    The identity monad
    '''
    def pure(a) -> Monad[A]:
        return Identity(a)

    def bind(a: Monad[A], f: Callable[[A], Monad[B]]) -> Monad[B]:
        return f(a)
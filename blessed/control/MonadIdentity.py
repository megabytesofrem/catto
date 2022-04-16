from ..core import *
from ..data.Functor import Functor
from ..control.Monad import Monad

@Monad.register
class Identity(Monad[A]):
    '''
    The identity monad
    '''
    def pure(a) -> Monad[A]:
        return Identity(a)

    def bind(a: Monad[A], f: Callable[[A], Monad[B]]) -> Monad[B]:
        return f(a.unlift())

    def ap(f, a: Functor[A]) -> Functor[A]:
        return super().ap(a)

    def fmap(f, xs: Functor[A]) -> Functor[A]:
        return super().fmap(xs)
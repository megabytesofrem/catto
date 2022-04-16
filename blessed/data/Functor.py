from ..core import *

class Functor(Generic[A], metaclass=ABCMeta):
    '''
    The Functor typeclass represents the mathematical functor: a mapping between categories in the
    context of category theory. 

    In practice a functor represents a type that can be mapped over.
    Instances should satisfy the following:

    - Identity
        fmap id == id
    - Composition
        fmap (f . g) == fmap f . fmap g
    '''

    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_value(a) -> A:
        return Functor(a)

    def unlift(self) -> A:
        '''
        Unlift a value outside of the context of the functor
        '''
        return self.value

    @abstractmethod
    def fmap(f, xs) -> A:
        pass

@Functor.register
class FunctorList(Functor[List[A]]):
    '''
    Functor instance for lists
    '''
    def fmap(f, xs: Functor[A]) -> Functor[List[A]]:
        return list(map(f, xs))

@Functor.register
class FunctorTuple(Functor[Tuple[A]]):
    '''
    Functor instance for tuples
    '''
    def fmap(f, xs: Functor[A]) -> Functor[Tuple[A]]:
        (fst, snd) = xs
        return (fst, f(snd))
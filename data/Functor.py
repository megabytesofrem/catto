from core import *

class FunctorA(Generic[A]):
    '''
    Internal class to allow us to store a value within the context of a Functor
    '''
    def __init__(self, value: A):
        self.value = value

class Functor(FunctorA[A], metaclass=ABCMeta):
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

    @staticmethod
    def from_value(a: A) -> FunctorA:
        return FunctorA(a)

    @abstractmethod
    def fmap(f, xs) -> A:
        pass

class FunctorList(Functor[List[A]]):
    '''
    Functor instance for lists
    '''
    def fmap(f, xs) -> A:
        return list(map(f, xs))
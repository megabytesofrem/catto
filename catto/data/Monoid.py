from ..core import *
from ..data.Semigroup import Semigroup

class Monoid(Generic[A], Semigroup[A], metaclass=ABCMeta):
    '''
    The class of monoids (types with an associative binary operation that has an identity).
    Instances should satisfy the following:

    - Right identity
        x + mempty = x
    - Left identity
        mempty + x = x
    - Associativity
        x + (y + z) = (x + y) + z (Semigroup law)
    - Concatenation
        mconcat = foldr (+) mempty
    
    '''

    @abstractmethod
    def mempty() -> A:
        pass

    @abstractmethod
    def mappend(a, b) -> A:
        pass
    
    @abstractmethod
    def mconcat(a) -> A:
        pass

@Monoid.register
class MonoidInt(Monoid[int]):
    '''
    Monoid instance for integer under addition
    '''

    def mempty() -> int:
        return 0

    def mappend(a, b) -> int:
        return MonoidInt.sconcat(a,b)

    def mconcat(a: Monoid[A]) -> A:
        return functools.reduce(MonoidInt.mappend, a, MonoidInt.mempty())

@Monoid.register
class MonoidStr(Monoid[str]):
    '''
    Monoid instance for strings
    '''

    def mempty() -> str:
        return ''

    def mappend(a, b) -> str:
        return MonoidStr.sconcat(a,b)

    def mconcat(a: Monoid[A]) -> A:
        return functools.reduce(MonoidStr.mappend, a, MonoidStr.mempty())

@Monoid.register
class MonoidList(Monoid[List[A]]):
    '''
    Monoid instance for lists
    '''

    def mempty() -> List[A]:
        return []

    def mappend(a, b) -> List[A]:
        return MonoidList.sconcat(a,b)

    def mconcat(a: Monoid[A]) -> A:
        return functools.reduce(MonoidList.mappend, a, MonoidList.mempty())
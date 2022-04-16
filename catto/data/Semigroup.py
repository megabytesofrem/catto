from ..core import *

class Semigroup(Generic[A], metaclass=ABCMeta):
    '''
    The class of semigroups (types with an associative binary operation).
    Instances should satisfy the following:

    - Associativity
        x + (y + z) = (x + y) + z
    '''

    @abstractmethod
    def sconcat(a, b): 
        return a + b
from ..core import *
from ..control.Applicative import Applicative

class Monad(Applicative[A], metaclass=ABCMeta):
    '''
    The Monad class defines the basic operations over a monad, 
    a concept from a branch of mathematics known as category theory
    '''

    def __init__(self, value: A):
        self.value = value

    @abstractmethod
    # (>>=) :: m a -> (a -> m b) -> m b
    def bind(a: A, f: Callable[[A], B]) -> B:
        '''
        Sequentially compose two actions, passing any value produced by the first
        as an argument to the second.
        '''
        pass
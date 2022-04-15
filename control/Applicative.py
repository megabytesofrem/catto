from core import *
from data.Functor import *

class Applicative(Functor[A], metaclass=ABCMeta):
    '''
    A functor with application providing operations to
    - embed pure expressions (pure)
    - sequence computations and combine their results (ap)
    '''

    @abstractmethod
    def pure(a) -> Functor[A]:
        '''
        Lift a value
        '''
        return Functor.from_value(a)

    @abstractmethod
    def ap(f, x) -> Functor[A]:
        '''
        Sequential application
        '''
        pass
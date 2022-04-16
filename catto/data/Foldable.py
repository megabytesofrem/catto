from ..core import *
from ..data.Monoid import Monoid, MonoidList

class Foldable(Monoid[A]):
    '''
    The Foldable class represents data structures that can be reduced 
    to a summary value one element at a time.
    '''
    
    @abstractmethod
    def fold(t: A) -> Monoid[A]:  
        pass

@Foldable.register
class FoldableList(Monoid[List[A]]):
    def fold(t: List[A]) -> Foldable[A]:  
        return functools.reduce(MonoidList.mappend, t, MonoidList.mempty())
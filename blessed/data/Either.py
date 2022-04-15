from ..core import *

from ..control.Applicative import Applicative
from ..control.Applicative import Applicative

class Either(Applicative[Generic[A,B]]):
    '''
    The Either type represents value with two possiblities, Either[A,B] is Left(a) or Right(b)

    instance Applicative (Either e) where
        pure             =  Right
        Left  e  <*>  _  =  Left e
        Right f  <*>  r  =  fmap f r
    '''

    def __init__(self, left: A, right: B):
        self.left = left
        self.right = right

    def fmap(f, m) -> A:
        if m.right != None:
            return Right(f(m.right))
        else:
            return Left(m.left)

    # Applicative
    def pure(a) -> A:
        return Right(a)
    
    def ap(f, x) -> A:
        if f == Left:
            return Left(f)
        else:
            return Either.fmap(f, x)

def Left(a) -> Either[A,None]:
    return Either(a,None)

def Right(b) -> Either[None,B]:
    return Either(None,b)

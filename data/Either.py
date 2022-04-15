from core import *
from data.Functor import Functor

class EitherAB(Generic[A,B]):
    '''
    The Either type represents value with two possiblities, Either[A,B] is Left(a) or Right(b)
    '''

    def __init__(self, left: A, right: B):
        self.left = left
        self.right = right

def Left(a) -> EitherAB[A,None]:
    return EitherAB(a,None)

def Right(b) -> EitherAB[None,B]:
    return EitherAB(None,b)

class Either(Functor[EitherAB[A,B]]):
    '''
    Functor instance for Either
    '''

    def fmap(f, m) -> EitherAB[A,B]:
        if m.right != None:
            return Right(f(m.right))
        else:
            return Left(m.left)
from tokenize import maybe
from blessed.core import List

from blessed.data.Maybe import Maybe, Just, Nothing
from blessed.polyfills import polyfill
from blessed.control.Applicative import Applicative
from blessed.control.MonadIdentity import Identity

polyfill()

xs = list.fold([[1,2,3], [4,5,6]])
print(list.tail(xs) + [list.head(xs)])

ys = Maybe.ap(lambda x: Maybe.fmap(lambda y: x.value + y, Just(1)), Just(2))
#print(ys.value.value)

id_ = Identity.bind(Identity.pure(1), 
    lambda x: Identity.bind(Identity.pure(x + 1), lambda y: print(y)))

Maybe.bind(Just(5), lambda x: print(f'We got a Just({x})'))

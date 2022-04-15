from blessed.polyfills import polyfill
from blessed.control.Applicative import Applicative
from blessed.data.Foldable import Foldable
from blessed.data.Maybe import Just, Maybe, Nothing

polyfill()

xs = list.fold([[1,2,3], [4,5,6]])
print(list.tail(xs) + [list.head(xs)])

ys = Maybe.ap(lambda x: Maybe.fmap(lambda y: x.value + y, Just(1)), Just(2))
print(ys.value.value)
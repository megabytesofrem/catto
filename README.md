# Blessed
Blessed library that merges the functional world of Haskell and Python together

## Why is this a thing?
I was bored and was messing around with violating Pythons "type system" on a Discord
call, and had the great idea to make this a library. Please don't *actually* use this

## Example
```py
from blessed.polyfills import polyfill
from blessed.control.Applicative import Applicative
from blessed.data.Foldable import Foldable
from blessed.data.Maybe import Just, Maybe, Nothing

polyfill()

xs = list.fold([[1,2,3], [4,5,6]])
print(list.tail(xs) + [list.head(xs)])

# applicative!
ys = Maybe.ap(lambda x: Maybe.fmap(lambda y: x.value + y, Just(1)), Just(2))
print(ys.value.value)
```

### Whats implemented so far?
- Data.Semigroup
- Data.Monoid
- Data.Functor
- Data.Foldable
- Data.Maybe
- Data.Either
- Control.Applicative (Maybe, Either)
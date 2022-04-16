# Catto
Catto extends Python with concepts from category theory, such as functors, applicatives and monads

## Example
```py
from catto.core import List

from catto.data.Maybe import Maybe, Just, Nothing
from catto.polyfills import polyfill
from catto.control.Applicative import Applicative
from catto.control.MonadIdentity import Identity

polyfill()

xs = list.fold([[1,2,3], [4,5,6]])
print(list.tail(xs) + [list.head(xs)])

ys = Maybe.ap(lambda x: Maybe.fmap(lambda y: x.value + y, Just(1)), Just(2))
#print(ys.value.value)

id_ = Identity.bind(Identity.pure(1), 
    lambda x: Identity.bind(Identity.pure(x + 1), lambda y: print(y)))

Maybe.bind(Just(5), lambda x: print(f'We got a Just({x})'))

```

### Whats implemented so far?
- Data.Semigroup
- Data.Monoid
- Data.Functor
- Data.Foldable
- Data.Maybe
- Data.Either
- Control.Applicative (Maybe, Either)
- Control.Monad (MonadIdentity, Maybe)
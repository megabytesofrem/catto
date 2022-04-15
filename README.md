# Blessed
Blessed library that merges the functional world of Haskell and Python together

## Why is this a thing?
I was bored and was messing around with violating Pythons "type system" on a Discord
call, and had the great idea to make this a library. Please don't *actually* use this

## Example
```py
from data.Monoid import *
from data.Maybe import *
from data.Either import *
from data.Functor import *

from data.Applicative import *

import blessed

# Polyfill/monkey patch Pythons type-system, this allows this
# whole library to be possible
blessed.polyfill()

# mconcat :p
nums = [1,2,3]
more_nums = list.mconcat([nums, [4,5,6]]) # [1,2,3,4,5,6]

# safely deal with error values
def maybe_fail(a, b) -> Maybe[int]:
    if b == 0:
        return Nothing()
    else:
        return Just(a / b)

Maybe.fmap(lambda x: print(f'Result: {x}'), maybe_fail(4,2))

five = Applicative.pure(5)
```

### Whats implemented so far?
- Data.Semigroup
- Data.Monoid
- Data.Functor
- Data.Maybe
- Data.Either
- Control.Applicative (Maybe)
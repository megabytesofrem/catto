'''
Core functionality shared between other modules

Author: megabytesofrem
License: MIT
'''

import functools
from abc import ABCMeta, abstractmethod
from typing import List, Generic, TypeVar, Tuple, Callable

# Define some type aliases
A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')
D = TypeVar('D')
E = TypeVar('E')
F = TypeVar('F')
M = TypeVar('M')
S = TypeVar('S')

def compose(*fns):
    '''
    Function composition
    '''
    return functools.reduce(lambda f,g: lambda x: f(g(x)), fns, lambda x: x)
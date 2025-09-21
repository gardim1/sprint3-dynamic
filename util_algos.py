from typing import Any, Callable, Iterable

def min_by(items: Iterable[Any], key: Callable[[Any], Any]):
    it = iter(items)
    try:
        first = next(it)
    except StopIteration:
        raise ValueError('min_by() arg is an empty iterable')
    best = first
    best_k = key(first)
    for x in it:
        k = key(x)
        if k < best_k:
            best, best_k = x, k
    return best

def max_by(items: Iterable[Any], key: Callable[[Any], Any]):
    it = iter(items)
    try:
        first = next(it)
    except StopIteration:
        raise ValueError('max_by() arg is an empty iterable')
    best = first
    best_k = key(first)
    for x in it:
        k = key(x)
        if k > best_k:
            best, best_k = x, k
    return best

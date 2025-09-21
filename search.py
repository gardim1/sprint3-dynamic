from typing import Any, Callable, List, Optional

def linear_search(items: List[Any], predicate: Callable[[Any], bool]) -> Optional[int]:
    for i, x in enumerate(items):
        if predicate(x):
            return i
    return None

def binary_search(sorted_items: List[Any], key: Callable[[Any], Any], target: Any) -> Optional[int]:
    lo = 0
    hi = len(sorted_items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        k = key(sorted_items[mid])
        if k == target:
            return mid
        elif k < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

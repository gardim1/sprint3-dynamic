from typing import Any, Callable, List

def merge_sort(items: List[Any], key: Callable[[Any], Any]) -> List[Any]:
    n = len(items)
    if n <= 1:
        return items[:]
    mid = n // 2
    left = merge_sort(items[:mid], key)
    right = merge_sort(items[mid:], key)
    return _merge(left, right, key)

def _merge(a: List[Any], b: List[Any], key: Callable[[Any], Any]) -> List[Any]:
    i = j = 0
    out: List[Any] = []
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    while i < len(a):
        out.append(a[i]); i += 1
    while j < len(b):
        out.append(b[j]); j += 1
    return out

def quick_sort(items: List[Any], key: Callable[[Any], Any]) -> List[Any]:
    arr = items[:]
    _qsort(arr, 0, len(arr)-1, key)
    return arr

def _qsort(a: List[Any], lo: int, hi: int, key: Callable[[Any], Any]) -> None:
    if lo >= hi:
        return
    p = _partition(a, lo, hi, key)
    _qsort(a, lo, p-1, key)
    _qsort(a, p+1, hi, key)

def _partition(a: List[Any], lo: int, hi: int, key: Callable[[Any], Any]) -> int:
    pivot = key(a[hi])
    i = lo
    for j in range(lo, hi):
        if key(a[j]) <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i

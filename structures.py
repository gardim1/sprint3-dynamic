from typing import Generic, Iterable, Iterator, List, Optional, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Fila FIFO"""
    def __init__(self, data: Optional[Iterable[T]] = None) -> None:
        self._data: List[T] = list(data) if data else []
        self._head = 0

    def enqueue(self, item: T) -> None:
        self._data.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        item = self._data[self._head]
        self._head += 1
        if self._head > 32 and self._head > len(self._data)//2:
            self._data = self._data[self._head:]
            self._head = 0
        return item

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError('peek from empty queue')
        return self._data[self._head]

    def is_empty(self) -> bool:
        return self._head >= len(self._data)

    def __len__(self) -> int:
        return len(self._data) - self._head

    def __iter__(self) -> Iterator[T]:
        for i in range(self._head, len(self._data)):
            yield self._data[i]


class Stack(Generic[T]):
    """Pilha LIFO"""
    def __init__(self, data: Optional[Iterable[T]] = None) -> None:
        self._data: List[T] = list(data) if data else []

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if not self._data:
            raise IndexError('pop from empty stack')
        return self._data.pop()

    def peek(self) -> T:
        if not self._data:
            raise IndexError('peek from empty stack')
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        for i in range(len(self._data)-1, -1, -1):
            yield self._data[i]

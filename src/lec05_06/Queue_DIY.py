#tbd
from typing import Any
class Queue_DIY:
    def __init__(self, _capacity = 4):
        self._capacity = _capacity
        self.size = 0
        self.data = [None] * self._capacity
        self.head = 0
        self.tail = 0
    
    def pop(self) -> Any:   #poll or dequeue
        if self.size == 0:
            raise IndexError("pop from empty")        
        element = self.data[self.head]
        self.data[self.head]= None
        self.head = (self.head + 1) % self._capacity
        self.size -= 1
        
        if 0 < self.size <= self._capacity // 4:
            self._resize(self._capacity // 2)
            
        return element 
    
    
    def append(self, element: int) -> None:   #offera or enqueue
        if self.size == self._capacity:
            self._resize(2 * self._capacity)
            
        self.data[self.tail] = element
        self.tail = (self.tail + 1) % self._capacity
        self.size += 1 
    
    def peek(self) -> Any:  #peek
        if self.size == 0:
            raise IndexError("peek from empty")
        return self.data[self.head]
    
    def _resize(self, new_capacity:int) -> None:
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.head + i) %self._capacity]
        
        self.data = new_data
        self._capacity = new_capacity
        self.head = 0
        self.tail = self.size
        
    def __repr__(self):
        elems = [
            self.data[(self.head + i) % self._capacity]
            for i in range(self.size)
        ]
        return f"{elems}"
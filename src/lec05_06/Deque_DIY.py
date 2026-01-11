
from typing import Any
class Deque_DIY:
    def __init__(self, _capacity = 4):
        self._capacity = _capacity
        self.size = 0
        self.data = [None] * self._capacity
        self.head = 0
        self.tail = 0
    
    def popleft(self) -> Any:   # in deque popleft = pop in queue
        if self.size == 0:
            raise IndexError("pop from empty")        
        element = self.data[self.head]
        self.data[self.head]= None
        self.head = (self.head + 1) % self._capacity
        self.size -= 1
        
        if 0 < self.size <= self._capacity // 4:
            self._resize(max(4, self._capacity // 2))
            
        return element 
    
    def pop(self) -> Any:   # in deque pop = pop in stack
        if self.size == 0:
            raise IndexError("pop from empty")    
        idx = (self.tail - 1) % self._capacity    
        element = self.data[idx]
        self.data[idx]= None
        self.tail = idx
        self.size -= 1
        
        if 0 < self.size <= self._capacity // 4:
            self._resize(max(4, self._capacity // 2))
            
        return element 

    def appendleft(self, element: int) -> None:   # in deque appendleft = offer in queue
        if self.size == self._capacity:
            self._resize(2 * self._capacity)
         
        self.head = (self.head - 1) % self._capacity    
        self.data[self.head] = element
        self.size += 1 
    
    def append(self, element: int) -> None:    # in deque append = add in stack
        if self.size == self._capacity:
            self._resize(2 * self._capacity)
            
        self.data[self.tail] = element
        self.tail = (self.tail + 1) % self._capacity
        self.size += 1 
   
    
    def peek(self) -> Any:  #peek
        if self.size == 0:
            raise IndexError("peek from empty")
        return self.data[(self.tail - 1) % self._capacity]
     
    def peekleft(self) -> Any:  #peek
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
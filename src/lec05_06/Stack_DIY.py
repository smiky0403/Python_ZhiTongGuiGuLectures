#tbd
from typing import Any

class Stack_DIY:
    
    def __init__(self, _capacity = 4):
        self._capacity = _capacity
        self.size = 0
        self.data = [None] * self._capacity
        
    def push(self, element:Any) -> None:
        
        if self.size >= self._capacity:
            self._resize(self._capacity* 2)
        #self.data.append(element)
        self.data[self.size] = element
        self.size += 1
        
    def pop(self) -> Any:
        if self.size == 0:
            raise IndexError("pop from empty stack")
        
        element = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        #self.data.pop()
        if self.size > 0 and self.size <= self._capacity // 4:
            self._resize(max(4, self._capacity // 2))
            
        return element
    
    
    def peek(self) -> Any:
        if self.size == 0:
            raise IndexError("peek from empty stoack")     
        
        return self.data[self.size -1]
        
    def _resize(self, new_capacity: int):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self._capacity = new_capacity
        
    def __repr__(self):
        return f"{self.data[:self.size]}"
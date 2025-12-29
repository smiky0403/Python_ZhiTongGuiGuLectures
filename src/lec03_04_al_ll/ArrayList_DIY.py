class ArrayList_DIY:
    
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        
    def get(self, index):
        self.check_index(index)
        return self.data[index]
    
    def set(self, index, value):
        self.check_index(index)
        self.data[index] = value
        
    
    def add(self, value):
        if self.size >= self.capacity:
            self.resize()
        
        self.data[self.size] = value
        self.size += 1
        return 0
       
    def add_at(self, index, value):
        self.check_index(index)
        if self.size >= self.capacity:
            self.resize()      
        
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
            
        self.data[index] = value 
        self.size += 1
        
            
    def remove_at(self, index):
        self.check_index(self, index)      
        for i in range(index, self.size - 1, 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size] = None
        self.size -= 1
                
    def check_index(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Out of Bound")

    def resize(self):
        print("resizing")
        self.capacity *= 2
        new_data = [None]*self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        
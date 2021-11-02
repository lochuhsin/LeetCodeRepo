# My solution, easy thought

class OrderedStream:

    def __init__(self, n: int):
        self.index = 0
        self.container = [None for i in range(n)]
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.container[idKey-1] = value  #O(1)
        
        
        # O(N)
        chunk = []
        while self.index < len(self.container) and self.container[self.index] is not None :
            chunk.append(self.container[self.index])
            self.index += 1
        return chunk

'''
This uses dynamic arr (python lists)

Most of the concept are same as my original one,
But still cannot figure out why bound ?
O(1) for every operation, but not memory efficient ( the history contains
large of un-used url)

'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0
        self.bound = 0

    def visit(self, url: str) -> None:

        self.index += 1
        if self.index == len(self.history):
            self.history.append(url)
        else:
            self.history[self.index] = url
        
        self.bound = self.index

    def back(self, steps: int) -> str:

        self.index = max(self.index - steps, 0)
        return self.history[self.index]


    def forward(self, steps: int) -> str:

        self.index = min(self.index + steps, self.bound)
        return self.history[self.index]


'''
Two Stack solution
'''

'''
Linked list solution
'''

'''
Doubly linked list solution
'''

'''
Stack with two pointer
'''
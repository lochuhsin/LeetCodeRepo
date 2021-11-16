'''
Easy solution using recursive, for every recursive
check is the element is integer. If the element is integer
append to list. Else, using getlist() api do recursive.
'''

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.val_list = []
        self.index = 0
        
        self._flatten(nestedList)
    
    def next(self) -> int:
        val = self.val_list[self.index]
        self.index += 1
        return val
    
    def hasNext(self) -> bool:
        return self.index < len(self.val_list)
        
    def _flatten(self, nested):
        
        for element in nested:
            if element.isInteger():
                self.val_list.append(element.getInteger())
            else:
                nested_list = element.getList()
                self._flatten(nested_list)

'''
Smart solutions with stack, the advantage is not constructing
another datastructure that contains the hole element.
'''
class NestedIterator:
    
    def __init__(self, nestedList: [NestedInteger]):
    	# to remind that, the reason of using reversed
    	# is because using stack. the pop() function gets the
    	# element from the last
        self.stack = list(reversed(nestedList))
        
        
    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.stack.pop().getInteger()        
    
        
    def hasNext(self) -> bool:
        # to make sure that the next element is integer
        # execute self.make_stack_top_an_integer()
        self.make_stack_top_an_integer()
        return len(self.stack) > 0
        
        
    def make_stack_top_an_integer(self):
        while self.stack and not self.stack[-1].isInteger():
            element = self.stack.pop().getList()
            # The reason is same here
            self.stack.extend(reversed(element))


"""
Brillian usage of generators
"""
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        # Get a generator object from the generator function, passing in
        # nestedList as the parameter.
        self._generator = self._int_generator(nestedList)
        # All values are placed here before being returned.
        self._peeked = None

    # This is the generator function. It can be used to create generator
    # objects.
    def _int_generator(self, nested_list) -> "Generator[int]":
        # This code is the same as Approach 1. It's a recursive DFS.
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                # We always use "yield from" on recursive generator calls.
                yield from self._int_generator(nested.getList())
        # Will automatically raise a StopIteration.
    
    def next(self) -> int:
        # Check there are integers left, and if so, then this will
        # also put one into self._peeked.
        if not self.hasNext(): return None
        # Return the value of self._peeked, also clearing it.
        next_integer, self._peeked = self._peeked, None
        return next_integer
        
    def hasNext(self) -> bool:
        if self._peeked is not None: return True
        try: # Get another integer out of the generator.
            self._peeked = next(self._generator)
            return True
        except: # The generator is finished so raised StopIteration.
            return False
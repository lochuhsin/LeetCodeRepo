'''
This is a demonstation of the usage of trie created by myself.
1. Create a trie to store multiple words.
2. loop the text
3. If char (text char) in node.children that means this branch contains the
character. change the pointer to the next level node, at the meantime the index
goes on. If char not in node.children just simple break.
'''


class trie(object):
    
    def __init__(self):
        
        self.children = {}
        self.is_complete = False
        
    @staticmethod    
    def build(words: list):
        
        root = trie()
        for word in words:
            pointer = root
            for char in word:
                if char not in pointer.children:
                    pointer.children[char] = trie()
                pointer = pointer.children[char]
            pointer.is_complete = True
        return root

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        root = trie.build(words)
        
        result_list = []
        
        for l in range(len(text)):
            node = root
            for r in range(l, len(text)):
                if text[r] not in node.children:
                    break    
                node = node.children[text[r]]
                if node.is_complete:
                    result_list.append([l, r])
        return result_list
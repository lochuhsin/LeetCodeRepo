from collections import defaultdict


class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ""


class FileSystem(object):

    def __init__(self):
        self.root = Node()

    def find(self, path):  # find and return node at path.
        curr = self.root
        if len(path) == 1:
            return self.root

        for word in path.split("/")[1:]:
            curr = curr.child[word]

        return curr

    def ls(self, path):
        curr = self.find(path)
        if curr.content:  # file path,return file name
            return [path.split('/')[-1]]
        return sorted(curr.child.keys())

    def mkdir(self, path):
        self.find(path)

    def addContentToFile(self, filePath, content):
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath):
        curr = self.find(filePath)

        return curr.content

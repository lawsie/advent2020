with open("input.txt") as f:
    data = f.readlines()

data = [int(n.strip()) for n in data]
data.sort()

# You now have a sorted list of integers

class Node():

    def __init__(self, data=None):
        self._data = data
        self._branches = []
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, newdata):
        self._data = newdata

    @property
    def branch(self):
        return self._branches
    
    @branch.setter
    def branch (self, newbranch):
        self._branches.append(newbranch)
    
    def print_tree(self):
        print(self._data)
        for branch in self._branches:
            branch.print_tree()


root = Node(0)
root.print_tree()

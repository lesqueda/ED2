
class Node():
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

    def insert(self):
        pass
    #carlos gonzalez y eduardo paris
    def inorder(self, value):
    if a==None:
        return None
    else:
        self.inorder(a.left)
        print(a.dato)
        self.inorder(a.right)
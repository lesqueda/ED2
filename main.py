
class Node():
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

    def insert(self, value):
        if self.value:
            if value>self.value:
                if self.right==None:
                    self.right=Node(value)
                else:
                    self.right.insert(value) #Recursividad
            if value<self.value:
                if self.left==None:
                    self.left=Node(value)
                else:
                    self.left.insert(value) 
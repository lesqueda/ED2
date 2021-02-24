
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
   inorder
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

#Francisco, Miguel, Jorge, Jairo
    def postorden(nodo):
        if  node.value!= None:
            postorden(nodo.left())
            postorden(nodo.right())
            print(nodo.value)
     #

class Node():
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
    class arbol():
    def __init__(self):
        self.root = None

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

tree = arbol()

#Muestra las opciones de recorrido y tratamiento del árbol
while True:
    os.system("cls")
    print("Arbol Binario. Opciones:")
    opt = input("\n1.-Insertar nodo \n2.-Mostrar recorridos de árbol \n3.-Buscar \n4.-Salir \n\nPor favor elija una opcion -> ")

    if opt == '1':
        nodo = input("\nIngrese el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngrese solo digitos...")
    elif opt == '2':
        if tree.root == None:
            print("Vacio")
        else:
            print("Recorrido inorder")
            tree.inorder(tree.root)
            print("Recorrido preorder")
            tree.preorder(tree.root)
            print("Recorrido postorder")
            tree.postorder(tree.root)
    elif opt == '3':
        nodo = input("\nIngrese el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngrese solo digitos...")        
    elif opt == '4':
        print("\nGracias por participar. Adios.\n")
        os.system("pause")
        break
    else:
        print("\nElija una opcion correcta...")
    print()
    os.system("pause")

print()


class Nodo():
    def __init__(self, valor):
        self.valor=valor
        self.izq=None
        self.derecha=None

    def insert(self, valor):
        if self.valor:
            if valor<self.valor:
                if self.izq==None:
                    self.izq=Nodo(valor)
                else:
                    self.izq.insert(valor) 
            if valor>self.valor:
                if self.derecha==None:
                    self.derecha=Nodo(valor)
                else:
                    self.derecha.insert(valor) 
        else:
            self.valor=valor

    #carlos gonzalez y eduardo paris
    def inorder(self,valores):
        if self.izq:
            self.izq.inorder(valores)
        valores.append(self.valor)
        if self.derecha:
            self.derecha.inorder(valores)

    #preorder Jhosh Gómez Taller
    def preorder(self,valores):
        valores.append(self.valor)
        if self.izq:
            self.izq.preorder(valores)
        if self.derecha:
            self.derecha.preorder(valores)
                
    #Francisco, Miguel, Jorge, Jairo
    def postorden(self, valores):
        if self.izq:
            self.izq.postorden(valores)
        if self.derecha:
            self.derecha.postorden(valores)
        valores.append(self.valor)

#Muestra las opciones de recorrido y tratamiento del árbol
if __name__=="__main__":
    root=None
    sentinel=True
    while not root:
        root=Nodo(int(input("Bienvenido a Arbol Binario. Por favor, introduce tu valor raiz: ")))
    while sentinel:
        valores=[]
        opc=input("\n ¿Que accion deseas realizar ahora? \n 1. Insertar un valor al arbol \n 2. Recorrido Inorden \n 3. Recorrido Post Orden \n 4. Recorrido Preorden \n 5. Salir \n Opción: ")
        if opc=="1":
            valor=int(input("Introduce un valor: "))
            root.insert(valor)
            print(f"Valor '{valor}' insertado con exito")
        if opc=="2":
            root.inorder(valores)
            print("-".join([str(valor) for valor in valores]))
        if opc=="3":
            root.postorden(valores)
            print("-".join([str(valor) for valor in valores]))
        if opc=="4":
            root.preorder(valores)
            print("-".join([str(valor) for valor in valores]))
        if opc=="5":
            sentinel=False

# Não sei como o minimum e o maximum funcionam com esse código
# e também acho que o tree successor e o tree 
# predeccessor não estão funcionando, mas está aí
# o que anotei das aulas. Até tentei de outras formas
# com outros algoritmos mas ainda não funcionava. 
# Desculpe desde já. 

class Node(): # cria nó 
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.pai = None

    def __str__(self) -> str:
        return str(self.chave)

class Tree(): # inicia a arvore com o nó raiz
    def __init__(self):
        self.raiz = None # raiz começa None

    # inserção, transplante, remoção e busca. 
    def TreeInsert(self, chave, node=None): # insere um nó na árvore
        
        if (node is None):
            node = self.raiz

        if (self.raiz is None):
            self.raiz = Node(chave)

        else:
            if (chave <= node.chave):
                if (node.esquerda is None):
                    node.esquerda = Node(chave)

                else:
                    return self.TreeInsert(chave, node=node.esquerda)
            else:
                if (node.direita is None):
                    node.direita = Node(chave)

                else:
                    return self.TreeInsert(chave, node=node.direita)


    def tree_transplant(self, u, v): # transplanta uma parte 

        if (u.pai == None):
            self.raiz = v
        elif (u.pai.esquerda == u):
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        
        if (v != None):
            v.pai = u.pai


    def tree_remove(self, z): # remove uma parte

        if (z.esquerda == None):
            self.tree_transplant(z, z.direita)
        elif (z.direita == None):
            self.tree_transplant(z, z.esquerda)
        else:
            y = self.minumum(z.direita)

            if(y.pai!=z):
                self.tree_transplant(y, y.direita)
                y.direita = z.direita
                y.direita.pai = y
            self.tree_transplant(z, y)
            y.esquerda = z.esquerda
            y.esquerda = z.esquerda
            y.esquerda.pai = y


    def interative_tree_search(self, chave): # busca binária iterativa

        if (self.raiz == None):
            return None
        vertice = self.raiz

        while (vertice != None and vertice.chave != int(chave)):
            if (int(chave) < vertice.chave):
                vertice = vertice.esquerda
            else:
                vertice = vertice.direita
        
        return vertice

    # caminhada pela árvore: in-order, decrescente, pré-order e pós-order

    def inorder_tree_walk(self, vertice=None): # esquerda, raiz, direita

        if (self.raiz == None):
            return
        if (vertice == None): # começa na raiz
            vertice = self.raiz
        if (vertice.esquerda != None):
            self.inorder_tree_walk(vertice = vertice.esquerda)
        print(vertice) # meio
        if (vertice.direita != None):
            self.inorder_tree_walk(vertice = vertice.direita)

        return vertice


    def decrescente_tree_walk(self, vertice=None): # retorna em ordem decrescente 

        if (self.raiz == None):
            return
        if (vertice == None):
            vertice = self.raiz
        if (vertice.direita != None):
            self.decrescente_tree_walk(vertice = vertice.direita)
        print(vertice)
        if (vertice.esquerda != None):
            self.decrescente_tree_walk(vertice = vertice.esquerda)
        
        return vertice


    def preorder_tree_walk(self, vertice=None): # raiz, esquerda, direita

        if (self.raiz == None):
            return
        if (vertice == None):
            vertice = self.raiz
        print(vertice)
        if (vertice.esquerda != None):
            self.preorder_tree_walk(vertice=vertice.esquerda)
        if (vertice.direita != None):
            self.preorder_tree_walk(vertice=vertice.direita)
        return vertice


    def posorder_tree_walk(self, vertice=None): # esqueda, direita, raiz

        if (self.raiz == None):
            return
        if (vertice == None):
            vertice = self.raiz
        if (vertice.esquerda != None):
            self.posorder_tree_walk(vertice=vertice.esquerda)
        if (vertice.direita != None):
            self.posorder_tree_walk(vertice=vertice.direita)
        print(vertice)

    # mininum e maximum 

    def mininum_recursiva(self, vertice=None):
        if (vertice.esquerda is None):
            return vertice
        else:
            return self.mininum_recursiva(vertice=vertice.esquerda)
        

    def tree_mininum(self, vertice=None):
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        while (vertice.esquerda is not None):
            vertice = vertice.esquerda
        return vertice


    def tree_maximun(self, vertice=None):
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        while (vertice.direita is not None):
            vertice = vertice.direita
        return vertice

    '''    
    teste de outro tree minimum
    

    def minimo(self, vertice):
        current = vertice

        while (current is not None):
            if (current.esquerda is not None):
                break
            current = current.esquerda
        return current
    '''
    # tree-sucessor e tree-predecessor

    def tree_successor(self, vertice=None):
        if (vertice.direita is not None):
            return self.tree_mininum(vertice=vertice.direita)
        y = vertice.pai

        while (y is not None and vertice == y.direita):
            vertice = y
            y = vertice.pai

        return y


    def tree_predeccessor(self, vertice=None):
        if (vertice.esquerda is not None):
            return self.tree_maximum(vertice=vertice.esquerda)
        y = vertice.pai

        while (y is not None and vertice == y.esquerda):
            vertice = y
            y = vertice.pai

        return y
    

# testes na arvore
arvore = Tree()
arvore.TreeInsert(10)
arvore.TreeInsert(13)
arvore.TreeInsert(14)
arvore.TreeInsert(8)
arvore.TreeInsert(9)
arvore.TreeInsert(7)
arvore.TreeInsert(11)
arvore.TreeInsert(72)

'''
                         10
                          
                      8      13
                            
                   7    9  11   14
                                 
                                  72


'''
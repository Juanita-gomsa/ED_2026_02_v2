from collections import deque

from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    if T.is_empty():
        return True

    fila = deque([T.root()])
    vio_hueco = False

    while fila:
        p = fila.popleft()
        for hijo in (T.left(p), T.right(p)): 
            if hijo is None:
                vio_hueco = True
            else:
                if vio_hueco:                
                    return False
                fila.append(hijo)
    return True


def camino(T, p, q):
    subida = []   
    bajada = []   

    while p != q:
        if T.depth(p) >= T.depth(q):
            subida.append(p)
            p = T.parent(p)
        else:
            bajada.append(q)
            q = T.parent(q)

    nodos = subida + [p] + bajada[::-1]
    return " -> ".join(str(x.element()) for x in nodos)


if __name__ == "__main__":
    # tus pruebas (opcional)
    T = LinkedBinaryTree()
    a = T._add_root('A')
    b = T._add_left(a, 'B')
    c = T._add_right(a, 'C')
    d = T._add_left(b, 'D')
    print(es_completo(T))          # True
    print(camino(T, d, c))         # D -> B -> A -> C

import matplotlib.pyplot as plt


class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        ih = len(self.arreglo) - 1
        hijo = self.arreglo[ih]
        ip = ih // 2
        padre = self.arreglo[ip]
        while hijo < padre:
            self.arreglo[ih], self.arreglo[ip] = self.arreglo[ip], self.arreglo[ih]
            ih = ip
            ip = ih // 2
            hijo = self.arreglo[ih]
            padre = self.arreglo[ip]
        if imagen:
            self.dibujar()

    def _hundir(self, n):
        largo = len(self.arreglo)
        hijo_izq = 2 * n
        hijo_der = 2 * n + 1
        mas_peque = n

        # Buscar si el hijo izquierdo es menor
        if hijo_izq < largo and self.arreglo[hijo_izq] < self.arreglo[mas_peque]:
            mas_peque = hijo_izq

        # Buscar si el hijo derecho es menor
        if hijo_der < largo and self.arreglo[hijo_der] < self.arreglo[mas_peque]:
            mas_peque = hijo_der

        # Si el menor no es el nodo actual, intercambiamos y seguimos bajando
        if mas_peque != n:
            self.arreglo[n], self.arreglo[mas_peque] = self.arreglo[mas_peque], self.arreglo[n]
            self._hundir(mas_peque)

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) <= 1:
            if imagen:
                self.dibujar()
            return None

        val_min = self.arreglo[1]

        ultimo_elemento = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo_elemento
            self._hundir(1)

        if imagen:
            self.dibujar()
        return val_min

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')]
        for x in lista:
            self.arreglo.append(x)
        ultimo = len(self.arreglo) - 1
        i = ultimo // 2
        while i >= 1:
            self._hundir(i)
            i = i - 1

        if imagen:
            self.dibujar()

    def dibujar(self):
        cantidad = len(self.arreglo) - 1
        plt.figure(figsize=(10, 4))
        plt.axis('off')

        if cantidad == 0:
            plt.text(0.5, 0.5, 'Heap vacio', ha='center', fontsize=14)
            plt.show()
            return

        # Primero se calcula dónde va cada nodo
        xs = {}
        ys = {}
        for i in range(1, cantidad + 1):
            nivel = 0
            while 2 ** (nivel + 1) <= i:
                nivel = nivel + 1
            puesto = i - 2 ** nivel               # qué lugar ocupa dentro de su nivel
            xs[i] = (puesto + 0.5) / 2 ** nivel   # izquierda a derecha
            ys[i] = -nivel                        # cada nivel más abajo

        # Las aristas: cada nodo (menos la raíz) se une con su padre
        for i in range(2, cantidad + 1):
            padre = i // 2
            plt.plot([xs[padre], xs[i]], [ys[padre], ys[i]], color='black', zorder=1)

        # Los nodos con su valor
        for i in range(1, cantidad + 1):
            plt.scatter(xs[i], ys[i], s=700, color='white', edgecolors='blue', zorder=2)
            plt.text(xs[i], ys[i], str(self.arreglo[i]), ha='center', va='center', zorder=3)

        # Márgenes para que no se corten los círculos de las orillas
        plt.xlim(-0.05, 1.05)
        plt.ylim(min(ys.values()) - 0.5, 0.5)
        plt.show()

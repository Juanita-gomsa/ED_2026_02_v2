class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
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

    def _hundir(self, n):
        largo = len(self.arreglo)
        hijo_izq = 2 * n
        hijo_der = 2 * n + 1
        mas_peque = n

        if hijo_izq < largo and self.arreglo[hijo_izq] < self.arreglo[mas_peque]:
            mas_peque = hijo_izq

        # Buscar si el hijo derecho es menor
        if hijo_der < largo and self.arreglo[hijo_der] < self.arreglo[mas_peque]:
            mas_peque = hijo_der

        # Si el menor no es el nodo actual, intercambiamos y seguimos bajando
        if mas_peque != n:
            self.arreglo[n], self.arreglo[mas_peque] = self.arreglo[mas_peque], self.arreglo[n]
            self._hundir(mas_peque)

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None

        val_min = self.arreglo[1]

        ultimo_elemento = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo_elemento
            self._hundir(1)

        return val_min



    def build_heap(self, lista):
        pass

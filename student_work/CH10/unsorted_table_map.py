class UnsortedTableMap:
    # Diccionario implementado desde cero con una lista no ordenada
    # de entradas [clave, valor].

    def __init__(self):
        # Crea un diccionario vacío.
        self._table = []                  # lista de entradas [clave, valor]

    # ---------- auxiliar ----------
    def _buscar(self, k):
        # Retorna el índice de la entrada con clave k,
        # o -1 si no existe.
        for i in range(len(self._table)):
            if self._table[i][0] == k:
                return i
        return -1

    # ---------- núcleo: métodos especiales ----------
    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        # M[k]  (KeyError si no existe)
        ind = self._buscar(k)

        if ind == -1:
            raise KeyError("El valor no existe")

        return self._table[ind][1]

    def __setitem__(self, k, v):
        # M[k] = v  (inserta o reemplaza)
        ind = self._buscar(k)

        if ind == -1:
            self._table.append([k, v])
        else:
            self._table[ind][1] = v

    def __delitem__(self, k):
        # del M[k]  (KeyError si no existe)
        ind = self._buscar(k)

        if ind == -1:
            raise KeyError("El valor no existe")

        self._table.pop(ind)

    def __contains__(self, k):
        # k in M
        return self._buscar(k) != -1

    def __iter__(self):
        # for k in M  (genera las claves)
        for entrada in self._table:
            yield entrada[0]

    def __eq__(self, otro):
        if len(self) != len(otro):
            return False

        for k in self:
            if k not in otro or self[k] != otro[k]:
                return False
        return True


    # ---------- dado ----------
    def __repr__(self):
        return '{' + ', '.join(f'{k!r}: {v!r}' for k, v in self._table) + '}'

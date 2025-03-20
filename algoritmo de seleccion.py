#ALGORITMO DE SELECCION REALIZADO EN CLASES

class SelectionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(len(self.data)):
            min_idx = min(range(i, len(self.data)), key=self.data.__getitem__)
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
        return self.data

# Ejemplo de uso
if __name__ == "__main__":
    lista = [29, 10, 14, 37, 13]
    sorter = SelectionSort(lista)
    print("Lista ordenada:", sorter.sort())
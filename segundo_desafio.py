#***Segundo desafio***

# Agora sua lista de 500 números não estão ordenados.
#>>lista = [randint(0, 5000000) for x in range(500)]
#E você recebe uma outra lista com 50000 números também aleatórios.
#>>lista = [randint(0, 5000000) for x in range(50000)]
#Sua tarefa é para cada item da segunda lista, imprimir quais destes
#números estão na primeira lista recebido.

from random import randint

class Segundo_desafio():

    def __init__(self):

        self.list1 = [randint(0, 5000000) for x in range(500)]
        self.list2 = [randint(0, 5000000) for x in range(50000)]
        self.find_intersection()

    def find_intersection(self):
        intersec = [num for num in self.list1 if num in self.list2]
        print ("Segundo Desafio: ", intersec)


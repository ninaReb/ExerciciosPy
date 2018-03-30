# ***Primeiro desafio***

# Você recebe uma lista de 300 números ordenados por ordem crescente.
# Sua tarefa é achar um número aleatório informado pelo usuário da
# maneira mais eficiente possível.

#digitar os números do array. ex: 1,2,3,4
# def get_array():
#     text = input("digite os numeros")
#     my_array = text.split(',')
#     my_array = [int(i) for i in my_array]
#     print (my_array)
#     return my_array
#

class Primeiro_desafio():

    def __init__(self, array):
        self.my_array = array
        self.number = int(input("digite o numero"))
        self.find_number()


    def find_number(self):
        number = self.number
        if number in self.my_array:
            position = self.my_array.index(number)
            print("O número {} está na posição [{}] da lista".format(number, position))
        else:
            print("O número não foi encontrado na lista")














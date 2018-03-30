
# ***Quarto desafio***

# Neste problema você deve ler um conjunto de palavras, onde cada palavra
# é composta somente por letras no intervalo a-z e A-Z. Cada letra possui
# um valor específico, a letra a vale 1, a letra b vale 2 e assim por diante,
#  até a letra z, que vale 26. Do mesmo modo, a letra A vale 27, a letra B vale
#  28 e a letra Z vale 52.

# Você deve escrever um programa para determinar se uma palavra é uma palavra
#  prima ou não. Uma palavra é uma palavra prima se a soma de suas letras é um
#  número primo

import random

class Quarto_desafio:

    def __init__(self, name):
        self.folder_name = name
        self.word = self.get_word_from_list(self.folder_name)
        self.check_for_prime()

    def get_word_from_list(this, folder_name):
        folder = open(folder_name, "r")
        words = []
        for lines in folder:
            lines = lines.strip()
            words.append(lines)
        folder.close()
        pos = random.randrange(0, len(words))
        word = words[pos]
        return list(word)

    def give_values(self):
        values = {chr(i): i + 1 for i in range(ord("a"), ord("a") + 26)}
        values.update({chr(i): i + 1 for i in range(ord("A"), ord("A") + 26)})
        for i in values:
            values[i] = (ord(i) - ord('a')) + 1
            if ord(i) < ord('a'):
                values[i] = abs(ord(i) + ord('a') - 135)
        # print(values)
        return values

    def add_word(self):
        values = self.give_values()
        sum = 0
        for char in self.word:
            sum += values[char]
        print(self.word, " = ", sum)
        return sum

    def check_for_prime(self):
        word_value = self.add_word()
        for i in range(2, word_value):
            if (word_value % i) == 0:
                print( word_value, "não é primo")
                break
            else:
                print( word_value, " é primo")
                break












#digitando a palavra para testar
# word = list(input("Digite sua Palavra").strip())
#
#
# #caso seja necessário pegar uma palavra aleatória de um arquivo .txt (segue arquivo palavras.txt como exmplo)

# def give_values():
#     values = {chr(i): i + 1 for i in range(ord("a"), ord("a") + 26)}
#     values.update({chr(i): i + 1 for i in range(ord("A"), ord("A") + 26)})
#     for i in values:
#         values[i] = (ord(i) - ord('a')) + 1
#         if ord(i) < ord('a'):
#             values[i] = abs(ord(i) + ord('a') - 135)
#     #print(values)
#     return values
#
# def add_word():
#     values = give_values()
#     sum = 0
#     for char in word:
#         sum += values[char]
#     print(word, " = ", sum)
#     return sum
#
# def check_for_prime():
#     word_value = add_word()
#     for i in range(2, word_value):
#         if (word_value % i) == 0:
#             print(word_value, "não é primo")
#             break
#         else:
#             print(word_value, " é primo")
#             break
#
# check_for_prime()

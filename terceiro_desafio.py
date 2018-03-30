#***Terceiro desafio***
#Sua tarefa agora é dado um número qualquer imprimir todos os números
 #primos até o número dado.

class Terceiro_desafio():

    def __init__(self):
        self.lim = int(input("Terceiro desafio: Defina o número "))
        self.find_primes()

    def find_primes(self):
        prime_list = []
        for num in range(2,self.lim):
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    prime_list.append(num)
                    break
        print("Numeros primos:", prime_list)








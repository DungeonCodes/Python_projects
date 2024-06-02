import random
class Mylist(list):#herda todos os metodos da classe list
    def choise(self):
        return random.choice(self)

l = Mylist([1, 3, 2, 6])


print(l)
print(l.choise())


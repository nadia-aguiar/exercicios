#Exercise Question 1: Reverse the following tuple.

tupla_reverse = (0, 2, 4, 5, 6, 7)
tuple(sorted(tupla_reverse, reverse = True))

#Exercise Question 2: Access value 20 from the following tuple.

tupla2 = ("palavra legal", [3, 20, 7, 0], (1, 2, 3))
tupla2[1][1]

#Exercise Question 3: Create a tuple with single item 50.

tupla_single = (50,)
tupla_single

#Exercise Question 4: Unpack the following tuple into 4 variables.

tupla3 = ("Janeiro", "Fevereiro", "Março", "Abril")
print(tupla3[0])
print(tupla3[1])
print(tupla3[2])
print(tupla3[3])


#Exercise Question 5: Swap the following two tuples.

tupla = (0, 1)
tupla1 = (20, 21)
tupla, tupla1 = tupla1, tupla
print(tupla)
print(tupla1)


#Exercise Question 6: Copy element 44 and 55 from the following tuple into a new tuple.

a_tupla = (10, 25, 30, 44, 55, 60)
b_tupla = a_tupla[3],a_tupla[4]
b_tupla

#Exercise Question 7: Modify the first item (22) of a list inside a following tuple to 222.

a_tupla = (11, [22, 33], 44, 55)
a_tupla[1][0] = (222)
a_tupla

#Exercise Question 8: Sort a tuple of tuples by 2nd item.

tupla1 = (("a", 10), ("b", 2), ("c", 33), ("d", 7))
sorted(tupla1, key=lambda tupla:tupla[1])

#Exercise Question 9: Counts the number of occurrences of item 8 from a tuple.

tupla = (2, 10, 7, 7, 8, 8, 8)
tupla.count(8)

#Exercise Question 10: Check if all items in the following tuple are the same.

def confere(tuplex):
    return all (i == tuplex[0] for i in tuplex)
minha_tupla = (10, 10, 10, 10)
print(confere(minha_tupla))

#1. Write a Python program to create a tuple. 

tupla = ()
tupla = tuple()

#2. Write a Python program to create a tuple with different data types.

tupla = ([1, 2, 3], ("a", "b", 2))
tupla

#3. Write a Python program to create a tuple with numbers and print one item.

tupla_num = (10, 20, 30)
tupla_num [1]

#4. Write a Python program to unpack a tuple in several variables.

tupla = ("casa", "apartamento", "loja")
n1, n2, n3 = tupla
print(n1, n2, n3)

#5. Write a Python program to add an item in a tuple.

tupla = (2, 4, 6, 5)
nova_tupla = tupla + (10,)
nova_tupla

#6. Write a Python program to convert a tuple to a string. 

tupla = ("hoje é dia de maria")
str = "".join(tupla)
str

#7. Write a Python program to get the 4th element and 4th element from last of a tuple.

tupla = (10, 12, 14, 20, 17,-5, 8, 0, 9, 12)
tupla [3], tupla[-3]

#9. Write a Python program to find the repeated items of a tuple.

def repeat(alguma_tupla):
   x = []
   for i in alguma_tupla:
       if alguma_tupla.count(i)>1 and i not in x:
           x.append(i)
   return tuple(x)

tupla_repeat = (2, 2, 2, 45, 1, 1, 1)
repeat(tupla_repeat)

#10. Write a Python program to check whether an element exists within a tuple.

tupla = (5, 2, 7, 50, 23)
5 in tupla

#11. Write a Python program to convert a list to a tuple.

lista = ["isso é uma tupla"]
tupla = tuple(lista)
tupla

#12. Write a Python program to remove an item from a tuple.

tupla = (50, 100, 150, 11)
tupla = list(tupla)
tupla.remove(11)
tupla = tuple(tupla)
tupla

#13. Write a Python program to slice a tuple.

minha_tupla = ((1, 2, 3, ),("beijinho", "cajuzinho", "brigadeiro"))
print(minha_tupla[1])
print(minha_tupla[0])

#14. Write a Python program to find the index of an item of a tuple.

minha_tupla = (1, 2, 5, 10, 11, )
minha_tupla.index(5)

#15. Write a Python program to find the length of a tuple.

tupla_tamanho = ((1, 2, 3, ),("beijinho", "cajuzinho", "brigadeiro"))
len(tupla_tamanho)

#16. Write a Python program to convert a tuple to a dictionary.

tupla = ("x",55), ("y", 40), ("z", 58)
dicionario = dict(tupla)
dicionario

#18. Write a Python program to reverse a tuple.

tupla = (1, 2, 3, 4, 5, 6)
tupla_b = sorted(tupla, reverse = True)
tupla_b = tuple(tupla_b)
tupla_b

#19. Write a Python program to convert a list of tuples into a dictionary.

lista_tupla = [("dia", 20), ("mes", 2), ("ano", 1986)]
dicio = dict(lista_tupla)
dicio

#20. Write a Python program to print a tuple with string formatting.

tupla = (2, 4, 6)
print(f"Isso é uma tupla: {tupla}")

#21. Write a Python program to replace last value of tuples in a list.

lista_tupla = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print([t[:-1] + (100,) for t in lista_tupla])
#olhei a resposta#

#22. Write a Python program to remove an empty tuple(s) from a list of tuples.

abobrinha = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
abobrinha.remove(())
abobrinha
# porque tirou só um?#

#23. Write a Python program to sort a tuple by its float element.

lista_float = [('segunda', 12.20), ('terça', 15.10), ('quarta', 24.5)]
sorted(lista_float, key = lambda x: x[1], reverse = True)

#24. Write a Python program to count the elements in a list until an element  is a tuple.

almoco = ["arroz", "feijão", "batata", ("sobremesa", )]
cont = 0
for i in almoco:
    if isinstance(i, tuple):    
        break
    cont+=1

print(cont)


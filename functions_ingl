#1. Write a Python function to find the Max of three numbers
 def maior_numero(num1, num2, num3):
    if num1>=num2>=num3 or num1>=num3>=num2:
        print(f"O maior número é o : {num1}")
    elif num2>=num1>=num3 or num2>=num3>=num1:
        print(f"O maior número é o : {num2}")
    elif num3>=num2>=num1 or num3>=num1>=num2:
        print(f"O maior número é o : {num3}")
        
#2. Write a Python function to sum all the numbers in a list.
def soma_list():
    lista = []
    for i in range(5):
        seq = int(input("Digite um número: "))
        lista.append(seq)
    
    soma = sum(lista)
    print(f" A sequencia dos valores é de: {soma} ")
 
 #4. Write a Python program to reverse a string.
 
 def reverso():
    ele = input("Digite um elemento: ")
    ele1 = ele[:]
    ele2 = ele[::-1]
    print (f"o reverso desse elemento é: {ele2}")
    
    
    # 5. Write a Python function to calculate the factorial of a number (a non-negative integer).
    #The function accepts the number as an argument.
    
    def factorial(numero):
    fatorial = 1
    
    while numero > 1:
        fatorial = numero * fatorial
        numero = numero-1
   
    return fatorial  
    
    #6. Write a Python function to check whether a number is in a given range.
    def esta(num, lim_inferior, lim_superior):
    if num in range(lim_inferior, lim_superior):
        print("Este número está no intervalo")
    else:
        print("Esse número não está no intervalo")
        
     #7. Write a Python function that accepts a string and calculate 
     #the number of upper case letters and lower case letters.
     
     def quant_letras(frase):
    letra1 = 0
    letra2 = 0
    for l in frase:
        if l.isupper() == True:
            letra1 +=1
        elif  l.islower() == True:
            letra2 +=1    

    return letra1, letra2
    
    
    # 8. Write a Python function that takes a list and returns a new list
    #with unique elements of the first list.
    
    def lista(string):
    lista1 = string.split()
    lista2 = []
    for item in lista1:
        if item not in lista2:
            lista2.append(item) # não é a lista toda nádia, é só o elemento.
    
    return lista2
    
    #9. Write a Python function that takes a number as a parameter and check
    #the number is prime or not.
    
#esse foi um dos códigos mais difíceis que eu fiz até agora.
#Pensar em como passar do papel pro computador, foi trabalhoso.
#Mesmo que eu tivesse entendido a questão, confiar que eu ia conseguir 
#foi tenso. Mas eu consegui. Nem acredito...

def num_primo(num):
    divisor = 2
    while divisor <= num:
        if num % divisor !=0:
            divisor+=1
            if divisor == num and divisor % num == 0:
                print("Esse número é Lúcio.")
                break
        elif num == 2:
            print("Esse número é Lúcio.")
            break
        else:
            print("Esse número não é Lúcio.")
            break
            
            
#10. Write a Python program to print the even numbers from a given list. 
def pares(n):
    pares = []
    for num in n:
        if num % 2 == 0:
            pares.append(num)
    print(f"A sequência de números pares dessa lista é: {pares}")
    
    
# 11. Write a Python function to check whether a number is perfect or not.
def is_num_perfeito(n):
    soma1 = []
    for i in range (1,n):
        if n % i == 0:
            soma1.append(i)
    
    soma = sum(soma1)
    
    if soma == n:
        return True
    
    return False
    
#12. Write a Python function that checks whether a passed string is palindrome or not.

def palindromo(x):
    if x[:] == x[::-1]:
        print("Esse elemento é um palíndromo. ")
    else:
        print("Esse elemento nã é um palíndromo. ")
        
        
#14. Write a Python function to check whether a string is a pangram or not.
def pangram():
    abc = "abcdefghijlmnopqrstuvxz"
    abc = set(abc)
    frase = input("Digite uma frase: ").lower()
    if abc <= set(frase):
        return True
    else:
        return False
        
#15. Write a Python program that accepts a hyphen-separated sequence of words 
#as input and prints the words in a hyphen-separated sequence after 
#sorting them alphabetically.

def ordem(seq):
    palavra = seq.split("-")
    palavra.sort()

    return "-".join(palavra)
    
#16. Write a Python function to create and print a list where the values are
# square of numbers between 1 and 30 (both included).
def potencia():
    lista = []
    for i in range (1,31):
       lista.append(i**2)
    print(lista) #presta atenção nas suas indentações, Nádia...
    
    


    

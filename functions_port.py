#1. Faça um programa para imprimir para um n informado pelo usuário.Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. 

def n_linhas(n):
    lista = []
    for i in range (1,n+1):
        for j in range(i):
            lista.append(i)
    print(lista)
    
    
    
#2. Faça um programa para imprimir para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha. 

def sequencia(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i)
        print(lista)
        
        
#3. Faça um programa, com uma função que necessite de três argumentos,e que forneça a soma desses três argumentos. 

def soma(num1, num2, num3):
    resultado = num1 +num2+ num3
    return resultado
    
    
#4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
#e ‘N’, se seu argumento for zero ou negativo. 

def positivo_negativo(n):
    if n >0:
        print("P")
    elif n<=0:
        print("N")


#5. Faça um programa com uma função chamada somaImposto. # A função possui dois parâmetros formais: taxaImposto, que é a quantia 
#de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo 
#para incluir o imposto sobre vendas. 

def soma_imposto():
    custo = 75
    taxa_imposto = custo *3 /100
    total = custo + taxa_imposto
    print(f"O custo desse produto é de {custo} reais e a taxa de 3% sobre"
    + f"esse valor é de {taxa_imposto}. Num total de {total} reais ")
    
    
#6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: 
#uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário
# repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def horario(hora, minuto):
    A = "A.M"
    P = "P.M"
    antes = hora
    depois = hora-12
    if hora > 12:
        return  f"{depois}:{minuto:02d} {P}"
    else:
        return f"{antes}:{minuto:02d} {A}"
        
#7. Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá 
#solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará 
#o valor a ser pago e devolverá este valor ao programa que a chamou. 
#O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar 
#até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá 
#a quantidade e o valor total de prestações pagas no dia. O cálculo do valor  a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o 
#valor da prestação. Quando houver atraso, cobrar 3% de multa,  mais 0,1% de juros por dia de atraso. 

def valor_pagamento():
    prestacao = int(input("Digite o valor da prestação: "))
    atraso = int(input("Digite o número de dias de atraso do pagamento: "))
    multa = prestacao * 3/100
    juro = prestacao *1 /1000 * atraso
    if atraso == 0:
        valor_total = prestacao
        print(f"O valor a ser pago é de: {valor_total} ")
    else:
        valor_total = juro + multa + prestacao
        print(f"O valor a ser pago é de: {valor_total} ")
        
        
#8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 

def digitos(num):
    num = str(num)
    total = len(num)
    return total
    
#9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.

def reverso(n): 
    num1 = n[::-1]
    return num
    
#10. Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na 
#primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, 
#na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

def craps():
    d = random.randint(1, 7)
    d1 = random.randint(1, 7)
    d2 = random.randint(1, 7)
    d3 = random.randint(1, 7)
    ponto = int(d + d1)
    lanca = input("Digite 0 para começar o jogo ")
    while lanca != "0":
        lanca = input("Digite 0 para começar o jogo ")
    else:    
        rodada1 = print(f"{d}, {d1}")
        print(ponto)
        if ponto == 7 or ponto == 11:
            print("Você é um Natural. Você ganhou!")
        elif ponto == 2 or ponto == 3 or ponto == 12:
            print("Craps! Você perder...")
        else:
            de_novo = input(f"Seu ponto é:{ponto}. Jogue o dado novamente." +
                            "Aperte 00 ")
            while de_novo != "00":
                de_novo = input(f"Seu ponto é:{ponto}. Jogue o dado novamente." +
                            "Aperte 00 ")
            else:
                rodada2 = print(f"{d2}, {d3}")
                ponto2 = int(d2 + d3)
                print(ponto2)
            while ponto2 != ponto:
                d4 = random.randint(1, 7)
                d5 = random.randint(1, 7)
                de_novo = input(f"Seu ponto é:{ponto}. Jogue o dado novamente."
                                 + "Aperte 00 ")
                if de_novo == "00":
                    rodada3 = print(f"{d4}, {d5}")
                    ponto3 = int(d4 + d5)
                    print(ponto3)
                    if ponto3 == 7 or ponto2 == 7:
                        return "Você perdeu."
                    if ponto3 == ponto or ponto2 == ponto:
                        print ("Parabéns, você ganhou!")
                        break
                        
                        
#12. Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: 
#se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que
# todos os caracteres serão devolvidos em caixa alta ou caixa baixa,independentemente de como foram digitados.

import random


def embaralha(string):
    palavra = random.sample(string, len(string))
    palavra_nova = "".join(palavra).lower()
    print(palavra_nova)
    
    
#13. Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, 
#linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 o valor máximo é 20. Se valores fora da faixa forem informados, eles devem 
#ser modificados para valores dentro da faixa de forma elegante.

def valor_omissao(valor):
    if valor == " " or valor<1:
        return 1
    elif valor > 20:
        return 20
    else:
        return valor
    
    
def linha(num):
    l = "+"
    for x in range(num):
        l+= "-"
    l+="+"
    print(l)

def coluna(num,col):
    for y in range(col):
        c = "|"
        c+=" " *num
        c+="|"
        print(c)

def moldura(num, col):
    linha(num)
    coluna(num, col)
    linha(num)
    return moldura
    
    

    

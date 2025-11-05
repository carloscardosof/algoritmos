#arquivo onde devem vir as funções

def primeira_funcao():
    print("Primeira função!")

#Exercício 1
def ola():
    for i in range(4):
        print("olá mundo!")

#Exercício 2
def escrever(texto):
    print(texto)

#Exercício 3
def escrever_vezes(texto,numero):
    for x in range(numero):
        print(texto)

#Exercício 4
def soma(n1,n2):
    return n1+n2

#modo hard
def soma_variavel(*args):
    soma = 0
    for x in args:
        soma += x
    return soma

#Exercício 5
def maior(n1,n2):
    if n1>n2:
        return n1
    return n2

def div(n1,n2):
    
    
    try:
        print("deu certo")
        return n1/n2
    except ZeroDivisionError:
        print("deu erro")
        return None
    finally:
        print("vai de qq jeito")
        return None
    
def entrada():
    entr = input("Digite um número: ")

    try:
        numero = int(entr)
        if numero < 0:
            return -1
        return numero
    except:
        print("O valor digitado não é um número")
        return -1

x = 10

def ola_mundo():
    print('Olá mundo!')

def mostrar_numero():
    y = 4
    print(y)



def mostrar_numero2():
    y = 8
    print(y)

mostrar_numero()
mostrar_numero2()


def boas_vindas(nome):
    print("Bom dia "+nome)

boas_vindas("Carlos")

def raiz(num1, num2):
     return num1**num2

def mult(num1,num2):
    return num1*num2

def aritmetica(num1,num2,operacao="mult"):
    if operacao == "mult":
        return mult(num1,num2)
    elif operacao == "raiz":
        return raiz(num1,num2)
    else:
        print("Operação inválida")
        return None

print(aritmetica(operacao="mult",num2=3,num1=4))


def essa_cor_e_azul(cor):

    if cor == "azul":
        return True
    
    return False
    


    

print(essa_cor_e_azul("verde"))




def exibir_produto(nome,descricao="Sem descrição"):
    print(nome)
    if descricao != None:
        print(descricao)
    #print(nome+' '+descricao+' '+valor+' '+quantidade)

exibir_produto("Escova de dente", None)








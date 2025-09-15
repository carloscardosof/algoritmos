from datetime import datetime

print('Bem vindo à Papa Léguas Express!')

print('Entregamos seu produto em tempo recorde!')

ativo = True

produtos = ['arroz', 'tomate', 'café', 'refrigerante']

bairros = ['Renascença', 'Centro', 'São Francisco','Calhau','Cidade Operária','Bequimão','Anjo da Guarda']

pedidos = []

pedidos_entrega = [];

entregadores = ['João', 'Carlos', 'Ana', 'Roberta','Pedro', 'Luís', 'Marcos']

entregadores_caminho = []

entregas_finalizadas = []

id_pedido = 0

while ativo:
    
    comando = input('\nEscolha opção abaixo:\n'+
                    '[1] Cadastrar pedido\n'+
                    '[2] Exibir pedidos\n'+
                    '[3] Exibir pedidos que saíram para entrega\n'+
                    '[4] Exibir entregadores disponíveis\n'+
                    '[5] Exibir entregadores a caminho\n'+
                    '[6] Exibir entregas realizadas com sucesso\n'+
                    '[7] Encerrar o sistema\n')    
    match comando:
        case '1':
            cliente = input('Por favor, digite o seu nome:\n')
            produto = input('Produto:\n')
            quantidade = int(input('Quantidade:\n'))
            bairro = input('Bairro:\n')
            #horario = datetime.now()
            if not bairro in bairros:
                print('\nBairro não está disponível para entrega. Pedido cancelado.')
            else:
                if not produto in produtos:
                    print('\nProduto não encontrado! Pedido cancelado.')
                else:
                    id_pedido += 1 #aumenta o número global dos pedidos. cada novo pedido será com um novo número
                    print('\nO pedido '+str(id_pedido)+' foi registrado para o cliente '+cliente+':\n- Produto: '+produto+'\n- Quantidade:'+str(quantidade)+'\n- Bairro:'+bairro)

                    pedido = {
                        'id_pedido':id_pedido,
                        'cliente' : cliente,
                        'produto' : produto,
                        'quantidade' : quantidade,
                        'bairro' : bairro,
                        'horario': datetime.now()
                    }
                    
                    pedidos.append(pedido)
                    
                    if len(entregadores)>0 and len(pedidos)>2:
                        entrega = pedidos.pop(0)
                        print(pedidos[0])
                        pedidos_entrega.append(entrega)
                        entregador = entregadores.pop(0)
                        entregadores_caminho.append(entregador)
                        print('\nO pedido '+str(entrega['id_pedido'])+' saiu para a entrega!')
        case '2':
            if len(pedidos)>0:
                msg = '\nPedidos aguardando entrega:'
                
                for pedido in pedidos:
                    msg += '\n'
                    msg += 'id_entrega: '+pedido['id_entrega'],
                    msg += 'cliente: '+cliente['cliente']
                    
                    for chave, valor in pedido.items():
                        msg += '\n    '+chave+': '+str(valor)+', '
                
                print(msg[:-2])
            else:
                print('\nNenhum pedido registrado.')    
        case '3':
            print('entregas')
        
        case '4':
            print('entregadores 1')
        
        case '5':
            print('entregadores 2')
        
        case '6':
            print('sucesso')

        case '7':
            ativo = False
            print('\nEncerrando o sistema.')
        case _:
            print('Comando inválido!')


print('Obrigado por usar a Papa Léguas Express!')








    
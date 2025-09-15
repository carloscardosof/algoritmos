from datetime import datetime


print('Bem vindo à Papa Légua Express!')

print('Entregamos seu produto em tempo recorde!')

bairros = ['Renascença', 'Centro', 'São Francisco','Calhau','Cidade Operária','Bequimão','Anjo da Guarda']

produtos = ['arroz', 'tomate', 'café', 'refrigerante']

cliente = input('Por favor, digite o seu nome:\n')

produto = input('Produto:\n')

quantidade = input('Quantidade:\n')

bairro = input('Bairro:\n')

horario = datetime.now();

print('O pedido abaixo foi registrado para o cliente '+cliente+':\n- Produto: '+produto+'\n- Quantidade: '+quantidade+'\n- Bairro: '+bairro+'\n- Horário: '+str(horario))



if not bairro in bairros:
    print('Bairro não está disponível para entrega. Pedido cancelado.')
elif not produto in produtos:
    print('Produto não encontrado! Pedido cancelado.')
else:
    print('Compra registrada com sucesso!')
    
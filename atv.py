# 1 - Crie um dicionário d  e coloque nele seus dados: nome, idade,
# telefone,endereço. Usando o dicionário d criado anteriormente, imprima
# seu nome.


# d = {
#     'nome': 'ingred',
#     'idade': '22',
#     'telefone': '75123456',
#     'endereco': 'rua a',
# }


# print(d['nome'])


# 2- Crie um dicionário d e coloque nele os dados fornecidos pelo usuário:
# nome, idade, telefone,endereço. Também usando d, imprima todos os
# itens do dicionário no formato chave : valor, ordenado pela chave


# Cria um dicionário vazio
# d= {}

# Solicita os dados do usuário
# nome = input("Digite o nome: ")
# idade = input("Digite a idade: ")
# telefone = input("Digite o telefone: ")
# endereco = input("Digite o endereço: ")

# Preenche o dicionário com os dados do usuário
# d['nome'] = nome
# d['idade'] = idade
# d['telefone'] = telefone
# d['endereço'] = endereco

# Imprime os itens do dicionário ordenados pela chave
# for chave, valor in sorted(d.items()):
#     print(f"{chave}: {valor}")





# 3- Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
# chave (cpf), nome, idade, telefone. O programa deve ler um número
# indeterminado de dados, criar a agenda e imprimir todos os itens do
# dicionário no formato chave: nome-idadefone.


# d ={}


# cpf = int(input("Digite seu cpf: "))
# nome = input(" Insira seu nome: ")
# idade = int(input("Digite sua idade: "))
# tel = int(input("Digite seu telefone: "))


# d.append([cpf, nome, idade, tel])


# print(d)
# listaordenada = sorted(d)


# for item in listaordenada:
#     print('cpf:{} nome:{} idade:{} tel:{}' .format(item[0], item[1], item[2], item[3]))




# 4- Crie um programa que cadastre informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um dicionário. Depois remova todas as
# pessoas menores de 18 anos do dicionário e coloque em outro dicionário.


# d={}


# while True:
#     nome= input("Informe seu nome: ")
#     if nome =='':
#         break
#     cpf= int(input("Informe seu cpf: "))
#     idade= int(input("Informe sua idade: "))
#     tel= int(input("Informe seu telefone"))
#     d[nome] = (cpf,idade,tel)


#     print (d)


#     dados ={i:d[i] for i in sorted(d)}
#     print(dados)


#     menores_18 = {}
#     maiores_18 = {}


#     for i, v in dados.items():
#         if v[0] < 18:
#             menores_18[i] = v
#         else:
#             maiores_18[i] = v


#         del d,dados
#         print(menores_18)
#         print(maiores_18)


# 5- Considere um sistema onde os dados são armazenados em dicionários.
# Nesse sistema existe um dicionario principal e o dicionário de backup.
# Cada vez que o dicionário principal atinge tamanho 5, ele imprime os
# dados na tela e apaga o seu conteúdo. Crie um programa que insira dados
# em um dicionário, realizando o backup a cada dado e excluindo os dados
# do dicionário principal quando ele atingir tamanho 5.


# 6- Escreva uma função que conta a quantidade de vogais em um texto e
# armazena tal quantidade em um dicionário, onde a chave é a vogal
# considerada.

# def contar_vogais(texto):
#     contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
   
#     texto = texto.lower()
    
#     for letra in texto:
#         if letra in contagem_vogais:
#             contagem_vogais[letra] += 1
            
#     return contagem_vogais


# texto = input("Digite um texto: ")


# resultado = contar_vogais(texto)

# for vogal, contagem in resultado.items():
#     print(f"{vogal}: {contagem}")




# 7) Escreva um programa que lê duas notas de vários alunos e armazena tais
# notas em um dicionário, onde a chave é o nome do aluno. A entrada de
# dados deve terminar quando for lida uma string vazia como nome.
# Escreva uma função que retorna a média do aluno, dado seu nome.

# def calcular_media(notas):
#     soma = sum(notas)
#     media = soma / len(notas)
#     return media

# notas_alunos = {}  

# while True:
#     nome = input("Digite o nome do aluno (ou pressione Enter para sair): ")
    
#     if nome == "":
#         break
    
#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))
    
#     notas_alunos[nome] = [nota1, nota2]

# nome_aluno = input("Digite o nome do aluno para calcular a média: ")

# if nome_aluno in notas_alunos:
#     notas = notas_alunos[nome_aluno]
#     media = calcular_media(notas)
#     print(f"A média do aluno {nome_aluno} é {media:.2f}")
# else:
#     print("Aluno não encontrado.")


# 8) Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
# Escreva um programa que leia todos os tempos em segundos e os guarde
# em um dicionário, onde a chave é o nome do corredor. Ao final diga de
# quem foi a melhor volta da prova e em que volta; e ainda a classificação
# final em ordem (1o o campeão). O campeão é o que tem a menor média
# de tempos.


# def calcular_media_tempos(tempos):
#     return sum(tempos) / len(tempos)

# corredores = {
#     "Corredor 1": [],
#     "Corredor 2": [],
#     "Corredor 3": [],
#     "Corredor 4": [],
#     "Corredor 5": [],
#     "Corredor 6": []
# }

# for volta in range(1, 11):
#     print(f"Voltas da {volta}ª volta:")
#     for corredor in corredores:
#         tempo = float(input(f"Tempo para {corredor}: "))
#         corredores[corredor].append(tempo)





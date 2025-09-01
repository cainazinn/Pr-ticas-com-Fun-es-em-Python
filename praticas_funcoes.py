#Prática Funções:

#Três formas de mostrar o nome e o sobrenome do usuário usando função

# def minha_funcao(nome, sobrenome):
#     print("Prazer", nome, sobrenome + ".")

# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")    

#nome e sobrenome (nesse caso) são variáveis globais, portanto podem ser usadas dentro de funções.

# minha_funcao(nome, sobrenome)



# def minha_funcao():
#     print("Prazer", nome, sobrenome + ".")

# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# minha_funcao()



# def minha_funcao(nome, sobrenome):
#     print("Prazer", nome, sobrenome + ".")

# minha_funcao(nome = input("Digite seu nome: "), sobrenome = input("Digite seu sobrenome: "))

#----------------------------------------------------------------------------------------------------------------------------

#Somando valores utilizando função

# def somar(numero_1, numero_2):
#     soma = numero_1 + numero_2
#     print(f"A soma entre {numero_1} e {numero_2} é igual a {soma}.")

# somar(42, 60)

#ou

# def somar(n1, n2):
#     soma = n1 + n2
#     return soma

# resultado_da_soma = somar(4, 5)
# print(f"O resultado da primeira soma é igual a {resultado_da_soma}")

# resultado_de_outra_soma = somar(10, 20)
# print(f"O resultado da segunda soma é igual a {resultado_de_outra_soma}")

#----------------------------------------------------------------------------------------------------------------------------

# def verific_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
    
# if verific_par(17):
#     print("É par!")
# else:
#     print("É ímpar!")


# def verific_nome(nome):
#     if len(nome) > 3:
#         return True
#     else:
#         return False
    
# if verific_nome("Ca"):
#     print("Seu número tem mais que 3 caracteres!")
# else:
#     print("Seu nome tem menos que 3 caracteres!")


# def somar(n1, n2):
#     soma = n1 + n2
#     return soma

# resultado = somar(3, 4)
# print(f"O resultado da soma é igual a {resultado}")


# def somar_lista(*numeros):
#     soma = 0 
#     for n in numeros:
#         soma += n
#     return soma

# soma_dos_numeros_da_lista = somar_lista(6, 5, 4, 3, 2, 1)
# print(f"A soma de todos os números da lista é igual a", soma_dos_numeros_da_lista)

# def calcular_media(*numeros):
#     soma = 0
#     quantidade = len(numeros)

#     for n in numeros:
#         soma += n
#     media = soma / quantidade
#     return media

# resultado = calcular_media(2, 4, 5, 11, 3)
# print(resultado)

#Exercícios
#01 - Crie uma função que recebe um número, e faz um contador regressivo a partir dele. 

# def contagem_regressiva(numero):
    
#     for n in range(numero, -1, -1):
#         print(n)

# numero = int(input("Defina de onde você deseja que inicie a contagem: "))

# contagem_regressiva(numero)


#agora usando return

# def contagem_regressiva(numero):
#     contagem = []

#     for n in range(numero, -1, -1):
#         contagem.append(n)

#     return contagem

# numero = int(input("Defina de onde você deseja que a contagem regressiva comece: "))
# resultado = contagem_regressiva(numero)

# for n in resultado:
#     print(n)

#02 - Crie uma função que recebe uma lista e retorne o maior número dessa lista.

# def maior_num_lista(*numeros):
#     maior_num = numeros[0]

#     for n in numeros:

#         if n > maior_num:
#             maior_num = n
#     print(numeros)
#     return maior_num
    
# resultado = maior_num_lista(6, 5, 3, 7, 11, 9)
# print(f"O maior número dessa lista é {resultado}.")

# numero = 30
# for n in range(10, -1, -1):
#     print(n)
    

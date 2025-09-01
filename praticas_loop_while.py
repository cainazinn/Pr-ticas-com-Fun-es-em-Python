# Utilizando for
# for i in range(1, 9):
#     print(i)
# print("FIM")

# Utilizando while

#Prática 1

# numero = 0
# while numero < 10:
#     print(numero)
#     numero += 1

n = 1
par = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        par +=1
    print(par)
print("FIM")

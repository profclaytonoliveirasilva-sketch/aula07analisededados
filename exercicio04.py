'''
Construir um algoritmo que tenha a entrada de números inteiros escolhidos
pelo usuário. A quantidade será escolhida, também, pelo usuário e o 
algoritmo mostrará:
1 - uma lista com todos os números
2 - uma lista com números ímpares
3 - uma lista com os números em ordem crescente
4 - uma lista com os números em ordem descrescente
5 - uma lista com um número removido pelo usuário
'''
print("Exercício\n")
numeros = []
qtde = int(input("Escolha a quantidade de números para a lista: "))
for i in range(qtde):
    numero = int(input(f"Insira o {i+1}º Número: "))
    numeros.append(numero)
print(f"Números digitados: {numeros}\n")
print("Números ímpares\n")
for i in numeros:
    if i %2 == 1: #ou i %2 != 0:
        print(i)
print("Ordem Crescente:\n")
numeros.sort()
print(f"Números {numeros}")
print("Ordem Descrescente:\n")
numeros.sort(reverse=True)
print(f"Números {numeros}")
numero_r = int(input("Escolha um número para remover: "))
numeros.remove(numero_r)
numeros.sort(reverse=False)
print(f"Números atualizados: {numeros}")
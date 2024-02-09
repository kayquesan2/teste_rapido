ordemL = int(input("Digite o valor de Linhas: "))
ordemC = int(input("Digite o valor de Colunas: "))

matriz = []

while ordemC > 10 or ordemL > 10:
    ordemL = int(input("Digite o valor de Linhas: "))
    ordemC = int(input("Digite o valor de Colunas: "))

for i in range(0,ordemL,1):
    matriz.append([])

for l in range (0, ordemL, 1):
    for c in range (0, ordemC, 1):
        valor = int(input("Digite o valor: "))
        matriz[l] = valor

for i in range(0,ordemL,1):
    print(matriz[i])

consulta = int(input("Digite um valor que deseja consultar na lista?"))

for l in range (0, ordemL, 1):
    for c in range (0, ordemC, 1):
        if consulta == matriz[l][c]:
            print(f"posição: {matriz[l][c]+1} ")
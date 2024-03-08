import os
os.system("cls")

NLA = int(input("Digite o num de LINHAS da Matriz A: "))
NCA = int(input("Digite o num de COLUNAS da Matriz A: "))
print()

A = []                      #Cria a Matriz A
for i in range(0, NLA):
    A.append( [] )
    for j in range(0, NCA):
        A[i].append (0)

for i in range(0, NLA):     #Percorre a matriz add seus respectivos valores
    for j in range(0, NCA):
        A[i][j] = float(input("Digite A[%d][%d]: " %(i+1, j+1)))

print()

NLB = int(input("Digite o num de LINHAS da Matriz B: "))
NCB = int(input("Digite o num de COLUNAS da Matriz B: "))
print()

B = []                      #Cria a Matriz B
for i in range(0, NLB):
    B.append( [] )
    for j in range(0, NCB):
        B[i].append(0)

for i in range(0, NLB):     #Percorre a matriz add seus respectivos valores
    for j in range(0, NCB):
        B[i][j] =float(input("Digite B[%d][%d]: " %(i+1, j+1)))

print()

if(NCA == NLB):             #Verifica se a COLUNA de A é = a LINHA de B

    C = []                  #Cria a Matriz C
    for i in range(0, NLA):
        C.append( [] )
        for j in range(0, NCB):
            C[i].append(0)

    for i in range(NLA):
        for j in range(NCB):
            soma = 0
            for k in range(0, NLB):
                soma += A[i][k] * B[k][j]   #Realiza o calculo
            C[i][j] = soma

    print("Matriz A")       #Exibe tds as matrizes
    for i in range(0, NLA):
        for j in range(0, NCA):
            print("%5.1f" %A[i][j], end=" ")
        print()
    
    print()
    print("Matriz B")
    for i in range(0, NLB):
        for j in range(0, NCB):
            print("%5.1f" %B[i][j], end=" ")
        print()  

    print()
    print("Matriz C")
    for i in range(0, NLA):
        for j in range(0, NLA):
            print("%5.1f" %C[i][j], end=" ")
        print()
    print()

else:
    print("O num de COLUNAS da Matriz A PRECISA ser igual ao num de LINHAS da Matriz B")
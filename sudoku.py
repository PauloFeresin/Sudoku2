# exercicio 1383 do beecrowd - impacta

sudoku = []

n = int(input())
teste = 0
# for i in range(0,n+1):
    
# print("Instancia", i)
for linhas in range(9):
    linha = []

    for colunas in range(1):
        entrada = input()
        entrada = entrada.split()
        linha.extend(entrada)

    sudoku.append(linha)

# print(sudoku)

colunas = []

falhas = 0
acertos = 0


# verifica colunas
cont = 0
for i in range(0, 9):
    for linha in sudoku:
        digito = linha[cont]
        colunas.append(digito)
        if len(set(linha)) != len(linha):
            falhas += 1
        else:
            acertos += 1

    cont += 1


# verifica linhas
for linha in sudoku:
    if len(set(linha)) != len(linha):
        falhas += 1
    else:
        acertos += 1

# verifica matrizes 3x3








if falhas > 0:
    print("NAO")
if acertos > 0:
    print("SIM")










# def testa_sudoku(n):
#     for i in range(1,n+1):
    
#         print("Instancia", i)
#         for linhas in range(9):
#             linha = []

#             for colunas in range(1):
#                 entrada = input()
#                 entrada = entrada.split()
#                 linha.extend(entrada)

#             sudoku.append(linha)

#         # print(sudoku)

#         colunas = []
#         cont = 0

#         for i in range(0, 9):
#             for linha in sudoku:
#                 digito = linha[cont]
#                 colunas.append(digito)
#                 if len(set(linha)) != len(linha):
#                     print("NAO")
#                 else:
#                     print("SIM")
#                     break

#             cont += 1



#         for linha in sudoku:
#             if len(set(linha)) != len(linha):
#                 print("NAO")
#             else:
#                 print("SIM")
#                 break

# testa_sudoku(n)
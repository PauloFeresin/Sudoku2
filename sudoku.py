# exercicio 1383 do beecrowd - impacta

sudoku = []

n = int(input())
teste = 0
for i in range(0,n+1):
    
    print("Instancia", i)
    for linhas in range(9):
        linha = []

        for colunas in range(1):
            entrada = input()
            entrada = entrada.split()
            linha.extend(entrada)

        sudoku.append(linha)

    # print(sudoku)

    colunas = []
    cont = 0

    for i in range(0, 9):
        for linha in sudoku:
            digito = linha[cont]
            colunas.append(digito)
            if len(set(linha)) != len(linha):
                print("NAO")

        cont += 1



    for linha in sudoku:
        if len(set(linha)) != len(linha):
            print("NAO")


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
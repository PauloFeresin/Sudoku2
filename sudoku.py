## exercicio 1383 do beecrowd - impacta

sudoku = []

for linhas in range(9):
    linha = []

    for colunas in range(1):
        entrada = input()
        linha.append((entrada))
        
    sudoku.append(linha)

print(sudoku)

